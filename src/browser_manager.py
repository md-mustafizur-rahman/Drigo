import os
import base64
import time
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


class BrowserManager:
    """
    Manages a Playwright browser to search YouTube,
    take screenshots, and navigate to videos.
    """

    def __init__(self):
        self._playwright = None
        self._browser = None
        self._page = None
        self._screenshot_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "screenshots", "youtube_search.png"
        )
        os.makedirs(os.path.dirname(self._screenshot_path), exist_ok=True)
        print("[*] BrowserManager initialized.")

    def _ensure_browser(self):
        """Launch the browser if it isn't already running."""
        try:
            if self._browser is None or not self._browser.is_connected():
                print("[*] Launching browser...")
                self._playwright = sync_playwright().start()
                self._browser = self._playwright.chromium.launch(
                    headless=False,          # Show the browser window to the user
                    args=["--start-maximized"]
                )
                context = self._browser.new_context(
                    no_viewport=True         # Let the browser use its maximized size
                )
                self._page = context.new_page()
                print("[*] Browser launched (headed/visible mode).")
        except Exception as e:
            print(f"[Browser ERROR] Failed to ensure browser: {e}")
            self.close()  # Cleanup and allow for retry next time
            raise e

    def search_youtube(self, query: str) -> str | None:
        """
        Opens YouTube, searches for `query`, waits for results,
        and takes a screenshot.

        Returns the base64-encoded PNG screenshot, or None on failure.
        """
        try:
            self._ensure_browser()

            search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
            print(f"[*] Navigating to: {search_url}")
            self._page.goto(search_url, wait_until="domcontentloaded", timeout=20000)

            # Wait for video cards to appear
            self._page.wait_for_selector("ytd-video-renderer, ytd-compact-video-renderer", timeout=15000)
            time.sleep(1.5)  # Allow thumbnails to settle

            print(f"[*] Taking FOCUSED screenshot of search results...")
            
            # Try to capture ONLY the primary results container to avoid browser/OS UI distraction
            results_container = self._page.query_selector("ytd-search, #contents.ytd-item-section-renderer")
            if results_container:
                results_container.screenshot(path=self._screenshot_path)
            else:
                # Fallback to viewport if container not found
                self._page.screenshot(path=self._screenshot_path, full_page=False)

            # Return base64 for vision analysis
            with open(self._screenshot_path, "rb") as f:
                b64 = base64.b64encode(f.read()).decode("utf-8")
            print(f"[+] Focused screenshot captured ({len(b64)} chars base64)")
            return b64

        except PlaywrightTimeoutError as e:
            print(f"[Browser ERROR] Timeout while searching YouTube: {e}")
            return None
        except Exception as e:
            print(f"[Browser ERROR] {e}")
            return None

    def scroll_down(self, steps=1):
        """Scrolls the search results down to find more videos."""
        try:
            if not self._page:
                return
            print(f"[*] Scrolling down ({steps} steps)...")
            for _ in range(steps):
                self._page.keyboard.press("PageDown")
                time.sleep(0.8)
            time.sleep(1.0) # Wait for images to load
        except Exception as e:
            print(f"[Browser ERROR] Failed to scroll: {e}")

    def play_first_video(self) -> bool:
        """
        Clicks the first non-ad video result on the current YouTube search page.
        Returns True on success, False on failure.
        """
        try:
            if self._page is None:
                print("[Browser ERROR] No page open. Call search_youtube() first.")
                return False

            # Click the first organic video result title link
            first_video = self._page.query_selector("ytd-video-renderer #video-title")
            if first_video is None:
                print("[Browser WARNING] Could not find first video element.")
                return False

            title = first_video.get_attribute("title") or first_video.inner_text()
            print(f"[*] Clicking video: {title}")
            first_video.click()

            # Wait for the video player to appear
            self._page.wait_for_selector("video", timeout=15000)
            print("[+] Video is now playing!")
            return True

        except PlaywrightTimeoutError:
            print("[Browser ERROR] Timeout waiting for video player.")
            return False
        except Exception as e:
            print(f"[Browser ERROR] Could not click video: {e}")
            return False

    def close(self):
        """Close the browser and stop Playwright gracefully."""
        try:
            if self._browser and self._browser.is_connected():
                self._browser.close()
            if self._playwright:
                self._playwright.stop()
            self._browser = None
            self._page = None
            print("[*] Browser closed.")
        except Exception as e:
            print(f"[Browser] Error during close: {e}")

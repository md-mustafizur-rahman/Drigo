import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

class LLMEngine:
    def __init__(self):
        self.provider = os.getenv("LLM_PROVIDER", "ollama").lower()
        self.system_prompt = "You are a helpful voice assistant named Drigo. Always respond in English unless specifically asked otherwise. Keep your responses concise and friendly."

        if self.provider == "gemini":
            from google import genai
            from google.genai import types
            self._genai_types = types
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                print("[WARNING] Gemini API Key is missing! Please configure GEMINI_API_KEY in .env.")
            self.gemini_client = genai.Client(api_key=api_key)
            self.model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
            print(f"[*] Initialized LLM Engine: Gemini ({self.model_name})")
        else:
            self.model_name = os.getenv("OLLAMA_MODEL", "llama3.1")
            self.url = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434/api/generate")
            print(f"[*] Initialized LLM Engine: Ollama ({self.model_name})")

    def generate_streaming_response(self, prompt: str):
        """
        Sends a prompt to the corresponding LLM API and yields the generated text chunks.
        """
        if self.provider == "gemini":
            try:
                config = self._genai_types.GenerateContentConfig(
                    system_instruction=self.system_prompt
                )
                response_stream = self.gemini_client.models.generate_content_stream(
                    model=self.model_name,
                    contents=prompt,
                    config=config
                )
                for chunk in response_stream:
                    if chunk.text:
                        yield chunk.text
            except Exception as e:
                error_msg = f"[LLM ERROR] Failed to connect to Gemini: {e}"
                print(f"\n{error_msg}")
                yield error_msg
        else:
            payload = {
                "model": self.model_name,
                "prompt": prompt,
                "system": self.system_prompt,
                "stream": True
            }

            try:
                response = requests.post(
                    self.url,
                    json=payload,
                    headers={"Content-Type": "application/json"},
                    timeout=90,
                    stream=True
                )
                response.raise_for_status()
                
                for line in response.iter_lines():
                    if line:
                        data = json.loads(line.decode("utf-8"))
                        chunk = data.get("response", "")
                        if chunk:
                            yield chunk
                        if data.get("done"):
                            break
            except requests.exceptions.RequestException as e:
                error_msg = f"[LLM ERROR] Failed to connect to Ollama: {e}"
                print(f"\n{error_msg}")
                yield error_msg
            except Exception as e:
                error_msg = f"[LLM ERROR] An unexpected error occurred: {e}"
                print(f"\n{error_msg}")
                yield error_msg

    def generate_response(self, prompt: str) -> str:
        """
        Wrapper for non-streaming response.
        """
        full_response = ""
        for chunk in self.generate_streaming_response(prompt):
            if "LLM ERROR" in chunk:
                if not full_response:
                    return chunk
            full_response += chunk
        return full_response

    def analyze_image(self, prompt: str, image_base64: str) -> str:
        """
        Sends a vision prompt + base64 image to Ollama (llava model).
        Returns the model's text description.
        """
        # Always use the Ollama backend for vision (llava is local)
        model = os.getenv("OLLAMA_MODEL", "llava")
        url = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434/api/generate")

        payload = {
            "model": model,
            "prompt": prompt,
            "images": [image_base64],
            "stream": False
        }

        try:
            print(f"[*] Sending screenshot to {model} for analysis...")
            response = requests.post(
                url,
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=120
            )
            response.raise_for_status()
            data = response.json()
            return data.get("response", "[No response from vision model]")
        except requests.exceptions.RequestException as e:
            error_msg = f"[Vision ERROR] Failed to connect to Ollama: {e}"
            print(f"\n{error_msg}")
            return error_msg
        except Exception as e:
            error_msg = f"[Vision ERROR] Unexpected error: {e}"
            print(f"\n{error_msg}")
            return error_msg

if __name__ == "__main__":
    # Quick test
    llm = LLMEngine()
    test_prompt = "Say hello!"
    print(f"Test Prompt: {test_prompt}")
    print(f"Response: {llm.generate_response(test_prompt)}")

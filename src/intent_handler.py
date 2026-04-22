import re

def detect_youtube_intent(text: str) -> bool:
    """
    Returns True if the user wants to watch a YouTube video.
    Trigger phrases: 'youtube' AND ('video' OR 'show me' OR 'play' OR 'watch' OR 'clip' OR 'search' OR 'find')
    """
    t = text.lower()
    has_youtube = "youtube" in t
    has_action = any(kw in t for kw in ["video", "show me", "play", "watch", "clip", "search", "find", "open", "look up"])
    return has_youtube and has_action

def extract_search_query(text: str) -> str:
    """
    Extract the search topic from the voice command.
    Handles conversational natural language better.
    """
    t = text.lower()
    
    # 1. Try specific regex patterns for common phrasing
    patterns = [
        r"(?:show|play|watch|find|search for) (?:a |an |some )?(.*?) (?:video|clip|gameplay|song)s? (?:on|from) youtube",
        r"(?:show|play|watch|find|search for) (?:a |an |some )?(.*?) (?:on|from) youtube",
        r"youtube (?:search|find|for) (.*)",
        r"on youtube (?:show|play|watch) (.*)",
        r"(.*?) on youtube",
    ]
    
    for pattern in patterns:
        m = re.search(pattern, t)
        if m:
            query = m.group(1).strip()
            # Clean up leading/trailing filler
            query = re.sub(r"^(?:me|a|an|the|some|please|drigo|search|find|play|watch)\s+", "", query)
            if query:
                return query
            
    # 2. Fallback: Systematic Cleanup
    # Remove obvious filler phrases manually
    clean_text = t
    # Remove the "youtube" core trigger
    clean_text = re.sub(r"\bon youtube\b", "", clean_text)
    clean_text = re.sub(r"\byoutube\b", "", clean_text)
    
    # Remove action verbs and helper words
    fillers = [
        "drigo", "please", "could you", "can you", "i want to", "i'd like to",
        "show me", "play", "watch", "search for", "find", "look up", "open",
        "a video", "the video", "a song", "the song", "video of", "song of",
        "a clip", "the clip", "latest", "newest", "on the", "will be", "is",
        "for", "of", "about", "search"
    ]
    
    for word in fillers:
        clean_text = re.sub(r"\b" + re.escape(word) + r"\b", "", clean_text)
        
    # Clean redundant punctuation and whitespace
    clean_text = re.sub(r"[?!.,]", " ", clean_text)
    clean_text = " ".join(clean_text.split()).strip()
    
    # Final check for "ai" in query (often from 'Drigo AI')
    clean_text = re.sub(r"\bai\b", "", clean_text).strip()
    
    return clean_text if clean_text else "trending videos"



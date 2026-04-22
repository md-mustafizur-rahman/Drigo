from src.intent_handler import detect_youtube_intent, extract_search_query

test_transcripts = [
    "show me minecraft video on youtube",
    "play alan walker song on youtube",
    "could you play a video on the youtube? the video will be aaron walker latest song.",
    "drigo AI search cute cats on youtube please",
    "watch interstellar trailer on youtube"
]

for t in test_transcripts:
    detected = detect_youtube_intent(t)
    query = extract_search_query(t)
    print(f"Transcript: {t}")
    print(f"  Detected: {detected}")
    print(f"  Query:    '{query}'")
    print("-" * 20)

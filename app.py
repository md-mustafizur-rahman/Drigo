import os
from flask import Flask, render_template, request, send_file, jsonify
from flask_cors import CORS
import io
import wave
from src.tts import FishSpeechTTS
from src.stt import WhisperSTT
from src.llm import LLMEngine
from dotenv import load_dotenv
import librosa
import numpy as np
import tempfile

load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize AI Engines
tts_engine = FishSpeechTTS()
stt_engine = WhisperSTT()
llm_engine = LLMEngine()

# Mock user database (in-memory)
users = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/add-user', methods=['POST'])
def add_user():
    data = request.json
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400

    # Mock adding user to database
    user = {"name": name, "email": email}
    users.append(user)
    print(f"[*] Added user: {name} ({email})")

    # Generate voice response
    response_text = f"User {name} has been added successfully."
    audio_data = tts_engine.synthesize(response_text)

    if audio_data:
        # Return audio data as a response
        print(f"[+] Voice response ready ({len(audio_data)} bytes).")
        return send_file(
            io.BytesIO(audio_data),
            mimetype="audio/wav",
            as_attachment=False,
            download_name="response.wav"
        )
    else:
        print("[!] Voice generation failed completely.")
        return jsonify({
            "success": True,
            "message": response_text,
            "warning": "User added, but voice response failed (TTS engine unavailable)."
        }), 200

@app.route('/api/voice-command', methods=['POST'])
def voice_command():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file uploaded"}), 400
        
    audio_file = request.files['audio']
    
    # Save the uploaded file temporarily
    # The browser now sends a WAV file, which is easier to decode
    with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as temp_audio:
        audio_file.save(temp_audio.name)
        temp_path = temp_audio.name
        
    try:
        # Load and resample to 16kHz
        # librosa can handle most audio formats if ffmpeg/pysoundfile is present
        audio_np, sr = librosa.load(temp_path, sr=16000)
        
        # WhisperSTT.transcribe_raw handles the transcription
        transcript = stt_engine.transcribe_raw(audio_np)
        
        if not transcript.strip():
            return jsonify({
                "transcript": "",
                "message": "I couldn't hear anything. Please try again.",
                "error": "Empty transcription"
            }), 200
            
        print(f"[*] Voice Command Transcript: {transcript}")
        
        # Generate LLM Response
        ai_response = llm_engine.generate_response(transcript)
        print(f"[*] AI Response: {ai_response}")
        
        # Synthesize Voice
        audio_data = tts_engine.synthesize(ai_response)
        
        # Prepare response (sending text and audio)
        import base64
        audio_base64 = base64.b64encode(audio_data).decode('utf-8') if audio_data else None
        
        if not audio_base64:
            print("[!] Voice synthesis failed for voice command.")

        return jsonify({
            "transcript": transcript,
            "ai_response": ai_response,
            "audio": audio_base64,
            "tts_error": audio_data is None
        })
        
    except Exception as e:
        import traceback
        print(f"[ERROR] Voice Command Processing Failed: {e}")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500
    finally:
        # Cleanup temp file
        if 'temp_path' in locals() and os.path.exists(temp_path):
            os.remove(temp_path)

@app.route('/api/test-ollama', methods=['GET', 'POST'])
def test_ollama():
    try:
        # Prompt for the test
        prompt = request.json.get('prompt', 'Hello, are you running on my GPU?') if request.method == 'POST' and request.is_json else 'Hello, are you running on my GPU?'
        
        print(f"[*] Testing Ollama connection with prompt: '{prompt}'")
        ai_response = llm_engine.generate_response(prompt)
        print(f"[*] Ollama Response: {ai_response}")
        
        return jsonify({
            "success": True,
            "prompt": prompt,
            "ollama_response": ai_response
        })
    except Exception as e:
        import traceback
        print(f"[ERROR] Ollama Test Failed: {e}")
        traceback.print_exc()
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

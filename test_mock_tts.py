import unittest
from unittest.mock import patch, MagicMock
import os
import io
import wave
import numpy as np
from src.tts import FishSpeechTTS
from src.audio import AudioHandler

class TestFishSpeechIntegration(unittest.TestCase):
    def setUp(self):
        self.tts = FishSpeechTTS()
        self.audio_handler = AudioHandler()

    def create_dummy_wav(self):
        """Creates a 1-second silent WAV file in memory."""
        buffer = io.BytesIO()
        with wave.open(buffer, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(16000)
            wf.writeframes(np.zeros(16000, dtype=np.int16).tobytes())
        return buffer.getvalue()

    @patch('requests.post')
    def test_tts_synthesize_mock(self, mock_post):
        # Mock successful API response
        dummy_wav = self.create_dummy_wav()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = dummy_wav
        mock_post.return_value = mock_response

        # Test synthesis
        audio_data = self.tts.synthesize("Hello world")
        
        self.assertIsNotNone(audio_data)
        self.assertEqual(audio_data, dummy_wav)
        mock_post.assert_called_once()

    @patch('pyaudio.PyAudio')
    def test_audio_playback_mock(self, mock_pyaudio):
        # Mock PyAudio setup
        mock_pa_instance = mock_pyaudio.return_value
        mock_stream = MagicMock()
        mock_pa_instance.open.return_value = mock_stream

        dummy_wav = self.create_dummy_wav()
        
        # Test playback
        self.audio_handler.play_audio(dummy_wav)
        
        # Verify stream was opened and written to
        mock_pa_instance.open.assert_called()
        mock_stream.write.assert_called()
        mock_stream.stop_stream.assert_called()
        mock_stream.close.assert_called()

if __name__ == '__main__':
    unittest.main()

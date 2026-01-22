import os
import tempfile
from faster_whisper import WhisperModel

TEMP_DIR = os.path.join(os.getcwd(), "temp_audio")
os.makedirs(TEMP_DIR, exist_ok=True)

class Transcriber:
    def __init__(self):
        self.model = WhisperModel("small", device="cpu", compute_type="int8")

    def transcribe(self, audio_bytes):
        with tempfile.NamedTemporaryFile(dir=TEMP_DIR, suffix=".webm", delete=False) as f:
            f.write(audio_bytes)
            file_path = f.name

        segments, info = self.model.transcribe(file_path)
        text = " ".join([seg.text for seg in segments])

        return {
            "text": text.strip(),
            "language": info.language
        }

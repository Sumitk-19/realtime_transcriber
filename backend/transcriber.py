import subprocess
import tempfile
from faster_whisper import WhisperModel

class Transcriber:
    def __init__(self):
        self.model = WhisperModel("small", device="cpu", compute_type="int8")

    def transcribe(self, audio_bytes):
        with tempfile.NamedTemporaryFile(suffix=".webm") as f:
            f.write(audio_bytes)
            f.flush()

            segments, info = self.model.transcribe(f.name)
            text = " ".join([seg.text for seg in segments])

            return {
                "text": text.strip(),
                "language": info.language
            }

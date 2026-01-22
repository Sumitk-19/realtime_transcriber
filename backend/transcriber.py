import numpy as np
from faster_whisper import WhisperModel

class Transcriber:
    def __init__(self):
        self.model = WhisperModel("small", device="cpu", compute_type="int8")
        self.buffer = b""

    def transcribe(self, audio_bytes):
        self.buffer += audio_bytes

        # Ensure even number of bytes for int16
        if len(self.buffer) % 2 != 0:
            self.buffer = self.buffer[:-1]

        audio_np = np.frombuffer(self.buffer, dtype=np.int16).astype(np.float32) / 32768.0

        segments, info = self.model.transcribe(audio_np, language=None)
        text = " ".join([seg.text for seg in segments])

        return {
            "text": text.strip(),
            "language": info.language
        }

Neural Transcriber AI 🎙️🤖
---
Real-Time Multilingual Speech-to-Text Web Application (Offline, AI-Powered)

Neural Transcriber AI is a real-time, offline, multilingual speech recognition system built using FastAPI WebSockets and Faster-Whisper.
It captures microphone audio from the browser, streams it to a Python backend, automatically detects the spoken language, and displays live transcriptions in an AI-style dashboard interface.

This project demonstrates end-to-end AI system design, real-time streaming, and speech processing, similar to the core technology used in Zoom Live Captions and Google Meet Subtitles.
---
🚀 Features
---

🎤 Real-time microphone streaming (Browser → Python)
🌍 Automatic language detection (100+ languages)
⚡ Low-latency transcription using Faster-Whisper (CPU optimized)
🔌 WebSocket-based streaming (FastAPI)
🖥️ Local web dashboard UI
🔒 Fully offline, privacy-friendly
📄 Downloadable transcripts (future upgrade ready)
---
🧠 Tech Stack
---

Frontend

HTML, CSS (AI Dashboard UI)

JavaScript (MediaRecorder API, WebSockets)
---

Backend
---
Python

FastAPI

WebSockets

Faster-Whisper (CTranslate2, CPU optimized)

FFmpeg (audio decoding)
---

📁 Project Structure
---
```
NeuralTranscriber/
│
├── backend/
│   ├── main.py          # FastAPI WebSocket server
│   ├── transcriber.py  # Whisper inference engine
│   └── requirements.txt
│
├── frontend/
│   ├── index.html      # AI dashboard UI
│   ├── script.js       # Mic streaming logic
│   └── style.css       # Dark futuristic theme
│
├── .gitignore
└── README.md
```
---

⚙️ Installation
```
1. Clone Repository
git clone https://github.com/yourusername/neural-transcriber-ai.git
cd neural-transcriber-ai/backend


2. Install Dependencies
pip install -r requirements.txt
pip install faster-whisper

3. Install FFmpeg (Windows)

Download from: https://www.gyan.dev/ffmpeg/builds/

Add ffmpeg/bin to your system PATH.
```
---
```
▶️ Run the Application
Start Backend
uvicorn main:app --reload
```
---
Open Frontend

Open frontend/index.html in Chrome and click Start.

Speak in any language and watch live transcription appear.


from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from transcriber import Transcriber

app = FastAPI()
transcriber = Transcriber()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("Client connected")

    try:
        while True:
            audio_chunk = await websocket.receive_bytes()
            result = transcriber.transcribe(audio_chunk)

            await websocket.send_json({
                "text": result["text"],
                "language": result["language"]
            })

    except Exception as e:
        print("Disconnected:", e)

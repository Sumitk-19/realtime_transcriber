let socket;
let audioContext;
let processor;
let input;

async function start() {
  socket = new WebSocket("ws://127.0.0.1:8000/ws");

  const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  audioContext = new AudioContext({ sampleRate: 16000 });

  input = audioContext.createMediaStreamSource(stream);
  processor = audioContext.createScriptProcessor(4096, 1, 1);

  input.connect(processor);
  processor.connect(audioContext.destination);

  processor.onaudioprocess = (e) => {
    const floatData = e.inputBuffer.getChannelData(0);
    const pcm16 = floatTo16BitPCM(floatData);
    socket.send(pcm16);
  };
}

function stop() {
  processor.disconnect();
  input.disconnect();
  socket.close();
}

function floatTo16BitPCM(float32Array) {
  const buffer = new ArrayBuffer(float32Array.length * 2);
  const view = new DataView(buffer);
  let offset = 0;
  for (let i = 0; i < float32Array.length; i++, offset += 2) {
    let sample = Math.max(-1, Math.min(1, float32Array[i]));
    view.setInt16(offset, sample < 0 ? sample * 0x8000 : sample * 0x7fff, true);
  }
  return buffer;
}

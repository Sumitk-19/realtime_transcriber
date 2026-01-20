let socket;
let mediaRecorder;

function start() {
  socket = new WebSocket("ws://localhost:8000/ws");

  navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => {
    mediaRecorder = new MediaRecorder(stream, { mimeType: "audio/webm;codecs=opus" });

    mediaRecorder.ondataavailable = async (e) => {
      const buffer = await e.data.arrayBuffer();
      socket.send(buffer);
    };

    socket.onmessage = msg => {
      const data = JSON.parse(msg.data);
      document.getElementById("transcript").value += " " + data.text;
      document.getElementById("language").innerText = "Language: " + data.language;
    };

    mediaRecorder.start(1500); // 1.5 sec chunks
    document.getElementById("status").innerText = "Listening...";
  });
}


function stop() {
  mediaRecorder.stop();
  socket.close();
  document.getElementById("status").innerText = "Stopped";
}

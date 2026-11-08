import React, { useRef, useState } from "react";

export default function VoiceRecorder({ onRecognize }) {
  const [recording, setRecording] = useState(false);
  const mediaRecorderRef = useRef(null);
  const audioChunks = useRef([]);

  async function startRecording() {
    setRecording(true);
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorderRef.current = new window.MediaRecorder(stream);
    mediaRecorderRef.current.ondataavailable = (e) => audioChunks.current.push(e.data);
    mediaRecorderRef.current.onstop = async () => {
      const blob = new Blob(audioChunks.current, { type: "audio/wav" });
      audioChunks.current = [];
      if (onRecognize) {
        onRecognize(blob);
      }
    };
    mediaRecorderRef.current.start();
  }

  function stopRecording() {
    setRecording(false);
    mediaRecorderRef.current && mediaRecorderRef.current.stop();
  }

  return (
    <div style={{ margin: "1rem" }}>
      {recording ? (
        <button onClick={stopRecording}>Stop Recording</button>
      ) : (
        <button onClick={startRecording}>Start Recording</button>
      )}
    </div>
  );
}

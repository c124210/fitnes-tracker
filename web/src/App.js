import React, { useState } from 'react';
import VoiceRecorder from './components/VoiceRecorder';
import { recognizeSpeech } from './api';

function App() {
  const [recognizedText, setRecognizedText] = useState("");
  const [error, setError] = useState("");

  async function handleRecognize(blob) {
    setRecognizedText("Recognizing...");
    setError("");
    try {
      // Convert Blob to base64 or ArrayBuffer for backend
      const arrayBuffer = await blob.arrayBuffer();
      const audioData = Array.from(new Uint8Array(arrayBuffer));
      const response = await recognizeSpeech(audioData, 16000, 1);
      setRecognizedText(response?.recognized_text || "No speech recognized.");
    } catch (err) {
      setError("Recognition failed: " + err);
      setRecognizedText("");
    }
  }

  return (
    <div style={{ minHeight: "100vh", background: "#f5f6fa", display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center" }}>
      <h1>Fitness Tracker Voice</h1>
      <VoiceRecorder onRecognize={handleRecognize} />
      {recognizedText && <div style={{ margin: "1rem" }}><strong>Heard:</strong> {recognizedText}</div>}
      {error && <div style={{ color: 'red' }}>{error}</div>}
    </div>
  );
}

export default App;

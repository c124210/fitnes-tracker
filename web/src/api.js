// Example API client for FastAPI backend
export const API_BASE = 'http://localhost:8000'; // Adjust if hosting elsewhere

export async function recognizeSpeech(audioData, sampleRate, channels) {
  const resp = await fetch(`${API_BASE}/speech/recognize`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ audio_data: audioData, sample_rate: sampleRate, channels })
  });
  return await resp.json();
}
// Add more backend calls as needed

"""
Audio Ingestion & Ring Buffer Pipeline
Captures microphone and loopback audio streams in real-time.
"""
import numpy as np
import sounddevice as sd
import queue

class AudioCaptureManager:
    def __init__(self, sample_rate: int = 16000, chunk_duration_sec: float = 1.0):
        self.sample_rate = sample_rate
        self.chunk_size = int(sample_rate * chunk_duration_sec)
        self.audio_queue = queue.Queue()
        self.is_streaming = False

    def _audio_callback(self, indata, frames, time_info, status):
        mono_data = np.mean(indata, axis=1) if indata.ndim > 1 else indata.flatten()
        self.audio_queue.put(mono_data.copy())

    def start_stream(self):
        self.is_streaming = True
        self.stream = sd.InputStream(
            samplerate=self.sample_rate,
            channels=1,
            dtype='float32',
            blocksize=self.chunk_size,
            callback=self._audio_callback
        )
        self.stream.start()

    def stop_stream(self):
        self.is_streaming = False
        if hasattr(self, 'stream'):
            self.stream.stop()
            self.stream.close()

    def get_audio_chunk(self):
        try:
            return self.audio_queue.get(timeout=0.5)
        except queue.Empty:
            return None

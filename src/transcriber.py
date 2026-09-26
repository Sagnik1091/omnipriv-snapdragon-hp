"""Proposal-stage transcription interface.

Real ONNX/QNN inference is not implemented in this reference repository.
"""
import numpy as np

class HexagonTranscriber:
    def __init__(self, model_path: str = "models/speech_model.onnx"):
        self.model_path = model_path
        print("[Transcriber] SIMULATION MODE — no AI model or QNN provider is loaded.")

    def transcribe_chunk(self, audio_data: np.ndarray) -> str:
        if audio_data is None or len(audio_data) == 0:
            return ""
        return "[SIMULATED TRANSCRIPT] Replace this stub with validated local ASR inference."

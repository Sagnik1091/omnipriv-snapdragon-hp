"""Proposal-stage meeting-minutes formatter.

Real generative-model inference is not implemented in this reference repository.
"""
from typing import List, Dict

class HexagonSummarizer:
    def __init__(self, model_path: str = "models/instruction_model.onnx"):
        self.model_path = model_path
        print("[Summarizer] SIMULATION MODE — no language model or QNN provider is loaded.")

    def generate_minutes(self, transcripts: List[Dict]) -> str:
        combined = "\n".join(
            f"[{t['timestamp']}] {t['speaker']}: {t['content']}" for t in transcripts
        )
        return f"""# Simulated Meeting Minutes

> Reference output only. No AI model generated this summary.

## Transcript context
{combined}

## Planned production output
- Decisions linked to transcript segments
- Action items with owner and due date where stated
- Unresolved questions and follow-ups
"""

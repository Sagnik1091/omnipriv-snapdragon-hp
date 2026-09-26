"""Print the model-provisioning checklist.

This script intentionally does not create fake .onnx files. Qualcomm AI Hub model
selection, licensing, export, and target-device compatibility must be verified
before model artifacts are provisioned.
"""
from pathlib import Path

CANDIDATES = [
    ("Speech recognition", "Select a Qualcomm AI Hub speech model supported on the target chipset."),
    ("Embeddings", "Select a compact sentence-embedding model and validate the intended runtime."),
    ("Synthesis", "Select a compact instruction model that fits the memory and license constraints."),
]

def main():
    model_dir = Path(__file__).resolve().parents[1] / "models"
    print("OmniPriv model-provisioning checklist")
    print(f"Planned local model directory: {model_dir}")
    for name, requirement in CANDIDATES:
        print(f"- {name}: {requirement}")
    print("\nNo model files were downloaded or generated.")
    print("Record model URL, version, license, checksum, compile target, and provider logs before use.")

if __name__ == "__main__":
    main()

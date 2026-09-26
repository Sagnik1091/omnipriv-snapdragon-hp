# OmniPriv

**Proposal-stage reference prototype for the Snapdragon AI Lab Build & Present Challenge**

OmniPriv is an offline-first meeting intelligence concept designed for Snapdragon-powered HP PCs. The intended product captures meeting audio, produces local transcripts, retrieves cited discussion segments, and creates structured minutes without requiring a cloud service during meetings.

> **Current status:** this repository contains a runnable Python simulation of the proposed workflow. It does **not** yet perform real Whisper/Llama inference, semantic vector search, QNN acceleration, WinUI packaging, or hardware benchmarking. Planned functionality and performance targets are documented separately from completed work.

## Why OmniPriv

- **Privacy and governance:** local processing can reduce exposure to remote data handling.
- **Offline resilience:** meeting assistance can remain available when connectivity is limited.
- **Device efficiency:** Snapdragon X platforms provide a Hexagon NPU intended for efficient on-device AI workloads.
- **Verifiability:** the proposed product exposes runtime/provider diagnostics rather than relying on unverified acceleration claims.

## Intended workflow

```text
Microphone / system audio
        ↓
Local buffering and preprocessing
        ↓
Speech model compiled for a validated local runtime
        ↓
Timestamped transcript + local embedding index
        ↓
Grounded minutes, action items, and transcript-cited Q&A
```

## What works today

- A runnable, deterministic pipeline simulation.
- Local SQLite transcript insertion and retrieval.
- A meeting-minutes output format.
- Unit tests for storage and simulated summary formatting.

## What is not implemented yet

- Real microphone-to-ASR integration in the main pipeline.
- Real ONNX Runtime or QNN execution.
- Downloaded or compiled Qualcomm AI Hub model artifacts.
- Embedding generation, HNSW, or vector similarity search.
- Generative-model inference.
- WinUI 3 interface or ARM64 MSIX installer.
- Measured Snapdragon/HP latency, memory, power, or battery results.

## Run the reference simulation

```bash
git clone https://github.com/Sagnik1091/omnipriv-snapdragon-hp.git
cd omnipriv-snapdragon-hp
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python src/main.py
python -m unittest discover -s tests -v
```

The console output is explicitly labeled as simulated and should not be interpreted as hardware or AI-model validation.

## Proposed target stack

| Stage | Candidate technology | Evidence required before claiming completion |
|---|---|---|
| Transcription | Qualcomm AI Hub speech model; ONNX/QNN where supported | Provider allocation, latency, accuracy sample |
| Retrieval | Compact embedding model plus local vector index | Embedding latency and retrieval relevance |
| Synthesis | Compact local instruction model | Runtime logs, tokens/sec, memory, grounded-output review |
| Windows delivery | ARM64 Windows app and MSIX | Repeatable install, accessibility and offline tests |

Candidate model selection is intentionally not locked until licensing, input/output compatibility, and support for the target Snapdragon chipset are verified.

## Engineering targets — not benchmark results

- Transcript update latency: **≤1 second**.
- Meeting-time processing: **no required outbound connection**.
- Working memory: **below 4 GB**, subject to final model selection.
- CPU package-power reduction: **≥30% versus a documented CPU reference path**.
- Grounding: key summary and Q&A claims link to transcript excerpts.

See [`docs/VALIDATION_PLAN.md`](docs/VALIDATION_PLAN.md) for measurement requirements.

## Roadmap

1. Connect a recorded WAV file to real local transcription.
2. Compile/profile one supported model and capture QNN/provider evidence.
3. Add embeddings, local similarity search, and cited retrieval.
4. Add grounded minutes, action items, and export.
5. Package and test the validated workflow on Windows on ARM.

## Responsible disclosure of status

The current code is a reference simulation, not a production application. No claim of NPU execution, zero CPU fallback, measured latency, measured power reduction, battery endurance, or model throughput is made until reproducible evidence is published.

## License

Application code is released under the MIT License. Third-party models and runtimes remain subject to their own licenses and distribution requirements.

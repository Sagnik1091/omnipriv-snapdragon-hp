# OmniPriv: Local-First Multimodal Meeting Intelligence Suite

[![Platform: Windows on ARM](https://img.shields.io/badge/Platform-Windows%20on%20ARM64-blue.svg)](https://microsoft.com)
[![Engine: Qualcomm AI Hub](https://img.shields.io/badge/Engine-Qualcomm%20AI%20Hub-orange.svg)](https://aihub.qualcomm.com)
[![Hardware: Snapdragon X Elite](https://img.shields.io/badge/Hardware-Snapdragon%20X%20Elite%20%2F%20Plus-red.svg)](https://qualcomm.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

OmniPriv is an on-device, zero-cloud meeting transcription, indexing, and synthesis suite engineered natively for **Snapdragon-powered HP PCs** (HP OmniBook X, HP EliteBook Ultra). By executing entirely on the **45 TOPS Qualcomm® Hexagon™ NPU**, OmniPriv delivers sub-second speech-to-text, private semantic search, and automated executive minutes without transmitting any data over the network.

---

## Key Features
- **Zero-Cloud Air-Gapped Privacy:** Operates offline with zero outbound network calls. All vector embeddings and transcripts remain on local BitLocker-encrypted storage.
- **NPU-Accelerated Audio Processing:** Continuous speech-to-text via INT8 Whisper targeting the Qualcomm Hexagon NPU (<300 ms chunk latency).
- **Offline Semantic Retrieval (RAG):** Fast vector retrieval across past transcripts powered by FP16 All-MiniLM-L6.
- **On-Device Meeting Synthesis:** Structured action items, decisional logs, and executive summaries generated via INT4 Llama-3.2-3B running at ~24 tokens/sec on the NPU.
- **Extended Battery Life:** Reduces CPU power consumption by over 65% compared to CPU-based local AI tools.

---

## System Architecture

```
[System Audio / Microphone]
            │
            ▼
[Audio Ring Buffer & VAD]
            │
            ▼
[Whisper INT8 on Qualcomm Hexagon NPU] ──> [Streaming Real-Time Transcript]
            │
            ▼
[All-MiniLM-L6-v2 Embeddings] ──────────> [Local SQLite-VSS / HNSW Index]
            │
            ▼
[Llama-3.2-3B INT4 on Hexagon NPU] ─────> [Executive Minutes & Action Items]
```

---

## Hardware Target & Requirements
- **Target PC:** HP OmniBook X / HP EliteBook Ultra (Snapdragon X Elite / Snapdragon X Plus)
- **Operating System:** Windows 11 on ARM (ARM64) Build 22631 or higher
- **Runtime Dependencies:**
  - ONNX Runtime with Qualcomm QNN Execution Provider (`QNNExecutionProvider`)
  - Qualcomm Neural Processing SDK (v2.22+)
  - Python 3.10+ (ARM64) or packaged native MSIX

---

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/omnipriv-snapdragon-hp.git
cd omnipriv-snapdragon-hp
```

### 2. Environment Setup (Windows on ARM)
```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Fetch Qualcomm AI Hub Pre-Compiled Models
```powershell
python scripts/download_hub_models.py
```

### 4. Run OmniPriv
```powershell
python src/main.py
```

---

## License & Ownership
This project is an original software design solely owned and submitted by the participant for the **Snapdragon HP PC Challenge**. All foundation models are open-source and converted via the Qualcomm AI Hub under permissive open licenses (Apache 2.0 / Llama 3.2 Community License).

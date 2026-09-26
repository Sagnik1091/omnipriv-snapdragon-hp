# Implementation status

| Capability | Status | Evidence |
|---|---|---|
| Pipeline simulation | Implemented | `src/main.py` |
| SQLite transcript persistence | Implemented | `src/vector_store.py` and unit test |
| Audio capture helper | Partial / not connected | `src/audio_capture.py` |
| Real ASR inference | Planned | Current transcriber is a deterministic stub |
| Embeddings and vector search | Planned | Current store is ordinary SQLite |
| Local LLM summary generation | Planned | Current summarizer formats a template |
| QNN / Hexagon NPU execution | Planned | No inference session or provider logs yet |
| WinUI 3 application | Planned | No Windows UI project yet |
| MSIX packaging | Planned | No installer project yet |
| Hardware benchmark | Planned | No device measurements published |

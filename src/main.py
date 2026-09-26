"""OmniPriv proposal-stage reference simulation."""
from transcriber import HexagonTranscriber
from vector_store import LocalVectorStore
from summarizer import HexagonSummarizer

def main():
    print("=" * 68)
    print("OmniPriv — proposal-stage reference simulation")
    print("No real AI inference, QNN execution, or hardware benchmark occurs.")
    print("=" * 68)

    HexagonTranscriber()
    store = LocalVectorStore()
    summarizer = HexagonSummarizer()

    simulated_events = [
        ("10:00:15", "Lead", "We will validate local transcription on the target HP device."),
        ("10:00:45", "Product", "Performance figures must be reported only after measurement."),
        ("10:01:20", "Security", "Offline behavior will be verified with network monitoring."),
    ]
    for timestamp, speaker, text in simulated_events:
        store.insert_transcript(timestamp, speaker, text)
        print(f"[SIMULATED INPUT] [{timestamp}] {speaker}: {text}")

    print(summarizer.generate_minutes(store.query_recent(limit=10)))
    print("Simulation completed. See docs/IMPLEMENTATION_STATUS.md for limitations.")

if __name__ == "__main__":
    main()

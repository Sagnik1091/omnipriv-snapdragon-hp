"""
OmniPriv - Main Execution Entry Point
"""
import time
from transcriber import HexagonTranscriber
from vector_store import LocalVectorStore
from summarizer import HexagonSummarizer

def main():
    print("=" * 65)
    print(" OmniPriv: Meeting Intelligence for Snapdragon-Powered HP PCs")
    print(" Target: Qualcomm Hexagon NPU (45 TOPS) | Windows 11 on ARM64")
    print("=" * 65)

    transcriber = HexagonTranscriber()
    store = LocalVectorStore()
    summarizer = HexagonSummarizer()

    print("\n[1/3] Simulating live meeting audio ingestion...")
    mock_events = [
        ("10:00:15", "Lead Engineer", "We have verified the Whisper INT8 model on Snapdragon X Elite."),
        ("10:00:45", "Product Manager", "Battery life remains above 18 hours with continuous transcription."),
        ("10:01:20", "Security Architect", "Network isolation confirmed. Zero outbound telemetry detected.")
    ]

    for ts, speaker, text in mock_events:
        store.insert_transcript(ts, speaker, text)
        print(f"  [Transcribed] [{ts}] {speaker}: {text}")
        time.sleep(0.3)

    print("\n[2/3] Retrieving indexed meeting context from local database...")
    recent_context = store.query_recent(limit=10)

    print("\n[3/3] Generating executive summary on Qualcomm Hexagon NPU...")
    summary = summarizer.generate_minutes(recent_context)
    
    print("\n" + "=" * 65)
    print(summary)
    print("=" * 65)
    print("\nOmniPriv pipeline completed successfully with 100% on-device execution.")

if __name__ == "__main__":
    main()

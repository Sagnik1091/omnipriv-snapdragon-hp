"""Pipeline Unit Tests."""
import unittest
from src.vector_store import LocalVectorStore
from src.summarizer import HexagonSummarizer

class TestOmniPrivPipeline(unittest.TestCase):
    def setUp(self):
        self.store = LocalVectorStore()
        self.summarizer = HexagonSummarizer()

    def test_database_insert_and_retrieval(self):
        self.store.insert_transcript("10:00:00", "Alice", "Testing Snapdragon HP PC integration.")
        results = self.store.query_recent(limit=1)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["speaker"], "Alice")

    def test_summary_generation(self):
        mock_data = [{"timestamp": "10:00", "speaker": "Bob", "content": "Action item created."}]
        summary = self.summarizer.generate_minutes(mock_data)
        self.assertIn("Executive Meeting Minutes", summary)

if __name__ == "__main__":
    unittest.main()

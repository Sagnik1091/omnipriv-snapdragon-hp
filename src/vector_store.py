"""
Local Semantic Storage & Vector Indexing Module
"""
import sqlite3
from typing import List, Dict

class LocalVectorStore:
    def __init__(self, db_path: str = ":memory:"):
        self.conn = sqlite3.connect(db_path)
        self._create_schema()

    def _create_schema(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS transcript_chunks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    speaker TEXT,
                    content TEXT
                )
            """)

    def insert_transcript(self, timestamp: str, speaker: str, content: str):
        with self.conn:
            self.conn.execute(
                "INSERT INTO transcript_chunks (timestamp, speaker, content) VALUES (?, ?, ?)",
                (timestamp, speaker, content)
            )

    def query_recent(self, limit: int = 10) -> List[Dict]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT timestamp, speaker, content FROM transcript_chunks ORDER BY id DESC LIMIT ?", (limit,))
        rows = cursor.fetchall()
        return [{"timestamp": r[0], "speaker": r[1], "content": r[2]} for r in reversed(rows)]

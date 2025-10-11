import sqlite3
from app.config import DATABASE_PATH


def init_db():
    with sqlite3.connect(DATABASE_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS history(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symptoms TEXT,
                result TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.commit()


def log_query(symptoms: str, result: str):
    with sqlite3.connect(DATABASE_PATH) as conn:
        conn.execute(
            "INSERT INTO history (symptoms, result) VALUES (?, ?)", (symptoms, result)
        )
        conn.commit()


def fetch_history(limit:int=10):
    with sqlite3.connect(DATABASE_PATH) as conn:
        rows = conn.execute(
            "SELECT symptoms, result, timestamp from history ORDER BY timestamp DESC limit ?", (limit,)
        ).fetchall()
        return [{"symptoms":r[0], "result":r[1], "timestamp":r[2]} for r in rows]
    
init_db()
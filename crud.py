import sqlite3
from typing import List, Optional

DATABASE = "magic8ball.db"

def get_connection():
    return sqlite3.connect(DATABASE)


def get_all_answers() -> List[dict]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, answer FROM answers")
    rows = cur.fetchall()
    conn.close()
    return [{"id": row[0], "answer": row[1]} for row in rows]


def get_random_answer() -> Optional[str]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT answer FROM answers ORDER BY RANDOM() LIMIT 1")
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None


def add_answer(text: str) -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO answers (answer) VALUES (?)", (text,))
    conn.commit()
    conn.close()


def update_answer(id: int, text: str) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE answers SET answer = ? WHERE id = ?", (text, id))
    updated = cur.rowcount
    conn.commit()
    conn.close()
    return updated > 0


def delete_answer(id: int) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM answers WHERE id = ?", (id,))
    deleted = cur.rowcount
    conn.commit()
    conn.close()
    return deleted > 0
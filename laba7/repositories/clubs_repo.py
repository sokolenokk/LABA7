import sqlite3
from typing import Optional
from laba7.db import get_connection


def add_club(name: str, city: str) -> int:
    with get_connection() as conn:
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO clubs (name, city) VALUES (?, ?)",
                (name, city)
            )
            conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            cursor.execute("SELECT id FROM clubs WHERE name = ?", (name,))
            row = cursor.fetchone()
            return int(row["id"])


def get_club_id_by_name(name: str) -> Optional[int]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM clubs WHERE name = ?", (name,))
        row = cursor.fetchone()
        return int(row["id"]) if row else None

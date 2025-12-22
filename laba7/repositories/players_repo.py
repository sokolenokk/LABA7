from typing import List, Dict, Any
from laba7.db import get_connection


def add_player(full_name: str, position: str, age: int, club_id: int) -> int:
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO players (full_name, position, age, club_id) VALUES (?, ?, ?, ?)",
            (full_name, position, age, club_id)
        )

        conn.commit()
        return cursor.lastrowid


def find_players_by_position(position: str) -> List[Dict[str, Any]]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, full_name, position, age, club_id FROM players WHERE position = ?",
            (position,)
        )
        rows = cursor.fetchall()
        return [dict(r) for r in rows]


def find_players_younger_than(max_age: int) -> List[Dict[str, Any]]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, full_name, position, age, club_id FROM players WHERE age < ?",
            (max_age,)
        )
        rows = cursor.fetchall()
        return [dict(r) for r in rows]

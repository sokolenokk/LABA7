from typing import List, Dict, Any, Optional
from laba7.db import get_connection


def add_player(full_name: str, position: str, age: int, club_id: int) -> int:
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            "INSERT OR IGNORE INTO players (full_name, position, age, club_id) VALUES (?, ?, ?, ?)",
            (full_name, position, age, club_id)
        )
        conn.commit()

        cursor.execute(
            "SELECT id FROM players WHERE full_name = ? AND club_id = ?",
            (full_name, club_id)
        )
        row = cursor.fetchone()
        return int(row["id"])


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


def get_players_with_clubs(club_name: Optional[str] = None):
    with get_connection() as conn:
        cursor = conn.cursor()

        sql = """
            SELECT
                p.id AS player_id,
                p.full_name,
                p.position,
                p.age,
                c.id AS club_id,
                c.name AS club_name,
                c.city AS club_city
            FROM players p
            JOIN clubs c ON p.club_id = c.id
        """

        params = ()
        if club_name is not None:
            sql += "WHERE c.name = ?"
            params = (club_name,)

        cursor.execute(sql, params)
        rows = cursor.fetchall()
        return [dict(r) for r in rows]

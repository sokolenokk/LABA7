from laba7.db import get_connection


def test_tables_exist(db):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='clubs'")
        assert cur.fetchone() is not None

        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='players'")
        assert cur.fetchone() is not None


def test_indices_exist(db):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='index'")
        index_names = {row["name"] for row in cur.fetchall()}

        assert "idx_players_unique" in index_names

        assert "idx_players_position" in index_names
        assert "idx_players_age" in index_names

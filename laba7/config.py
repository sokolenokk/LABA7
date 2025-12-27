import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def get_db_path() -> Path:
    env_path = os.getenv("LABA7_DB_PATH")
    if env_path:
        return Path(env_path)
    return BASE_DIR / "data" / "football.db"

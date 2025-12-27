import pytest
from laba7.shema import create_tables


@pytest.fixture()
def db(tmp_path, monkeypatch):
    test_db_path = tmp_path / "test.db"
    monkeypatch.setenv("LABA7_DB_PATH", str(test_db_path))

    create_tables()
    return test_db_path

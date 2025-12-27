from laba7.repositories.clubs_repo import add_club
from laba7.repositories.players_repo import add_player, get_players_with_clubs


def test_join_returns_club_fields(db):
    barca_id = add_club("FC Barcelona", "Barcelona")
    add_player("Pedri", "CM", 23, barca_id)

    rows = get_players_with_clubs()
    assert len(rows) == 1

    row = rows[0]
    assert row["full_name"] == "Pedri"
    assert row["club_name"] == "FC Barcelona"
    assert row["club_city"] == "Barcelona"


def test_join_filter_by_club(db):
    barca_id = add_club("FC Barcelona", "Barcelona")
    mu_id = add_club("Manchester United", "Manchester")

    add_player("Pedri", "CM", 23, barca_id)
    add_player("Bruno Fernandes", "AM", 31, mu_id)

    barca_rows = get_players_with_clubs("FC Barcelona")
    assert len(barca_rows) == 1
    assert barca_rows[0]["full_name"] == "Pedri"

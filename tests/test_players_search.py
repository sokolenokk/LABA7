from laba7.repositories.clubs_repo import add_club
from laba7.repositories.players_repo import add_player, find_players_by_position, find_players_younger_than


def test_find_players_by_position(db):
    barca_id = add_club("FC Barcelona", "Barcelona")
    mu_id = add_club("Manchester United", "Manchester")

    add_player("Pedri", "CM", 23, barca_id)
    add_player("Kobbie Mainoo", "CM", 20, mu_id)
    add_player("Bruno Fernandes", "AM", 31, mu_id)

    cm_players = find_players_by_position("CM")
    names = {p["full_name"] for p in cm_players}

    assert "Pedri" in names
    assert "Kobbie Mainoo" in names
    assert "Bruno Fernandes" not in names


def test_find_players_younger_than(db):
    barca_id = add_club("FC Barcelona", "Barcelona")

    add_player("Pedri", "CM", 23, barca_id)
    add_player("Lewandowski", "ST", 36, barca_id)

    young = find_players_younger_than(25)
    names = {p["full_name"] for p in young}

    assert "Pedri" in names
    assert "Lewandowski" not in names

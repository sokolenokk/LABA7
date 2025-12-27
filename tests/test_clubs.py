from laba7.repositories.clubs_repo import add_club, get_club_id_by_name


def test_add_club_and_get_id(db):
    club_id = add_club("FC Barcelona", "Barcelona")
    assert isinstance(club_id, int)
    assert club_id > 0

    fetched_id = get_club_id_by_name("FC Barcelona")
    assert fetched_id == club_id


def test_add_club_twice_returns_same_id(db):
    id1 = add_club("Manchester United", "Manchester")
    id2 = add_club("Manchester United", "Manchester")
    assert id1 == id2

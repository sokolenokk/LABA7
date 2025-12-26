from laba7.shema import create_tables
from laba7.repositories.clubs_repo import add_club, get_club_id_by_name
from laba7.repositories.players_repo import add_player, \
    find_players_by_position, find_players_younger_than, \
    get_players_with_clubs


def seed_demo_data() -> None:
    barca_id = add_club("FC Barcelona", "Barcelona")
    mu_id = add_club("Manchester United", "Manchester")

    add_player("Robert Lewandowski", "ST", 36, barca_id)
    add_player("Pedri", "CM", 23, barca_id)
    add_player("Bruno Fernandes", "AM", 31, mu_id)
    add_player("Kobbie Mainoo", "CM", 20, mu_id)


def main() -> None:
    create_tables()
    seed_demo_data()

    print("Поиск игроков по позиции параметризованный SELECT")
    cm_players = find_players_by_position("CM")
    for p in cm_players:
        print(p)

    print("Поиск игроков младше заданного возраста параметризованный SELECT")
    young_players = find_players_younger_than(25)
    for p in young_players:
        print(p)

    print("Получить id клуба по имени параметризованный SELECT")
    club_id = get_club_id_by_name("FC Barcelona")
    print("id Барсы: ", club_id)
    print()
    print()


    print("JOIN: игркоки + инфа о клубе")
    joined = get_players_with_clubs()
    for row in joined:
        print(row)

    print("JOIN: игркоки Барсы:")
    joined_barca = get_players_with_clubs("FC Barcelona")
    for row in joined_barca:
        print(row)


if __name__ == "__main__":
    main()

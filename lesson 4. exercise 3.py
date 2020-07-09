def attack_and_print_health(attacker, defender):
    print(attack(attacker, defender))
    print(get_person_health(attacker))
    print(get_person_health(defender))
    print()


def attack(attacker, defender):
    damage = attacker['damage']
    defender['health'] -= damage
    info = f"{attacker['name']} deals damage to {defender['name']}:"
    "{damage} points"
    return info


def print_start_info(*persons):
    for person in persons:
        print(get_person_info(person))
    print()


def get_person_info(person):
    info = f"{person['name']}: \n\tdamage = {person['damage']},"
    "\n\thealth = {person['health']}"
    return info


def get_person_health(person):
    info = f"{person['name']}`s health = {person['health']}"
    return info


def create_person(name):
    person = {
        'name': name,
        'health': 100,
        'damage': 50
    }
    return person


def main():
    print('test check...\n')

    player = create_person('Player')
    enemy = create_person('Enemy')

    print_start_info(player, enemy)

    attack_and_print_health(attacker=enemy, defender=player)
    attack_and_print_health(attacker=player, defender=enemy)
    attack_and_print_health(attacker=enemy, defender=player)


if __name__ == '__main__':
    main()

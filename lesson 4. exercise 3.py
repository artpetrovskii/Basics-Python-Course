def attack(person1, person2):
    nice_shot = random.randint(1, 7)
    if nice_shot >= 3:
        person2['health'] -= person1['damage']
        return person1, person2['health']
    else:
        person1['health'] -= person2['damage']
        return person1['health'], person2
    my_wanzer = {
        'health': 100, 'damage': 30, 'name': input('Введите имя Ванзера')
    }
    OCU = {
        'health': 140, 'damage': 20, 'name': input('Введите противника Объединенного Океанического Союза')
    }
    turn = 1
    while my_wanzer['health'] <= 0 and OCU['health'] <= 0:
        if turn % 2 != 0:
            my_wanzer, OCU = attack(my_wanzer, OCU)
        else:
            OCU, my_wanzer = attack(OCU, my_wanzer)
            turn += 1
    else:
        if my_wanzer['health'] > 0:
            print(f"{my_wanzer['name']}победил. Попробуй еще раз")
        else:
            print(f"{OCU['name']} победил. Попробуй еще раз")

import random

def new_damage(damage, armor):
    return damage / armor

def attack(person1, person2):
    nice_shot = random.randint(1, 7)
    if nice_shot >= 3:
        person2['health'] -= new_damage(person1['damage'], person2['armor'])
        return person1, person2['health']
    else:
        person1['health'] -= new_damage(person2['damage'], person1['armor'])
        return person1['health'], person2

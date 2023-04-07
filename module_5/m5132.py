import random


class Warrior:
    def __init__(self):
        self.health = 100
        self.stamina = 100
        self.armor = 100

        self.hit = False

    def attack(self):
        self.stamina -= 10

    def defense(self, other):
        if other.hit:
            

    def battle(self, other):
        if random.randint(0, 1) == 1:
            other.health -= 20
            other.hit = False
            self.hit = True
        else:
            self.health -= 20
            other.hit = True
            self.hit = False


Unit1 = Warrior()
Unit2 = Warrior()

while (Unit1.health > 0) & (Unit2.health > 0):
    Unit1.battle(Unit2)
    if Unit1.hit:
        print(f'Ударил воин 1, у воина 2 осталось здоровья {Unit2.health}')
    else:
        print(f'Ударил воин 2, у воина 1 осталось здоровья {Unit1.health}')

if Unit1.health <= 0:
    print('Победил воин 2')
else:
    print('Победил воин 1')

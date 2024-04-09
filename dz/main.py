from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")


class Bow(Weapon):
    def attack(self):
        print("Боец наносит удар из лука.")


class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            self.weapon.attack()
        else:
            print("Боец атакует рукопашным боем.")


class Monster:
    def __init__(self, name):
        self.name = name

    def attack(self):
        print("Монстр атакует бойца.")


fighter = Fighter("Боец")
monster = Monster("Монстр")

sword = Sword()
bow = Bow()

fighter.change_weapon(sword)
fighter.attack()
monster.attack()

print("Боец выбирает лук.")
fighter.change_weapon(bow)
fighter.attack()
monster.attack()

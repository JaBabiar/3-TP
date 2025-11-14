### Master Class
class Champion:
    def __init__(self, summonner_name, health, mana):
        self.name = summonner_name
        self.health = health
        self.mana = mana
        self.is_alive = True

    def take_damage(self, amount):
        if not self.is_alive:
            print(f"{self.name} is dead")
            return
        self.health -= amount
        print(f"{self.name} takes {amount}, Health: {self.health}")

        if self.health <= 0:
            self.health = 0
            self.is_alive = False
            print(f"{self.name} slain")

class Teemo(Champion):
    def __init__(self, summonner_name, health, mana,stack):
        super().__init__(summonner_name, health, mana)

        # Teemo
        self.shroom = stack

    def plant_shroom(self):
        if self.shroom > 0:
            print()
            self.shroom -= 1
        else:
            print()
            return

class Bard(Champion):
    def __init__(self, summonner_name, health, mana,stack):
        super().__init__(summonner_name, health, mana)

        # Teemo
        self.stack = stack

    def plant_heal(self):
        if self.stack > 0:
            print()
            self.stack -= 1
        else:
            print()
            return

teemo_player = Teemo("XxX_Teemo67_XxX", 580, 320,3)
teemo_player.plant_shroom()
bard_player = Bard("XxX_BarDo67_XxX", 580, 320,3)
bard_player.plant_heal()
bard_player.take_damage(590)

print(bard_player.is_alive)
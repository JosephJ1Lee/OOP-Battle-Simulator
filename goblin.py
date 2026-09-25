import random
from enemy import Enemy

class Goblin(Enemy):
    def __init__(self, name):
        super().__init__(name, health = 100, attackPower = 8)
        self.gold = 0
        
    def steal(self, hero):
        """Steal gold from good guys."""
        self.gold += hero.gold
        hero.gold = 0
        print("GIT REKT NOOB")
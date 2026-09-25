from enemy import Enemy

class Boss(Enemy):
    """A stronger enemy with a powered-up attack."""
    def __init__(self, name):
        super().__init__(name, health=200, attackPower=40)

    def introduce(self, name):
        print("WATASHIA GOBLIN BOSSU")
        
    def attack(self):
        damage = super().attack()
        bonus_damage = 5
        print(f"{self.name} unleashes a crushing blow!")
        return damage + bonus_damage
    
    def take_damage(self, damage):
        print("DIS IS DA SPECIAL MESSAGE")
        super().take_damage(damage)
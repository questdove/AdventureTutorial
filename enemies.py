class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
 
    def is_alive(self):
        return self.hp > 0

class CorpCop(Enemy):
    def __init__(self):
        super().__init__(name="CorpCop", hp=10, damage=2)
 
 
class Assassin(Enemy):
    def __init__(self):
        super().__init__(name="Assassin", hp=30, damage=15)
    

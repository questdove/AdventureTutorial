class Item():
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
    
class Money(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name = "Credits", description = "A digital currency accepted everywhere.".format(str(self.amt)), value = self.amt)

class Clue(Item):
    def _init__(self, cluepoints):
        self.cluepoints = cluepoints
        super().__init__(name = "Clue", description = "Its a fucking clue!".format(str(self.cluepoints)), value = 0)


"""Weapons"""

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
 
 
class Taser(Weapon):
    def __init__(self):
        super().__init__(name="Taser",
                         description="A small personal safety device that delivers a ZAP!",
                         value=0,
                         damage=5)

class Knife(Weapon):
    def __init__(self):
        super().__init__(name="Knife",
                         description="A small retractable knife. Somewhat dangerous in the right hands.",value=10,damage=10)

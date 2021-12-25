
class Hero():
    def __init__(self,name,power,health,*args,**kwargs):
        self.name = name
        self.power = power
        self.health = health

    def darbe(self,power):
        self.health -= power

    def vurma(self):
        return self.power


class Spiderman(Hero):
    def __init__(self):
        super().__init__("Spiderman", 20, 400)

class IronMan(Hero):
    def __init__(self):
        super().__init__("IronMan", 25, 600)

class Hulk(Hero):
    def __init__(self):
        super().__init__("Hulk", 30, 700)

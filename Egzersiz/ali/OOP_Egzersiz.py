class Hero:
    def __init__(self,name,strength,health,*args,**kwargs):
        self.name = name
        self.strength = strength
        self.health = health

    def damage1(self,strength):
        self.health -= strength//2
    
    def damage2(self,strength):
        self.health -= strength//3

    def damage3(self,strength):
        self.health -= strength

    def damage(self,strength):
        liste = [self.strength]
        self.health -= strength

    def shot1(self):
        return self.strength//2

    def shot2(self):
        return self.strength//3

    def shot3(self):
        return self.strength

    def shot(self):
        liste = [self.shot1,self.shot2,self.shot3]
        return rnd.choice(liste)()
    @property
    def status(self):
        return f"{self.name} - Sağlık:{self.health}"

    def __del__(self):
        print("R.I.P", self.name)

class Deadpool(Hero):
    def __init__(self):
        super().__init__("Deadpool", 25, 500)

class CaptainAmerica(Hero):
    def __init__(self):
        super().__init__("CaptainAmerica", 33, 333)

class IronMan(Hero):
    def __init__(self):
        super().__init__("IronMan", 22, 666)

class BattalGazi(Hero):
    def __init__(self):
        super().__init__("BattalGazi", 100, 1000)

import random as rnd
heroList = [Deadpool,CaptainAmerica,IronMan,BattalGazi]
p1 = rnd.choice(heroList)()
p2 = rnd.choice(heroList)()

import time

while p1.health > 0 and p2.health >0:
    time.sleep(0.5)
    p1.damage(p2.shot())
    p2.damage(p1.shot())
    print(p1.status)
    print(p2.status)
else:
    if p1.health > p2.health:
        print(p1.name,"kazandı")
    elif p1.health < p2.health:
        print(p2.name,"kazandı")
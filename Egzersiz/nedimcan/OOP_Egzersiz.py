"""
1- kahramanların tanımlanabileceği bir yapı oluşturun
2- parametre olarak adi,guc,saglik
3- darbe,vurma adında iki fonksiyon ile secilen karakterin güçleri 
4- ölçüsünde diğer karakterin sağlığında eksiltmesini sağlayalım
5- istenildiğinde tek bir fonksiyon ile karakterin durumunu görebilelim
"""
import random


class Hero:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health

    def impact(self):
        hit = random.randrange(0, self.power)

        if hit != 0:
            health = self.health - hit
            return f"Given hit: {hit} | Health: {health}"
        else:
            return "Hit missed!"

    def status(self, name):
        return f"Status of {self.name}: {self.health}"


a = Hero("A", 10, 100)
b = Hero("B", 20, 100)

print(a.status("A"))
print(b.status("B"))
print(b.impact())
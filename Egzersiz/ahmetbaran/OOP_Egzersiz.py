"""
kahramanların tanımlanabileceği bir yapı oluşturun
parametre olarak adi,guc,saglik
darbe,vurma adında iki fonksiyon ile secilen karakterin güçleri 
ölçüsünde diğer karakterin sağlığında eksiltmesini sağlayalım
istenildiğinde tek bir fonksiyon ile karakterin durumunu görebilelim
"""


class Hero:
    def __init__(self, name, power, hp, *args, **kwargs):
        self.name = name
        self.power = power
        self.hp = hp

    def attack(self, enemy):
        enemy.hp = enemy.hp - self.power

    def heroInfo(self):
        print(f'{self.name} - {self.hp} - {self.power}')

thor = Hero('Thor', 2000, 2000)
wolverine = Hero('Wolverine', 50, 9999999)
thor.heroInfo()
wolverine.heroInfo()



thor.attack(wolverine)
wolverine.attack(thor)

thor.heroInfo()
wolverine.heroInfo()

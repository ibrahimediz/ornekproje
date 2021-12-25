"""
kahramanların tanımlanabileceği bir yapı oluşturun
parametre olarak adi,guc,saglik
darbe,vurma adında iki fonksiyon ile secilen karakterin güçleri 
ölçüsünde diğer karakterin sağlığında eksiltmesini sağlayalım
istenildiğinde tek bir fonksiyon ile karakterin durumunu görebilelim

"""
class Hero():
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health

    def darbe(self, victim):
        victim.health -= self.power*0.75
        print(f"{victim.name} taken {self.power*0.75} damage from {self.name}")


    def vurma(self, victim):
        victim.health -= self.power
        print(f"{victim.name} taken {self.power*0.75} damage from {self.name}")
 
    
    def healthStatus(self):
        print(f"{self.name} current health: {self.health}")


hero1 = Hero("IronMan", 20,20)
hero2 = Hero("Spidey",15,30)

hero1.vurma(hero2)
hero2.healthStatus()


    

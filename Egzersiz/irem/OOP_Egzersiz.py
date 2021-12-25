"""
kahramanların tanımlanabileceği bir yapı oluşturun
parametre olarak adi,guc,saglik
darbe,vurma adında iki fonksiyon ile secilen karakterin güçleri 
ölçüsünde diğer karakterin sağlığında eksiltmesini sağlayalım
istenildiğinde tek bir fonksiyon ile karakterin durumunu görebilelim
"""

class Hero:
    def __init__(self,adi,guc,saglik):
        self.adi = adi
        self.guc = guc
        self.saglik = saglik
    
    def darbe(self,hero):
        self.saglik -= hero.guc
        print(f"{self.adi} darbe aldı ")

    def vurma(self,hero):
        hero.saglik -= self.guc
        print(f"{self.adi} vurdu")


hero = ("Captain America",20,40)
hero2 = ("Hulk",30,60)
hero3 = ("Thor",20,50)
"""
kahramanların tanımlanabileceği bir yapı oluşturun
parametre olarak adi,guc,saglik
darbe,vurma adında iki fonksiyon ile secilen karakterin güçleri 
ölçüsünde diğer karakterin sağlığında eksiltmesini sağlayalım
istenildiğinde tek bir fonksiyon ile karakterin durumunu görebilelim
"""
from abc import ABC,abstractmethod
class Superhero(ABC): #Parent
    
    @abstractmethod
    def damage(self):
        pass
    @abstractmethod
    def takendamage(self,dmg):
        pass
    @abstractmethod
    def herocond(self):
        pass
    

class Marvel(Superhero): # child
    def __init__(self,adi,guc,saglik,super_power):
        super().__init__()
        self.Superhero = adi
        self.Superhero = guc
        self.Superhero = saglik
        self.Marvel = super_power
    def takendamage(self,dmg):
        self.saglik = self.saglik - dmg

    def damage (self):
        return self.guc
    @property
    def herocond(self):
        return f"{self.adi} - Sağlık:{self.saglik}"


class DC(Superhero): # child
    def __init__(self,adi,guc,saglik,super_power):
        super().__init__()
        self.Superhero = adi
        self.Superhero = guc
        self.Superhero = saglik
        self.DC = super_power
    def takendamage(self,dmg):
        self.saglik = self.saglik - dmg
    
    def damage (self):
        return self.guc

    def herocond(self):
        print(self)

    def __del__(self):
        print(self.adi," sizlere ömür")

        

obj=Marvel("spiderman",50,100,"yumruk")
print(Marvel.herocond(self))
"""
kahramanların tanımlanabileceği bir yapı oluşturun
parametre olarak adi,guc,saglik
darbe,vurma adında iki fonksiyon ile secilen karakterin güçleri 
ölçüsünde diğer karakterin sağlığında eksiltmesini sağlayalım
istenildiğinde tek bir fonksiyon ile karakterin durumunu görebilelim
"""
import random as rnd
import time
class Hero:
    def __init__(self,adi,guc,saglik,*args,**kwargs):
        self.adi = adi # örnek özellik instance attribute
        self.guc = guc
        self.saglik = saglik
    def vurma(self): # instance method
        print(f"{self.adi}  vuruldu")
        return self.guc
    def darbe(self, guc): # instance method
        print(f"{self.adi}  darbe aldi")
        self.saglik -= guc
        
    def __del__(self):
        print('rip', self.adi)
    
    def durum(self):
        return f"{self.adi} - Sağlık:{self.saglik}"

class Ironman(Hero):
    def __init__(self):
        super().__init__("Ironman", 25, 80)
class Deadpool(Hero):
    def __init__(self):
        super().__init__("Deadpool", 50, 50)
class CaptainAmerica(Hero):
    def __init__(self):
        super().__init__("CaptainAmerica", 10, 50)

karakterList = [Ironman(), Deadpool(), CaptainAmerica()]
P1 = rnd.choice(karakterList)
P2 = rnd.choice(karakterList)

while P1.saglik > 0 and P2.saglik > 0:
    time.sleep(0.5)
    P1.darbe(P2.vurma())
    P2.darbe(P1.vurma())
    print(P1.durum())
    print(P2.durum())
else:
    if P1.saglik > P2.saglik:
        print(P1.adi, " Kazandi")
    elif P1.saglik < P2.saglik:
        print(P2.adi, " Kazandi")

# obj1 = Hero("Ironman","100","100")
# obj2 = Hero("Spiderman","100","100")
# obj1.darbe()

"""
kahramanların tanımlanabileceği bir yapı oluşturun
parametre olarak adi,guc,saglik
darbe,vurma adında iki fonksiyon ile secilen karakterin güçleri 
ölçüsünde diğer karakterin sağlığında eksiltmesini sağlayalım
istenildiğinde tek bir fonksiyon ile karakterin durumunu görebilelim
"""
import random as rnd
class MarvelHero:
    def __init__(self,adi,guc,saglik,*args,**kwargs):
        self.adi = adi
        self.guc = guc
        self.saglik = saglik
        self.superguc = 0    
    def vurma1(self):
        return self.guc//2

    def vurma2(self):
        return self.guc//3

    def vurma3(self):
        return self.guc

    def vurma(self):
        liste = [self.vurma1,self.vurma2,self.vurma3]
        return rnd.choice(liste)()
    
    def darbe1(self,guc):
        self.saglik -= guc//2
    
    def darbe2(self,guc):
        self.saglik -= guc//3

    def darbe3(self,guc):
        self.saglik -= guc

    def darbe(self,guc):
        liste = [self.darbe1,self.darbe2,self.darbe3]
        rnd.choice(liste)(guc)
        


    @property
    def durum(self):
        return f"{self.adi} - Sağlık:{self.saglik}"

    def __del__(self):
        print("R.I.P",self.adi)


# deadpool = MarvelHero("deadpool", 10, 100)
class Deadpool(MarvelHero):
    def __init__(self):
        super().__init__("Deadpool", 25, 500)
    
    def darbe(self,guc):
        if self.superguc == 5:
            print(self.adi,"Süper Güç Kullandı")
            self.superguc = -1 
            self.saglik = 500
        elif self.superguc >= 0:
            self.superguc += 1
        super().darbe(guc)

class CaptainAmerica(MarvelHero):
    def __init__(self):
        super().__init__("CaptainAmerica", 30, 550)

class IronMan(MarvelHero):
    def __init__(self):
        super().__init__("IronMan", 20, 600)

class Hulk(MarvelHero):
    def __init__(self):
        super().__init__("Hulk", 25, 500)

    def vurma(self):
        if self.superguc == 5:
            print(self.adi,"Süper Güç Kullanı")
            self.superguc = -1 
            return self.guc*5
        elif self.superguc >= 0:
            self.superguc += 1
        return super().vurma()


karakterList = [Deadpool,CaptainAmerica,IronMan,Hulk]
P1 = rnd.choice(karakterList)()
P2 = rnd.choice(karakterList)()
import time
while P1.saglik > 0 and P2.saglik > 0:
    time.sleep(0.5)
    P1.darbe(P2.vurma())
    P2.darbe(P1.vurma())
    print(P1.durum)
    print(P2.durum)
else:
    if P1.saglik > P2.saglik:
        print(P1.adi,"Kazandı")
    elif P1.saglik < P2.saglik:
        print(P2.adi,"Kazandı")
    else:
        print("Berabere")
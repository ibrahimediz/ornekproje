class Hero:
    def __init__(self,adi,guc,saglik,*args,**kwargs):
        self.adi = adi #
        self.guc = guc
        self.saglik = saglik
        Hero.liste.append((self.adi,self.guc,self.saglik))
    def darbe(self): # instance method
        self.guc = self.saglik -1
        print(f"{self.adi}  darbe aldi")
    def vurma(self): # instance method
        self.guc = self.saglik -2
        print(f"{self.adi}  vuruldu")
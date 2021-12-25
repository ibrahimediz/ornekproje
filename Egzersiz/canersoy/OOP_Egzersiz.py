class Hero:
    list_ = []
    def __init__(self):
        self.adi = adi
        self.guc = guc
        self.saglik = saglik
        Hero.list_.append((self.adi,self.guc,self.saglik))
    
    def darbe(self, enemy): # bence buraya diger classi almak gerekiyor
        self.saglik = self.saglik - enemy.guc # gibi
    
    def vurma(self):
        return self.guc

    @classmethod
    def HeroStatus(cls):
        print(*cls.list_,sep="\n")


thor = Hero('thor', 1000, 100)
wolverine = Hero('wolverine', 1000, 100)
thor.darbe(wolverine) # ben boyle dusundum
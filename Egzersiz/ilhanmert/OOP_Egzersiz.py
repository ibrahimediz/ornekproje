from abc import ABC, abstractmethod

class Kahraman(ABC):
    #@abstractmethod
    def __init__(self,ad,guc,saglik):
        self_ad=ad
        self_guc=guc
        self_saglik=saglik
    
    def darbe(self, hasar):
        self_saglik=self_saglik-hasar
    
    def vurma(self):
        return self.guc

    def __del__(self):
        print("gg",self,adi)
    
    def karakterDurumu(self):
        print(f"karakter adi: {self_ad}")
        print(f"karakter gucu: {self_guc}")
        print(f"saglik: {self_saglik}")
    
    

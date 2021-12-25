"""
"""

class Kahramanlar():

    def __init__(self,adi,guc,saglik):
        self.adi = adi
        self.guc = guc
        self.saglik = saglik
    
    def darbe(self,guc):
        self.saglik -= guc

    def vurma(self,ikinciKarakter):
        return self.guc 

    def karakterDurum(self):
        
        print(f"{self.adi} adı, {self.saglik} sağlık, {self.guc} gücü, ")        

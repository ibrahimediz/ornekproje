class A:
    def __init__(self,yetki):
        self.yetki = yetki
        self.__gizli = 2
# __gizli gizli
# __gizli_ gizli
# __gizli__ gizli değil
obj1 = A(1)
print(obj1.yetki)
# print(obj1.__gizli) # AttributeError: 'A' object has no attribute '__gizli'


class A:
    def __init__(self,yetki):
        self.yetki = yetki
        self.__gizli = 2

    @property # asagidakiler fonksiyonun ismiyle ayni olmak zorunda
    def gizli(self): # getter
        if self.yetki == 1:
            return self.__gizli
        else:
            raise Exception("Yetki Hatası")
    @gizli.setter
    def gizli(self,param):
        if self.yetki == 1:
            if isinstance(param,int) and param in range(10):
                self.__gizli = param
            else:
                raise Exception("Değer Hatası")
        else:
            raise Exception("Yetki Hatası")
        
    @gizli.deleter
    def gizli(self):
        if self.yetki == 1:
            self.__gizli = -1*self.gizli
        else:
            raise Exception("Yetki Hatası")
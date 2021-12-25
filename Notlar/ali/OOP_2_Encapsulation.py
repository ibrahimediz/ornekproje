# class A:
#     def __init__(self,yetki):
#         self.yetki=yetki
#         self.__gizli = 2

# obj1=A(1)
# print(obj1.yetki) # 1 

# # print(obj1.__gizli) #AttributeError: 'A' object has no attribute '__gizli'
# print(obj1._A__gizli)

# class A:
#     def __init__(self,yetki):
#         self.yetki=yetki
#         self.__gizli = 2

#     def gizliGetir(self):
#         if self.yetki == 1:        
#             return self.__gizli
#         else:
#             raise Exception("Yetki hatası")
    
# obj1 = A(1)
# obj2 = A(2)
# print(obj1.gizliGetir())
# print(obj2.gizliGetir()) # Exception

class A:
    def __init__(self,yetki):
        self.yetki=yetki
        self.__gizli = 2

    @property
    def gizli(self):
        if self.yetki == 1:        
            return self.__gizli
        else:
            raise Exception("Yetki hatası")

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

    
obj1 = A(1)
obj2 = A(2)
print(obj1.gizli)
# print(obj2.gizli) # Exception: Yetki Hatası
obj1.gizli = 3
print(obj1.gizli)
del obj1.gizli
print(obj1.gizli)
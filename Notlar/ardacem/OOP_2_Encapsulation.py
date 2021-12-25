"""
private
public
protected
"""
#################################
# class A:
#     def __init__(self,yetki):
#         self.yetki = yetki
#         self.__gizli = 2
# # __gizli gizli
# # __gizli_ gizli
# # __gizli__ gizli degil
# # _yari_gizli

# obj1 = A(1)
# print(obj1.yetki)
# print(obj1.__gizli)
#################################
# class A:
#     def __init__(self,yetki):
#         self.yetki = yetki
#         self.__gizli = 2
#     def gizliGetir(self): # getter
#         if self.yetki == 1:
#             return self.__gizli
#         else:
#             raise Exception("Yetki Hatasi")
# obj1 = A(1)
# print(obj1.gizliGetir())
# print(obj2.gizliGetir())  
# 
class A:
    def __init__(self,yetki):
        self.yetki = yetki
        self.__gizli = 2
    @property
    def gizli(self): # getter
        if self.yetki == 1:
            return self.__gizli
        else:
            raise Exception("Yetki Hatasi")
obj1 = A(1)
print(obj1.gizli)

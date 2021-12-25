""" 
private => not accessible
public => accessible
protected => semi accessible
"""

# __gizli gizli
# __gizli_ gizli
# __gizli__ gizli değil
# _yari_gizli

################################### property
# class A:
#     def __init__(self,yetki):
#         self.yetki = yetki
#         self.__gizli = 2

#     @property
#     def gizli(self): # getter
#         if self.yetki == 1:
#             return self.__gizli
#         else:
#             raise Exception("Yetki Hatası")
#     @gizli.setter
#     def gizli(self,param):
#         if self.yetki == 1:
#             if isinstance(param,int) and param in range(10):
#                 self.__gizli = param
#             else:
#                 raise Exception("Değer Hatası")
#         else:
#             raise Exception("Yetki Hatası")
        
#     @gizli.deleter
#     def gizli(self):
#         if self.yetki == 1:
#             self.__gizli = -1*self.gizli
#         else:
#             raise Exception("Yetki Hatası")

    
# obj1 = A(1)
# obj2 = A(2)
# print(obj1.gizli)
# # print(obj2.gizli) # Exception: Yetki Hatası
# obj1.gizli = 3
# print(obj1.gizli)
# del obj1.gizli
# print(obj1.gizli)
# """ 
# private
# public ----> pythonda yoklar!!!
# protected
# """
# ##################### Dışarıdan erişim var #####################

# class A:
#     def __init__(self,yetki):
#         self.yetki = yetki
        
# obj1 = A(1)
# print(obj1.yetki)
# ###################### __ yapınca gizli #####################3
# class A:
#     def __init__(self,yetki):
#         self.yetki = yetki
#         self.__gizli = 2 #--> private olduğu söyleniyor böyle
        
# # __gizli gizli
# # __gizli_ gizli
# # __gizli__ gizli değil
# #_yarıgizli --> protected

# obj1 = A(1)
# print(obj1.yetki)
# print(obj1.__gizli)  # AttributeError: 'A' object has no attribute '__gizli'
# print(obj1._A__gizli) # böyle erişiliyor gizli veriye !!

# ######################################################

# class A:
#     def __init__(self,yetki):
#         self.yetki = yetki
#         self.__gizli = 2
#     @property #--> set tanımlana bilir
#     def gizliGetir(self): # getter
#         if self.yetki == 1:
#             return self.__gizli
#         else:
#             raise Exception("Yetki Hatası")
    
# obj1 = A(1)
# obj2 = A(2)
# print(obj1.gizliGetir()) #---> if olmadan önce çalıştı
# print(obj2.gizliGetir()) # Exception: Yetki Hatası

################################### property
# class A:
#     def __init__(self,yetki):
#         self.yetki = yetki
#         self.__gizli = 2

#     @property #---> isim gizli olan dosyayla aynı olmalı
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
#######################################################


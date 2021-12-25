# import time
# def HesapZaman(fonk):
#     def icFonk(*args,**kwargs):
#         basla = time.time()
#         fonk(*args,**kwargs)
#         bitis = time.time()
#         print(f"{fonk.__name__} {bitis-basla}")
#     return icFonk

# @HesapZaman
# def faktoriyel(sayi):
#     time.sleep(2)
#     sonuc = 1
#     for i in range(1,sayi+1):
#         sonuc *= i
#     print(sonuc)
# import math

# @HesapZaman
# def Mfaktoriyel(sayi):
#     time.sleep(2)
#     print(math.factorial(sayi))

# faktoriyel(5)
# Mfaktoriyel(5)


################################################
# class A:
#     def __init__(self):
#         self.a = "A"

#     @staticmethod
#     def pi():
#         return 22/7


# A.pi()

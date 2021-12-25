# class A: #Parent
#     def __init__(self):
#         self.a = "A"
    
#     def soyleA(self):
#         print(self.a)
    
#     def soyle(self):
#         print("A Sınıfından Çalıştım")

# class B(A): # child
#     def __init__(self): #overriding
#         super().__init__() 
#         self.b = "B"
    

# objb = B()
# objb.soyle()
# objb.soyleA()
####################başka bir çok biçimlilik#######################

# class A:
#     def soyle(self):
#         print("A Sınıfından Çaşlıştım")
# class B:
#     def soyle(self):
#         print("A Sınıfından Çaşlıştım")

# liste = [A(),B()]
# def fonk(obj):
#     obj.soyle()
# for item in liste:
#     fonk(item)

############### abstraction ################

# from abc import ABC,abstractmethod
# class Arac(ABC):
#     @abstractmethod
#     def yakitTipiSoyle(self):
#         pass

# # obj = Arac() # TypeError: Can't instantiate abstract class Arac with abstract methods yakitTipiSoyle

# # class KaraAraclari(Arac):
# #     pass

# # objKaraArac = KaraAraclari() #TypeError: Can't instantiate abstract class KaraAraclari with abstract methods yakitTipiSoyle


# class KaraAraclari(Arac):
#     def yakitTipiSoyle(self):
#         print("Benzin")

# objKaraArac = KaraAraclari() #TypeError: Can't instantiate abstract class KaraAraclari with abstract methods yakitTipiSoyle
# objKaraArac.yakitTipiSoyle()

################# Decorators ###################

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

#################### static method ###########################

# class A:
#     def __init__(self):
#         self.a = "A"

#     @staticmethod
#     def pi():
#         return 22/7


# A.pi()

############################################################
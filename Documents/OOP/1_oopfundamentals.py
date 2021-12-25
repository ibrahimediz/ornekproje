#  OOP  object oriented programming
#  DRY  Dont repeat Yourself
#  WET  We Enjoy Texting
###########################
# class sınıf 
# object nesne ya da instance örnek
###############
# attribute # özellik
# method # metot
###########################
# class Sinif:
#     pass
# print(type(Sinif)) # <class 'type'>
# print(*dir(Sinif),sep="\n")

# print(type(Sinif())) # <class '__main__.Sinif'>
# print(__name__) # __main__
############################
# class Sinif:
#     pass
# Sinif() # instantiation
# class Sinif:
#     def __init__(self):# constructor Yapıcı
#         print("Çalıştım")
# Sinif()
###########################
# class Kedi:
#     tur = "fellis catus" # class attribute
#     def __init__(self,adi,cins,yas,*args,**kwargs):
#         self.adi = adi # örnek özellik instance attribute
#         self.cins = cins
#         self.yas = yas
    
#     def beslenme(self): # instance method
#         print(f"{self.adi}  beslendi")

# obj1 = Kedi("Melek","Tekir","11")
# obj2 = Kedi("Duman","Scottish","12")
# print(obj1.adi)
# print(obj2.adi)
# obj1.beslenme()
###########################
# class Kedi:
#     tur = "fellis catus" # class attribute
#     liste = []
#     def __init__(self,adi,cins,yas,*args,**kwargs):
#         self.adi = adi # örnek özellik instance attribute
#         self.cins = cins
#         self.yas = yas
#         Kedi.liste.append((self.adi,self.cins,self.yas))
#     def beslenme(self): # instance method
#         print(f"{self.adi}  beslendi")

#     @classmethod
#     def turGetir(cls):
#         print(cls.tur)

#     @classmethod
#     def kacKedi(cls):
#         print(len(cls.liste))
    
#     @classmethod
#     def kediListe(cls):
#         print(*cls.liste,sep="\n")



# obj1 = Kedi("Melek","Tekir","11")
# obj2 = Kedi("Duman","Scottish","12")
# obj1.beslenme()
# Kedi.kacKedi()
# Kedi.kediListe()
###################################### destructor
class Kedi:
    tur = "fellis catus" # class attribute
    liste = []
    def __init__(self,adi,cins,yas,*args,**kwargs):
        self.adi = adi # örnek özellik instance attribute
        self.cins = cins
        self.yas = yas
        Kedi.liste.append((self.adi,self.cins,self.yas))
    def beslenme(self): # instance method
        print(f"{self.adi}  beslendi")

    @classmethod
    def turGetir(cls):
        print(cls.tur)

    @classmethod
    def kacKedi(cls):
        print(len(cls.liste))
    
    @classmethod
    def kediListe(cls):
        print(*cls.liste,sep="\n")

    def __del__(self): #destructor
        print("R.I.P",self.adi)

# obj1 = Kedi("Melek","Tekir","11")
# obj2 = Kedi("Duman","Scottish","12")
# obj1.beslenme()
# Kedi.kacKedi()
# Kedi.kediListe()
# print(id(obj1))
# del obj1
# input()
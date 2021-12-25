# liste = [1,2,2,3]
# len(liste)
# metin = "asdas"
# len(metin)
#################
# def fonk(*args): # overloading
#     pass
# public void fonk(string a){

# }
# public void fonk(string a,string b){

# }
#################
class A: #Parent
    def __init__(self):
        self.a = "A"
    
    def soyleA(self):
        print(self.a)
    
    def soyle(self):
        print("A Sınıfından Çalıştım")

class B(A): # child
    def __init__(self): #overriding
        super().__init__() 
        self.b = "B"
    

objb = B()
objb.soyle()
objb.soyleA()

#####################
# class A:
#     def soyle(self):
#         print("A Sınıfından Çaşlıştım")
# class B:
#     def soyle(self):
#         print("B Sınıfından Çaşlıştım")

# liste = [A(),B()]
# def fonk(obj):
#     obj.soyle()
# for item in liste:
#     fonk(item)
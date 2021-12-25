# class A:
#     def __init__(self):
#         self.a = "A"
    
#     def soyleA(self):
#         print(self.a)
    
#     def soyle(self):
#         print("A Sınıfından Çalıştım")

# class B(A): #---> inheritance
#     #pass # yazınca inheritence ettiği classın aynısı olur
#     def __init__(self,):
#         super().__init__() #---> a sınıfını burda tamınladın ilk a'yı sonra b yi çalıştırır
#         #üst kısım ilk kalıtım alınmış yeri çalıştırır.
#         self.b = "B"

#     def soyleB(self):
#         print(self.b)

# class C(B):
#     def __init__(self):
#         super().__init__() #---> b den inherint eder
#         self.c = "C"

# objb = C()
# objb.soyle()
# objb.soyleA()

#########################################################class A:
# class A:
#     def __init__(self):
#         self.a = "A"
    
#     def soyleA(self):
#         print(self.a)
    
#     def soyle(self):
#         print("A Sınıfından Çalıştım")

# class B:
#     def __init__(self):
#         self.b = "B"
    
#     def soyleA(self):
#         print(self.b)
    
#     def soyle(self):
#         print("B Sınıfından Çalıştım")

# class C(A,B):
#     def __init__(self):
#         A.__init__(self)
#         B.__init__(self)
#         #super().__init__()
#         #B.__init__(self) şeklinde de yazıla bilir
#         self.c = "C"

#     def soyle(self): #---> b'de çalışsın diye
#         B.soyle(self)
# objc = C()
# objc.soyle() # --> ilk miras aldığı hangisiyse onu çalıştırır
############################################################


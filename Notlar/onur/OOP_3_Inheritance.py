# class A: #Parent
#     def __init__(self):
#         self.a = "A"
    
#     def soyleA(self):
#         print(self.a)
    
#     def soyle(self):
#         print("A Sınıfından Çalıştım")

# class B(A): # child
#     def __init__(self):
#         super().__init__()
#         self.b = "B"
# objb = B()
# objb.soyle()
# objb.soyleA()

################################### 
# class A: #Parent
#     def __init__(self):
#         self.a = "A"
    
#     def soyleA(self):
#         print(self.a)
    
#     def soyle(self):
#         print("A Sınıfından Çalıştım")

# class B(A): # child
#     def __init__(self):
#         super().__init__()
#         self.b = "B"

#     def soyleB(self):
#         print(self.b)

# class C(B):
#     def __init__(self):
#         super().__init__()
#         self.c = "C"

# objc = C()

################################################
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
#         self.c = "C"



# objc = C()
# objc.soyle() # A Sınıfından Çalıştım
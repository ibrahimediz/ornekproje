class A: #Parent
    def __init__(self):
        self.a = "A"
    
    def soyleA(self):
        print(self.a)
    
    def soyle(self):
        print("A Sınıfından Çalıştım")

#Multi inheritance
class B(A): # child
    def __init__(self):
        super().__init__()
        self.b = "B"

    def soyleB(self):
        print(self.b)

class C(B):
    def __init__(self):
        super().__init__()
        self.c = "C"

objc = C()
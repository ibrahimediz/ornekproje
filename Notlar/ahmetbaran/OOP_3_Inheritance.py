class A:
    def __init__(self):
        self.a = "A"
    
    def soyleA(self):
        print(self.a)
    
    def soyle(self):
        print("A Sınıfından Çalıştım")

class B(A):
    pass
objb = B()
print(objb.a)
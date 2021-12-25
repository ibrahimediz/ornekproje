class A:
    def __init__(self):
        self.a = "A"

    def soyleA(self):
        print(self.A)

    def soyle(self):
        print("A sınıfından çalıştım")

class B(A):
    def __init__(self):
        super().__init__()
        self.b = "B"

objb =B()
objb.soyleA()
objb.soyle()
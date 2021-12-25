""" 
private
public
protected
"""
class A:
    def __init__(self,yetki):
        self.yetki = yetki
        self.__gizli = 2
# __gizli gizli
# __gizli_ gizli
# __gizli__ gizli değil
obj1 = A(1)
print(obj1.yetki)
# print(obj1.__gizli) # AttributeError: 'A' object has no attribute '__gizli'
print(dir(obj1))
print(obj1._A__gizli)
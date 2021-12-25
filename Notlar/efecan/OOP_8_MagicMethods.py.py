class A:
    def __init__(self,param):
        self.param = param
    def __str__(self):
        return str(self.param)
    
    def __lt__(self,obj):
        return self.param < obj.param
    

#########################
# var1 = 3
# print(*dir(3))
# var2 = 2
# print(var1>var2)
#########################

var1 = A(5)
var2 = A(8)
print(var1) # <__main__.A object at 0x7f40c9030c40>
print(var1>var2)


class A(object):
    def __new__(cls):
         print("Creating instance")
         return super(A, cls).__new__(cls)
  
    def __init__(self):
        print("Init is called")

print(A())
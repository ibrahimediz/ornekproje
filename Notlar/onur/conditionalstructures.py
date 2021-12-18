a = 0 => "Boş"
a = -1 => "Dolu"
b = ""
c = [1] => "Dolu"
d = ()
e = {}
if c:
    print("Dolu")
else:
    print("Boş")


var1 = "Ali"   # A => 65 ASCII
var2 = "ali"   # a => 97  
if var1<var2:
    print("Doğru") => "Doğru"
else:
    print("Yanlış")


a = 5
sonuc = "Tek" if a % 2>0 else "Çift"
print(sonuc)
"""
str
"""
# "" ve '' string olarak algılanır
var1 = 'Ankara' 
var2 = "istanbul"

# """ """ docstring olarak algılanır
var3 = """ lorem ipsum"""
# print(__doc__)
"""
Erişim 
var1[index num] tek bir karakter
var1[start:end(not included):step]
"""
var4 = "Yemeksepeti"
#       012345678910
#      -11-10-9-8-7-6-5-4-3-2-1

print(var4[10])
print(var4[-1])
print(var4[5:])
print(var4[:-6])
######
var1 = "Yaşamak"
print(var1[1::2]) # aaa # 1 3 5
print(var1[::-1]) # kamaşaY

# Bu erişim sistemi hepsinde(Tuple, Dict, List) 
# aynıdır.

var1 = "Teşekkürler Süpermen"
var1.replace("e", "ı").replace("ü", "i")
var1.replace("e", "ı",) #
# bunun çıktısı str olduğu için 
# tekrar fonksiyon ile erişilebilir.
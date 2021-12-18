"""
str
Tanımlama 
"""
# var1 = 'Ankara'da'
var1 = "Ankara'da"
var1 = """
yoksun sen aslında yalnızım bu kumsalda,
 neler neler yapıyorsun bensizken Ankara'da """
# print(__doc__)
"""
Erişim
var1[indis numarası] tek bir karakter
var1[baslangic:bitis(e kadar):adim]
"""
var1 = "YemekSepeti"
#       012345678910
#  -11-10-9-8-7-6-5-4-3-2-1
print(var1[10])
print(var1[-1])
print(var1[0:5]) # Yemek => 0 1 2 3 4
print(var1[5:11]) # Sepeti => 5 6 7 8 9 10 
print(var1[:5]) #  Yemek => 0 1 2 3 4
print(var1[5:]) # Sepeti => 5 6 7 8 9 10 
print(var1[:-6])
var1 = "Yaşamak"
#       0123456
print(var1[1::2]) # aaa # 1 3 5
print(var1[::2]) # Yşmk # 0 2 4 6
print(var1[::-1]) # kamaşaY

var1 = "Teşekkürler Süpermen"
print(var1.replace("e","ı").replace("ü","ı")) # Tışıkkırlır Sıpırmın
print(var1.replace("e", "ı",2)) # Tışıkkürler Süpermen

# var1 = "Teşekkürler Süpermen" # => Teşekkürler Süpırmın
# el Cevap
# print(var1[::-1].replace('e', 'i',2)[::-1])


# var1 = "Teşekkürler Süpermen" # => Teşekkürler Süpırmın
# var2 = var1.split()
# # var2 => ["Teşekkürler","Süpermen"]
# var2[1]  = var2[1].replace("e","ı")
# var1 = " ".join(var2)
# print(var1)
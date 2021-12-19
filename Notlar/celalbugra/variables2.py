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

"""
str immutable bir veri tipidir.
"""
# burdaki odak nokta verinin güvenliği
# verinin değişikliğe uğrama ihtimali ortadan kaldırır

# var1. direk yardımcı fonksiyonları ekranda gösterir.var1

# strip e direk koleksiyon veririz.
var1 = "_____________________Yemeksepeti_________"
print(var1.strip("_")) # Yemeksepeti
var1 = "_____aaaa______Yemeksepeti_____"
print(var1.strip("_")) # aaaa______Yemeksepeti
var1 = "_________ssss_____aaa___Yemek_sepeti___ss"
print(var1.strip("_sa "))

# split
var1 = "Yemek_sepeti"
print(var1.split(' ',maxsplit=1))

# join
liste = ["Yemek","Sepeti","23262"]
print(";".join(liste)) 
# stringe dönüştürmeninde bir yolu olarak kullanılabilir.
#  

"""
append
insert
remove
pop
copy
"""







##### tuple

# var1 = 1,
# var1 = (1,)
# demet = (1,2,21,"Jamiryo")
# demet[1] = 2 tuple immutable bir veri tipidir.
# liste = [1,2,3,4] list mutabledır

###############
# a = "4"
# print("çi","pet"*5)
# liste1 = [1,2,3]
# liste2 = [5,6,7]
# liste3 = liste1 + liste2

# ## "".joins(liste) direk string olarak döndürür


# ####################
# # dict
# # mapping datatype

# sozluk = {"1":"Bir"}
#         # KEY:value => bu bir itemdır

# sozluk = {"1":"Bir"}
# sozluk["1"]
# sozluk.get("1")
# sozluk.setdefault("2","iki") # ekledik
# print(sozluk.keys())
# print(sozluk.values())
# print(sozluk.items())


"""
set
"""
liste1 = [1,2,3,4,5,6]
liste2 = [1,2,2,2,3,5,6,5,6,8,9,10,9]
kume1 = set(liste1)
kume2 = set(liste2)
kume1.difference(kume2)
kume2.difference(kume1)
kume1.sym



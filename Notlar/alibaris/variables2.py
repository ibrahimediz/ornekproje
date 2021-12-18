"""
örn: var1 = "YemekSepeti"
             012345678910
       -11-10-9-8-7-6-5-4-3-2-1

* indislerde normal erişimde [0,len(arr)-1] kadar
* tersten erişimde de [-len(arr),(-1)]'e kadar
"""

# var1 = "YemekSepeti"
# #       012345678910
# #  -11-10-9-8-7-6-5-4-3-2-1
# print(var1[10])
# print(var1[-1])
# print(var1[0:5]) # Yemek => 0 1 2 3 4
# print(var1[5:11]) # Sepeti => 5 6 7 8 9 10 
# print(var1[:5]) # 


# var1 = "Yaşamak"
# #       0123456
# print(var1[1::2]) # aaa # 1 3 5  Yalnızca a'ları yazdırdık ikişer şekilde gidereek
# print(var1[::2]) # Yşmk # 0 2 4 6
# print(var1[::-1]) # kamaşaY


# STR UMMUTABLE!!


# strip'i meyve soymaya benzetilebilir, 
# etrafındakileri kaldırır..
# # strip bir koleksiyon alır, değiştirmek istediklerini tek tek vermelisin
# var1 = "______________YemekSepeti________________"

# var2 = var1.strip("_")

# var1 = "_____aa_________YemekSepeti________bb____ ____"
# # print(var1.strip("_a b"))

# # SPLIT
# # rsplit
# # max_split parametresi ile en fazla kaç defa böleceği belirlenir
# # liste döndürür

# var1 = "Herkesin hayatına kimse karışamaz" 
# print(var1.split(' ',maxsplit = 2)) # ['Herkesin', 'hayatına', 'kimse karışamaz']
# print(var1.split(' ',maxsplit = 1)) # ['Herkesin', 'hayatına kimse karışamaz']

# # *LIST'ler OBJE tutar. O yüzden her veri tipinden eleman alabilir.

# # *LIST'lerde assignment operatörü ve copy arasındaki farkı unutma


# liste = [1,2,3,4]
# liste.append(5)
# liste.insert(0,0) # [i]lk parametre [i]ndis.. i'lerin benzerliğinden aklına maple
# print(liste.pop()) # indis belirtmezsek en sondaki elemanı çıkarır
# print(liste.pop())  # listenin durumu  => [1, 2, 3, 4]
# print(liste.pop(1)) # listenin durumu  => [1, 3, 4]

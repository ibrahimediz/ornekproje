"""Str"""
"""
    var = '' differs from var = ""
                          ex: var = 'Ankara'da' syntax error
                          ex: var = "Ankara'da" compiles
    
    Triples quotes allow multiple lines
"""

# var1 ="Yemeksepeti"  # index starts from 0 also works reverse ex below
# print(var1[10]) # i
# print(var1[-1]) # i
# print(var1[0:5]) # Yemek 0 1 2 3 4, 5 wont be included
# print(var1[:5]) # Yemek 0 1 2 3 4, 5 wont be included   starting point is not needed
# print(var1[:-6]) # Yemek 0 1 2 3 4, 5 Starts from 0 to index -6 and -6 not included (s)
# print(var1[5:11]) # Sepeti 5 6 7 8 9 10
# print(var1[5:]) # Sepeti 5 6 7 8 9 10 end point is not needed
# print(var1[1::2]) # eespt  starts from 1 to the end with 2 steps
# """
#     [start:end:step]
# """

# var2 = "Teşekkürler Süpermen"
# print(var2.replace("e", "ı").replace("ü", "ı"))
# var2 = var1.split()
# # var2 => ["Teşekkürler","Süpermen"]
# var2[1]  = var2[1].replace("e","ı")
# var1 = " ".join(var2)
# print(var1)

"""
Str is immutable data type
var1[1] ="a" errors
"""

# var1 = "______________________Yemek_Sepeti________________________"
# print(var1.strip('_')) # Yemek_Sepeti
# var1 = "____________aaaa__________Yemek_Sepeti________________________"
# print(var1.strip('_')) # aaaa__________Yemek_Sepeti
# var1 = "___ ______sssss__aaaa__________Yemek_Sepeti______ssss______ _____aaaa_______"
# print(var1.strip('_sa '))
# print(var1.lstrip('_sa ')) 
# print(var1.rstrip('_sa ')) 
# var1 = "Yemek_Sepeti"
# print(var1.split('_')) # ['Yemek', 'Sepeti']
# var1 = "Herkesin hayatına kimse karışamaz"
# print(var1.split(' ',maxsplit=1)) # ['Herkesin', 'hayatına kimse karışamaz']
# ###################join
# liste = ["Yemek","Sepeti","216222222222"]
# print(";".join(liste)) # Yemek;Sepeti;216222222222

# liste = [1,1.0,"deneme",[1,2,3]]
"""
append , insert, remove, pop, copy
"""
# a = [1,2,3,4]
# b=a
# b.append(3)
# print(a)

# a = [1,2,3,4]
# b=a.copy()
# b.append(3)
# print(a)

# liste = [1,2,3,4]
# liste.append(5)
# liste.insert(0,0)
# print(liste.pop())  # 5 listenin durumu  => [1, 2, 3, 4]
# print(liste.pop(1)) # 2 listenin durumu  => [1, 3, 4]
# liste = [1,2,3,1,1,1,1,1,1,]
# liste.remove(1)
# print(liste)
# liste = [item for item in liste if item != 1]
# print(liste)

"""
set
"""
liste1 =[1,2,2,2,2,2,2,2,2,3,4,5]
liste2 =[5,6,6,6,6,6,6,7,7,8,9]
kume1 = set(liste1)
kume2 = set(liste2)
print(kume1)
print(kume2)
print(kume1.difference(kume2))
print(kume2.difference(kume1))
print(kume1.symmetric_difference(kume2))
print(kume1.intersection(kume2))


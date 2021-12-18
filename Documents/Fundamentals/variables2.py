# """
# str
# Tanımlama 
# """
# # var1 = 'Ankara'da'
# var1 = "Ankara'da"
# var1 = """
# yoksun sen aslında yalnızım bu kumsalda,
#  neler neler yapıyorsun bensizken Ankara'da """
# # print(__doc__)
# """
# Erişim
# var1[indis numarası] tek bir karakter
# var1[baslangic:bitis(e kadar):adim]
# """
# # var1 = "YemekSepeti"
# # #       012345678910
# # #  -11-10-9-8-7-6-5-4-3-2-1
# # print(var1[10])
# # print(var1[-1])
# # print(var1[0:5]) # Yemek => 0 1 2 3 4
# # print(var1[5:11]) # Sepeti => 5 6 7 8 9 10 
# # print(var1[:5]) #  Yemek => 0 1 2 3 4
# # print(var1[5:]) # Sepeti => 5 6 7 8 9 10 
# # print(var1[:-6])
# # var1 = "Yaşamak"
# # #       0123456
# # print(var1[1::2]) # aaa # 1 3 5
# # print(var1[::2]) # Yşmk # 0 2 4 6
# # print(var1[::-1]) # kamaşaY


# """
# immutable veri bir veri tipidir
# """
# # var1[2] = "a" #TypeError: 'str' object does not support item assignment
# # var1 = "Teşekkürler Süpermen"
# # print(var1.replace("e","ı").replace("ü","ı")) # Tışıkkırlır Sıpırmın
# # print(var1.replace("e", "ı",2)) # Tışıkkürler Süpermen

# # var1 = "Teşekkürler Süpermen" # => Teşekkürler Süpırmın
# # el Cevap
# # print(var1[::-1].replace('e', 'i',2)[::-1])


# # var1 = "Teşekkürler Süpermen" # => Teşekkürler Süpırmın
# # var2 = var1.split()
# # # var2 => ["Teşekkürler","Süpermen"]
# # var2[1]  = var2[1].replace("e","ı")
# # var1 = " ".join(var2)
# # print(var1)
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

################################## list
liste = [1,1.0,"Jamiryo",[1,2,3,4]]
"""
append
insert
remove
pop
copy
"""
# a = [1,2,3,4]
# b = a
# b.append(3)
# print(a) # [1, 2, 3, 4, 3]

# a = [1,2,3,4]
# b = a.copy()
# b.append(3)
# print(a) # [1, 2, 3, 4]
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


################
# var1 = 1,
# var1 = (1,)
# demet = (1,2,21,"Jamiryo")
# # demet[1] = 2 tuple veri tipi immutable bir veri tipi
# liste = [1,2,3,4] # list veri tipi mutable veri tipidir
# liste[2] = 100

# print(type(liste))
# print(isinstance(liste, list))
######################
# a = "4"
# print("çi"," pet"*5)
# liste = [1,2,3]
# liste2 = [4,5,6]
# liste3 = liste + liste2 #concatenate
# a = "5"
# a = int(a)
# b = "Yakarsa"
# b = list(b) # ['Y', 'a', 'k', 'a', 'r', 's', 'a']
# print(b)
# b = "".join(b)
# print(b)

##################################################
# sozluk = {"1":"Bir"}
#         # KEY:value

# sozluk = {"1":"Bir"}
# sozluk["1"]
# sozluk.get("1")
# sozluk.setdefault("2","iki")
# print(sozluk.keys())
# print(sozluk.values())
# print(sozluk.items())
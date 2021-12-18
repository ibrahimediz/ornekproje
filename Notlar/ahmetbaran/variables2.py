var1 = """
yoksun sen aslında yalnızım bu kumsalda,
 neler neler yapıyorsun bensizken Ankara'da """ # Virgul icin gerekli

 # var1[baslangic:bitis(e kadar):adim]


"""
strip etrafini temizler sadece. 
strip koleksiyon alir

var.strip('_asd ') farkli karaktere gelene kadar sagdan soldan temizler
"""

var1 = "______________________Yemek_Sepeti________________________"
print(var1.strip('_')) # Yemek_Sepeti
var1 = "____________aaaa__________Yemek_Sepeti________________________"
print(var1.strip('_')) # aaaa__________Yemek_Sepeti
var1 = "___ ______sssss__aaaa__________Yemek_Sepeti______ssss______ _____aaaa_______"
print(var1.strip('_sa '))
print(var1.lstrip('_sa ')) 
print(var1.rstrip('_sa ')) 

"""

ctrl + k + c comment
ctrl + k + u comment iptal
"""

var1 = "Herkesin hayatına kimse karışamaz"
print(var1.split(' ',maxsplit=1)) # ['Herkesin', 'hayatına kimse karışamaz']

liste = ["Yemek","Sepeti","216222222222"]
print(";".join(liste))


# listelerde copy 

liste = [1,2,3,1,1,1,1,1,1,]

# liste.remove(1) ilk gordugu '1' i siler 

liste = [item for item in liste if item != 1] c

print(liste)
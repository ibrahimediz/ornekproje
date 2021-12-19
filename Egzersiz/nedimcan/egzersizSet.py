# iki açısı girilmiş olan bir üçgenin açılara göre türünü ekrana yazdıran python programını yazınız
# 45,45  45,90  1. İkizKenar Üçgen Dik Üçgen
# 60,60         2. Eşkenar Üçgen
# 90,25         3. Dik üçgen
# 120,41        4. Çeşit Kenar

# deg1 = int(input("1.Aci: ")) 
# deg2 = int(input("2.Aci: "))

# if deg1 == deg2:
#     print("Ikiz")

# elif deg1 != deg2:
#     if deg1 or deg2 > 90:
#         print("Dik")
#     else:
#         print("Cesit")


#Girilen bir metin içerisindeki karakterlerin sayılarını ekrana sözlük şeklinde döken bir python kodu
text = str(input("Text: "))

occurrence = {}

for i in set(text):
    occurrence[i] = text.count(i)
    
print(occurrence)
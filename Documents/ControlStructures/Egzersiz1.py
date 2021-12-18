# """TC kimlik numarasını doğrulayan python kodu yazınız.  
# Algoritmanın kuralları
# TC Kimlik numaraları 11 basamaktan oluşmaktadır. İlk 9 basamak arasında kurulan bir algoritma 
# bize 10. basmağı, ilk 10 basamak arasında kurulan algoritma ise bize 11. basamağı verir.
# 11 hanelidir.
# Her hanesi rakamsal değer içerir.
# İlk hane 0 olamaz.
# 1. 3. 5. 7. ve 9. hanelerin toplamının 7 katından, 2. 4. 6. ve 8. hanelerin toplamı çıkartıldığında, elde edilen sonucun 10′a bölümünden kalan, yani Mod10′u bize 10. haneyi verir.
# 1. 2. 3. 4. 5. 6. 7. 8. 9. ve 10. hanelerin toplamından elde edilen sonucun 10′a bölümünden kalan, yani Mod10′u bize 11. haneyi verir.
# """
# # tcKimlikNo = "10000000146"
# #             012345678910
# tcKimlikNo = input("TC Kimlik Numaranızı Giriniz:")
# if tcKimlikNo and len(tcKimlikNo) == 11:
#     if tcKimlikNo[0] != "0":
#         if tcKimlikNo.isdigit():
#             if (sum([int(tcKimlikNo[i]) for i in range(0,9,2)])*7-sum([int(tcKimlikNo[i]) for i in range(1,8,2)]))%10 == int(tcKimlikNo[9]):
#                 if sum([int(tcKimlikNo[i]) for i in range(0,10)])%10 == int(tcKimlikNo[10]):
#                     print("Doğru")
#                 else:
#                     print("Adım 5 Hata")
#             else:
#                 print("Adım 4 Hata")
#         else:
#             print("Adım 3 Hata")
#     else:
#         print("Adım 2 Hata")
# else:
#     print("Adım 1 Hata")

# # if (sum([int(tcKimlikNo[i]) for i in range(0,9,2)])*7-sum([int(tcKimlikNo[i]) for i in range(1,8,2)]))%10 == int(tcKimlikNo[9])

# turkish_id = list(map(int,list(tcKimlikNo)))

# # sum of [1st, 3rd, 5th, 7th, 9th] digits
# total_singular = sum([turkish_id[item] for item in range(0, len(turkish_id) - 1, 2)])

# # sum of [2nd, 4th, 6th, 8th] digits
# total_plural = sum([turkish_id[item] for item in range(1, len(turkish_id) - 3, 2)])


# sayi = "3,113,123,122"
sayi = input("Sayıyı giriniz:")
# üç milyon yüz yirmi üç bir yüz yirmi iki
birler = {"0":"","1":" bir ",
"2":" iki ",
"3":" üç ",
"4":" dört ",
"5":" beş ",
"6":" altı ",
"7":" yedi ",
"8":" sekiz ",
"9":" dokuz "}

onlar = {"0":"","1":" on ",
"2":" yirmi ",
"3":" otuz ",
"4":" kirk ",
"5":" elli ",
"6":" altmis ",
"7":" yetmis ",
"8":" seksen ",
"9":" doksan "}
sayi = sayi.replace(",", "").replace(".", "")
"""
10 12
11 12
9 9
7 9 
"""
sayi = sayi.zfill( len(sayi) + (3-len(sayi)%3))
print(sayi) # 003123122
"""
#   003123122
#   012345678
range(3) => 0 1 2
sayi[0:3] => (i*3):(i*3)+3
sayi[3:6]
sayi[6:9]
"""

liste = []         
for i in range(len(sayi)//3):
    liste.append(sayi[i*3:i*3+3])
print(liste) # ['003', '113', '123', '122']
#                 0      1      2      3
basamak = {0:"",1:"bin",2:"milyon",3:"milyar",4:"trilyon"}
#           3        2       1           0
#           0        1       2           3
#    4-1    
adim = 0 
for item in liste: # 123
    sonuc = ""
    if item[0] != "0": # 1
        if item[0] != "1":
            sonuc += birler[item[0]] + " yüz "
        else:
            sonuc += " yüz "# 10000000
    sonuc += onlar[item[1]] # 2
    sonuc += birler[item[2]]
    if not set(item) == set('0'):
        sonuc += basamak[(len(liste)-1)-adim]
    adim += 1
    print(sonuc)
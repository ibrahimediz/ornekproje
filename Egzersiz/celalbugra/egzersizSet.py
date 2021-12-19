# a = input("Birinci Kenar")
# b = input("İkinci Kenar")

# if (a and b) and (a.isdigit() and b.isdigit()):
#     a, b = int(a), int(b)
#     liste = [a,b,(180-(a+b))]
#     if sum(liste) == 180:
#         if len(set(liste)) == 2:
#             print("İkizkenar")
#         if len(set(liste)) == 3:
#             print("Çeşitkenar")
#         if 90 in liste:
#             print("Dik Üçgen")
    
#     else:
#         print("Açı Hatası")

# else:
#     print("Giriş Hatası")


# Yemeksepeti => {"Y":1}

text1 = input("Metin giriniz:").lower()

list1 = list(text1.strip(" "))

counts = dict()

for i in list1:

    if i not in counts:
        counts[i] = 1
    else:
        counts[i] += 1

print(counts)

#####

first_angle = int(input("Lütfen ilk açıyı giriniz: "))
second_angle = int(input("Lütfen ilk açıyı giriniz: "))

gelenAcilar = {first_angle, second_angle}

eskenar = {60, 60, 60}
dik = {25, 65, 90}
ikizKenar = {45, 45, 90}
cesitKenar = {120, 41, 19}

if gelenAcilar.intersection(ikizKenar):
    print("ikizkenar")
elif gelenAcilar.intersection(eskenar):
    print("eskenar")
elif gelenAcilar.intersection(dik):
    print("dik")
elif gelenAcilar.intersection(cesitKenar):
    print("cesitKenar")


"""
aci1 = input("1. Açıyı Giriniz:")
aci2 = input("2. Açıyı Giriniz:")
if (aci1 and aci2) and (aci1.isdigit() and aci2.isdigit()):
    aci1,aci2 = int(aci1),int(aci2)
    liste = [aci1,aci2,(180-(aci1+aci2))]
    if sum(liste) == 180:
        if len(set(liste)) == 2:
            print("İkizkenar üçgen")
        if len(set(liste)) == 3:
            print("Çeşitkenar üçgen")
        if 90 in liste:
            print("Dik Üçgen")
        if len(set(liste)) == 1:
            print("Eşkenar Üçgen")
    else:
        print("Açı Hatası")
else:
    print("Giriş Hatası")
    """

text = input("Enter text")
counter  = {}

for char in text:
    if char in counter.keys():
        counter[char] = 0
    else :
        counter[char] = counter[char] + 1

print(counter)
    



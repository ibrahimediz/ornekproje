#aci1 = input("1. Açıyı Giriniz:")
#aci2 = input("2. Açıyı Giriniz:")
#if (aci1 and aci2) and (aci1.isdigit() and aci2.isdigit()):
#    aci1,aci2 = int(aci1),int(aci2)
#    liste = [aci1,aci2,(180-(aci1+aci2))]
#    if sum(liste) == 180:
#        if len(set(liste)) == 2:
#            print("İkizkenar üçgen")
#        if len(set(liste)) == 3:
#            print("Çeşitkenar üçgen")
#        if 90 in liste:
#            print("Dik Üçgen")
#        if len(set(liste)) == 1:
#            print("Eşkenar Üçgen")
#    else:
#        print("Açı Hatası")
#else:
#    print("Giriş Hatası")
######################################Çözüm###
words = input("Lütfen metni giriniz: ")

liste=[i for i in words]
set_txt=set(liste)
occurence=dict()
for item in list(set_txt):
    occurence[item]=liste.count(item)

print(occurence)

########Başka Çözüm#########
text = 'afyonkarahisarlilastiramadiklarimizdanmisiniz'
sozluk = {x:text.count(x) for x in text.replace(" ", "")}
print(sozluk) 

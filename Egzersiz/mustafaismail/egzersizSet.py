metin = input("Metninizi giriniz").lower()

karakter_listesi = [i for i in metin]
karakter_set = set(karakter_listesi)
karakter_dic = dict()
for x in karakter_set:
    sayi = karakter_listesi.count(x)
    karakter_dic[x] = sayi

print(karakter_dic)




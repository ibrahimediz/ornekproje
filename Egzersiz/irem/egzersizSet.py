"girilen bir metin içerisindeki karakterlerin sayılarını ekrana sözlük şeklinde döken bir python kodu"

metin = input("Bir metin giriniz:")
metin_listesi = [i for i in metin]
set_ = set(metin_listesi)
sözlük = dict()
for a in list(set_):
    sözlük[a]=metin_listesi.count(a)
print(sözlük)

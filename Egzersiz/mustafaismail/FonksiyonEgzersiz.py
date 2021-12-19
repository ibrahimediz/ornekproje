from string import ascii_lowercase, ascii_uppercase, punctuation, digits
import random as rnd

sifre_uzunluk=int(input("Şifre için 4'ten büyük karakter sayısı giriniz"))

karakterler = ascii_lowercase + ascii_uppercase + punctuation + digits
sifre = []

for i in [ascii_lowercase, ascii_uppercase, punctuation, digits]:
    sifre.append(rnd.choice(str(i)))

while len(sifre) < sifre_uzunluk:
    sifre.append(rnd.choice(karakterler))

print(sifre)
sonuc = rnd.sample(karakterler,len(sifre))
print("".join(sonuc))
#aci1 = input("Birinci aciyi giriniz:")
#aci2 = input("İkinci aciyi giriniz:")
#kume1 = {int(aci1),int(aci2)}
#if aci1 + aci2 == 90:
#    print("İkizkenar ucgen")
#elif aci1 + aci2 == 135:
#    print("Dik ucgen")
#elif aci1 + aci2 == 120:
#    print("Eskanar ucgen")
#elif aci1 + aci2 == 115:
#    print("Dik ucgen")
#elif aci1 + aci2 >= 161:
#    print("Cesitkenar ucgen")

#text = input("Bir metin giriniz:")
#for chr in text:
#    chrCount = str(text.count(chr))
#    print(chr + " " + chrCount)

#dict = {}
#text = input("Bir metin giriniz: ").lower()
#for chr in text:
#    if chr in dict:
#        pass
#    else:
#        dict[chr] = str(text.count(chr))
#print(dict)

from string import ascii_lowercase,ascii_uppercase,punctuation,digits
print(ascii_lowercase,ascii_uppercase,punctuation,digits) 
import random as rnd
print(rnd.choice(ascii_lowercase))
pwLen = input ("Sifre uzunlugu giriniz: ")
pw = ""
i = 0



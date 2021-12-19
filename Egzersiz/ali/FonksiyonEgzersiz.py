from string import ascii_lowercase,ascii_uppercase,punctuation,digits
# abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 0123456789
import random as rnd
print(rnd.choice(ascii_lowercase))


liste=[]
lengthh = int(input("Lütfen karakter sınırı giriniz: "))
def passGenerate(lengthh):
    for i in range():
        liste.append(rnd.choice(ascii_lowercase))
        liste.append(rnd.choice(ascii_uppercase))
        liste.append(rnd.choice(digits))
        liste.append(rnd.choice(punctuation))
    return "".join(liste)
print(passGenerate(10))
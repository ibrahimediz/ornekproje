from string import ascii_lowercase,ascii_uppercase,punctuation,digits
import random as rnd

pwLen = int(input("Sifre uzunlugu giriniz: "))
pw = []
i = 0

while i < pwLen:
    pwMthd = rnd.choice([ascii_lowercase,ascii_uppercase,punctuation,digits])
    rndChr = rnd.choice(pwMthd)
    pw.append(rndChr)
    i=i+1

print(''.join(pw))
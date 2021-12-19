from string import ascii_lowercase,ascii_uppercase,punctuation,digits
import random as rnd

def passwordfunc ():
    pwd=''
    liste = [ascii_lowercase,ascii_uppercase,punctuation,digits]
    opt=input("uzunluk belirtmek ister misiniz? (yes or no)")
    if opt =='Yes':
        lent=input("Şifre uzunluğu ne kadar olsun: ")
        for _ in range(len(lent)):
            pwd+=rnd.choice(rnd.choice(liste))
    else:
        for _ in range(15):
            pwd+=rnd.choice(rnd.choice(liste))
    if pwd not in ascii_lowercase and ascii_uppercase and punctuation and digits:
        return pwd
    else:
        passwordfunc ()



print(passwordfunc ())
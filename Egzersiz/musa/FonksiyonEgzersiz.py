from string import ascii_lowercase,ascii_uppercase,punctuation,digits
print(ascii_lowercase,ascii_uppercase,punctuation,digits) 
# abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 0123456789
import random as rnd
print(rnd.choice(ascii_lowercase))
"""
yukarıdaki kodlardan yardım alarak belirtilen uzunlukta aşağıdaki kurallara uygun şifre üreten bir fonksiyon yazınız
1. en az bir büyük harf
2. en az bir küçük harf
3. en az bir noktalama işareti
4. en az bir rakam 
5. karakter sınırı parametre olarak alınabilir
"""

def passwordKontrol(password,uzunluk=8):
    kharf = bharf = rakam = noktalama = False
    if len(password) == uzunluk:
        
        for item in password:
            if item.isalpha():
                if item.isupper():
                    bharf = True
                else:
                    kharf = True
            elif item.isdigit():
                rakam = True
            elif item in punctuation:
                noktalama = True
    return kharf and bharf and rakam and noktalama


def passwordGen(uzunluk = 8):
    liste = [ascii_lowercase,ascii_uppercase,punctuation,digits]
    sonuc = ""
    sifre = ""
    while not passwordKontrol(sifre,uzunluk):
        if len(sonuc) == uzunluk:
            sifre = sonuc
            sonuc = ""
            continue
        else:
            sonuc += rnd.choice(rnd.choice(liste))
    else:
        return sifre


print(passwordGen(12))
        

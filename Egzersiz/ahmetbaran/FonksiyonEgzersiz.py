from string import ascii_lowercase,ascii_uppercase,punctuation,digits
print(ascii_lowercase,ascii_uppercase,punctuation,digits) 
# abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 0123456789
import random as rnd
"""
yukarıdaki kodlardan yardım alarak belirtilen uzunlukta aşağıdaki kurallara uygun şifre üreten bir fonksiyon yazınız
1. en az bir büyük harf
2. en az bir küçük harf
3. en az bir noktalama işareti
4. en az bir rakam 
5. karakter sınırı parametre olarak alınabilir
"""

def getPassLen():
    return 8
    # return int(input('uzunluk:'))


def checkPass(password):
    lowercase = uppercase = punc = digit = False
    if len(password) < getPassLen():
        return False
    for letter in password:
        if letter in ascii_lowercase:
            lowercase = True
        if letter in ascii_uppercase:
            uppercase = True
        if letter in punctuation:
            punc = True
        if letter in digits:
            digit = True

    return lowercase and uppercase and punc and digit


def generatePass():
    chars = [ascii_lowercase,ascii_uppercase,punctuation,digits]
    password = ''
    while not checkPass(password):
        if len(password) == getPassLen():
            password = ''
        else:
            password += rnd.choice(rnd.choice(chars))
    else:
        return password

print(generatePass()) 

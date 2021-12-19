"""
yukarıdaki kodlardan yardım alarak belirtilen uzunlukta aşağıdaki kurallara uygun şifre üreten bir fonksiyon yazınız
1. en az bir büyük harf
2. en az bir küçük harf
3. en az bir noktalama işareti
4. en az bir rakam 
"""

from string import ascii_lowercase, ascii_uppercase, punctuation, digits
import random as rnd


def generatePass(length):

    _all = ascii_letters + ascii_lowercase + ascii_uppercase + punctuation + digits

    created = "".join(rnd.choice(_all) for i in range(length))

    for each in created:
        if each not in ascii_letters and ascii_lowercase and ascii_uppercase and punctuation and digits:
            created = "".join(rnd.choice(_all) for i in range(length))

    print(created)


generatePass(10)
    
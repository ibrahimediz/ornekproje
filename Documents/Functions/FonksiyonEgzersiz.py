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
from string import ascii_lowercase,ascii_uppercase,punctuation,digits
# abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 0123456789
import random as rnd


# "n 5 olsun diyelim"
liste = [ascii_lowercase,ascii_uppercase,punctuation,digits]
n = int(input("Kaç haneli password istersin?: "))

password = ""

birinci = rnd.choice(ascii_uppercase)
ikinci = rnd.choice(ascii_lowercase)
üçüncü = rnd.choice(punctuation)
dördüncü = rnd.choice(digits)

sonuncu = ""
sonuc = 0
while sonuc < n-4:    
    sonuncu += (rnd.choice(rnd.choice(liste)))
    sonuc += 1
# rnd.sh
password = birinci + ikinci + üçüncü + dördüncü + sonuncu
print(password)
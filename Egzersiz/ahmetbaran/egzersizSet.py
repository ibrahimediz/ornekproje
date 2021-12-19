"""
iki açısı girilmiş olan bir üçgenin açılara göre türünü ekrana yazdıran python programını yazınız
45,45  45,90  1. İkizKenar Üçgen Dik Üçgen
60,60         2. Eşkenar Üçgen
90,25         3. Dik üçgen
120,41        4. Çeşit Kenar
"""

angles = [30,30]
#angles = [60,60]

angles.append(180-sum(angles))

if len(set(angles)) == 1:
    print('Eskenar')
elif len(set(angles)) == 2:
    print('Ikizkenar')
else: print('Cesitkenar')


"""girilen bir metin içerisindeki karakterlerin sayılarını ekrana sözlük şeklinde döken bir python kodu"""

text = 'afyonkarahisarlilastiramadiklarimizdanmisiniz'

letterCount = {}

for letter in text:
    if letter not in letterCount:
        if letter == ' ':
            letterCount['space'] = 1
        else:
            letterCount[letter] = 1
    else:
        if letter == ' ':
            letterCount['space'] = letterCount['space'] + 1
        else:
            letterCount[letter] = letterCount[letter] + 1

print(letterCount)

sozluk = {x:text.count(x) for x in text} # !!!!!!!
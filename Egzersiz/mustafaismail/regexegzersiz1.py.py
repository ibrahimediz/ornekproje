"""test_string = "123qwe678 -ABC91011- vyz"
yukarıdaki metinden re modülünü kullanarak
1. kaç digit olduğunu
2. kaç harf olduğunu
3. harf ya da digit olmayan karakter sayısını
4. vyz ile bittiğini düşünerek vyz nin konumunu ekrana yazdıran programı yazınız"""

import re

#1.
test_string = "123qwe678 -ABC91011- vyz"

pattern = re.compile(r'\d')
digits = re.finditer(pattern, test_string)
print(len([*digits]))


# 2.

pattern = re.compile(r'\w')
characters = re.finditer(pattern, test_string)
print((len([*characters])))

#3.
pattern = re.compile(r'[^\w\d]')

non_characters = re.finditer(pattern, test_string)
print((len([*non_characters])))



#4.
pattern = re.compile(r'vyz$')
vyz = re.finditer(pattern, test_string)
print(*vyz)



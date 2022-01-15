'''test_string = "123qwe678 -ABC91011- vyz"
yukarıdaki metinden re modülünü kullanarak
1. kaç digit olduğunu
2. kaç harf olduğunu
3. harf ya da digit olmayan karakter sayısını
4. vyz ile bittiğini düşünerek vyz nin konumunu ekrana yazdıran programı yazınız'''

import re

test_string = "123qwe678 -ABC91011- vyz"

count = len(re.findall(r"\d", test_string))
print(f'Digit: {count}')

count = len(re.findall(r'[a-z,A-Z]', test_string))
print(f'Digit: {count}')

count = len(re.findall(r'\W', test_string))
print(f'Digit: {count}')

print("vyz",re.search(r"vyz$",test_string).span())
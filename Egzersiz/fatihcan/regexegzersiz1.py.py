"""
test_string = "123qwe678 -ABC91011- vyz"
yukarıdaki metinden re modülünü kullanarak
1. kaç digit olduğunu
2. kaç harf olduğunu
3. harf ya da digit olmayan karakter sayısını
4. vyz ile bittiğini düşünerek vyz nin konumunu ekrana yazdıran programı yazınız
"""
import re
test_string = "123qwe678 -ABC91011- vyz"
digit = re.findall('[0-9]', test_string)
print(len("".join(digit)))




# yukarıdaki metinden re modülünü kullanarak
# 1. kaç digit olduğunu
# 2. kaç harf olduğunu
# 3. harf ya da digit olmayan karakter sayısını
# 4. vyz ile bittiğini düşünerek vyz nin konumunu ekrana yazdıran programı yazınız
import re

test_string = "123qwe678 -ABC91011- vyz"

result1 = re.findall('\d', test_string)
print(len(result1))

result2 = re.findall("\w", test_string)
print(len(result2))

result3 = re.findall("\W", test_string)
print(len(result3))

result4 = re.search("vyz$", test_string).span()
print(result4)
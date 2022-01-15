# yukarıdaki metinden re modülünü kullanarak
# 1. kaç digit olduğunu
# 2. kaç harf olduğunu
# 3. harf ya da digit olmayan karakter sayısını
# 4. vyz ile bittiğini düşünerek vyz nin konumunu ekrana yazdıran programı yazınız

import re

test_string = "123qwe678 -ABC91011- vyz"
x  = re.findall(r'\d+', test_string)
print(x)
regex = r"(?<![\"=\w])(?:[^\W_]+)(?![\"=\w])"

matches = re.finditer(regex, test_string)

for matchNum, match in enumerate(matches):
    print (match.group())

    
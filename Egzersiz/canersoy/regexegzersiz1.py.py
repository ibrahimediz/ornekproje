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

pattern = r"\d" #no of digits
print(len(re.findall(pattern, test_string)))

pattern = "[a-zA-Z]" #no of letters
print(len(re.findall(pattern, test_string)))

pattern = r"\W" #no of non-digit and non-letters
print(len(re.findall(pattern, test_string)))

#position of vyz
print(re.search("vyz", test_string))
print(*re.finditer("vyz", test_string)) #teşekkürler Baran :)

pattern = "[ ]" #no of whitespace
print(len(re.findall(pattern, test_string)))



test_string = "123qwe678 -ABC91011- vyz"
# yukarıdaki metinden re modülünü kullanarak
# 1. kaç digit olduğunu
# 2. kaç harf olduğunu
# 3. harf ya da digit olmayan karakter sayısını
# 4. vyz ile bittiğini düşünerek vyz nin konumunu ekrana yazdıran programı yazınız
#
# Answers
# print("Kaç digit var",len(list(re.finditer(r"\d",test_string))))
# print("Kaç harf ya da digit var",len(list(re.finditer(r"\w",test_string))))
# print("Kaç harf ya da digit olmayan karakter var",len(list(re.finditer(r"\W",test_string))))
# print("vyz",re.search(r"vyz$",test_string).span())


import re

#1
count_digit = len(list(re.finditer(r'\d', test_string))) 
print("Digit: ",count_digit)

#2
count_chars = len(list(re.finditer(r'\w', test_string))) 
print("Digit: ",count_chars)


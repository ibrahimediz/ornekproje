import re

test_string = "123qwe678 -ABC91011- vyz"
#1. kaç digit olduğunu
print(r"\d", *re.finditer(r"\d", test_string), sep="\n")

#2. kaç harf olduğunu

print(r"\w",*re.finditer(r"\w", test_string),sep="\n")

#3. harf ya da digit olmayan karakter sayısını

print(r"\W",*re.finditer(r"\W", test_string),sep="\n")

#4. vyz ile bittiğini düşünerek vyz nin konumunu ekrana yazdıran programı yazınız

print(r"\b",*re.finditer(r"\bvyz", test_string),sep="\n")
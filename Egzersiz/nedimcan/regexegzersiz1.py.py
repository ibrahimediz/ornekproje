"""test_string = "123qwe678 -ABC91011- vyz"
yukarıdaki metinden re modülünü kullanarak
1. kaç digit olduğunu
2. kaç harf olduğunu
3. harf ya da digit olmayan karakter sayısını
4. vyz ile bittiğini düşünerek vyz nin konumunu ekrana yazdıran programı yazınız"""

import re

test_string = "123qwe678 -ABC91011- vyz"

def rgx(string):
    digit_ = len(re.findall(r"\d", test_string))
    letter = len(re.findall(r"[A-Za-z]", test_string))
    nor_both = len(re.findall(r"\W", test_string))
    find_vyz = re.search(r"vyz", test_string) 

    return f"Digit: {digit_}, Letter: {letter}, Nor Both: {nor_both}, VYZ: {find_vyz}"

print(rgx(test_string))

"""
Ibrahim hocanin cozumu

import re
test_string = "123qwe678 -ABC91011- vyz"
print("Kaç digit var",len(list(re.finditer(r"\d",test_string))))
print("Kaç harf ya da digit var",len(list(re.finditer(r"\w",test_string))))
print("Kaç harf ya da digit olmayan karakter var",len(list(re.finditer(r"\W",test_string))))
print("vyz",re.search(r"vyz$",test_string).span())



"""
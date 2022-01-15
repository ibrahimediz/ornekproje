import re
test_string = "123qwe678 -ABC91011- vyz"

"""yukarıdaki metinden re modülünü kullanarak
1. kaç digit olduğunu
2. kaç harf olduğunu
3. harf ya da digit olmayan karakter sayısını
4. vyz ile bittiğini düşünerek vyz nin konumunu ekrana yazdıran programı yazınız"""

print(len(list(re.finditer(r'\d',test_string))))
print(len(list(re.finditer(r'\w',test_string))))
print(len(list(re.finditer(r'\W',test_string)))) 
print(len(list(re.finditer(r'\bvyz',test_string))))


for i in re.finditer("vyz", test_string):
    print(i.span())

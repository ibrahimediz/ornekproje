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
#1. kaç digit olduğunu
print("1-",len(list(re.findall(r'\d+',test_string))))
#2. kaç harf olduğunu
print("2-",len(list(re.finditer(r'\w',test_string))))
#3. harf ya da digit olmayan karakter sayısını
print(len(list(re.finditer())))
#1. kaç digit olduğunu
print("Kaç digit var",len(list(re.finditer(r"\d",test_string))))
#2. kaç harf olduğunu
print("Kaç harf ya da digit var",len(list(re.finditer(r"\w",test_string))))
#3. harf ya da digit olmayan karakter sayısını
print("Kaç harf ya da digit olmayan karakter var",len(list(re.finditer(r"\W",test_string))))
#4. vyz ile bittiğini düşünerek vyz nin konumunu ekrana yazdıran programı yazınız
print("vyz",re.search(r"vyz$",test_string).span())
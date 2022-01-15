import re
test_string = "123qwe678 -ABC91011- vyz"
print(len(list(re.finditer(r"\d", test_string))))
print(len(list(re.finditer(r"\w", test_string))))
print(len(list(re.finditer(r"\W", test_string))))
print(*re.finditer(r"\bvyz", test_string))
import re

pw = input()
pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%.*#?&])[A-Za-z\d@$!#%.*?&]{10,20}$"
match = re.compile(pattern)

if re.search(match, pw):
    print("valid")
else:
    print("not valid")
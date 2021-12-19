# find occurence
txt=input('Enter : ')
# convert input to list
list_txt=[i for i in txt]
# drop repetitive values
set_txt=set(list_txt)
# record occurences
occurence=dict()
for item in list(set_txt):
    occurence[item]=list_txt.count(item)

print(occurence)

## 
from string import ascii_lowercase,ascii_uppercase,punctuation,digits
print(ascii_lowercase,ascii_uppercase,punctuation,digits) 
# abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 0123456789
import random as rnd
def generate_password(length_pwd:int)->str:
    pass

import re

testString = '123abc456789abc123ABC'

pattern = re.compile(r'abc')

matches = pattern.finditer(testString)

for i in matches:
    x,y = i.span()
    print(x,y)
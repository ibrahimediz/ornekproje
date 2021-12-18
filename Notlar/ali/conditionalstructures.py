"""
if, elif, else, pass
"""
a=2
if a % 2 > 0:
    print("çift")
else:
    print("tek")

a = 0 # null 
b= "" # null
c = []
d = ()
e = {}
if c:
    print("boş")
else:
    print("dolu")

a=5
if a % 2 > 0 : print("tek")
sonuc = "tek" if a % 2 > 0 else "çift"
print(sonuc)

notu = 75

if 85 >= notu <= 100:
    print("AA")
elif 70 >= notu <= 84:
    print("BB")

# operators
"""
1. logical operator --  and  or   not
2. assignment operator --  =
3. aritmetic operators --  + * - / // % **
4. unary operators -- += *= /=
5. membership operators -- in  not in
6. identity operator -- is  is not
7. comparison operators -- < > <= >= == !=
"""
# precedence 
# https://www.programiz.com/python-programming/precedence-associativity

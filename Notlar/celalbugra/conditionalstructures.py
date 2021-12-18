"""
indetation - blockları belirlemede yardımcı olur
varsayılan olarak 4 
if
elif
else
"""



# # bir değerin boş olma ihtimali kontrolü
# a = 0
# b = ""
# c = []
# d = ()
# e = {}
# if c:
#     print("Dolu")
# else:
#     print("Bos")
# # asycı değerleri karşılaştırır
# var1 = "Ali"   # A => 65
# var2 = "ali" # a => 97

# a = 5
# if a % 2 > 0 : print("Tek")
# sonuc = "Tek" if a % 2 > 0 else "Çift"
# print(sonuc)

# """
# AA 85 100
# BB 70 84
# CC 60 70
# """
# notu = 75
# if 85 >= notu <= 100:
#     print("AA")
# elif 70 >= notu <= 84:
#     print("BB")
# elif 60 >= notu < 70:

##########################
# operators
"""
1. Logical Operator and not
2. Assigment Operator = 
3. Arithmetic Op 
4. Unary Op +=,*=,/=
5. Bitwise Op & ^ | 
6. Membership OP
7. Identiy op is, is not
8. Comprasiob Op >,<
"""

# python oto 2'56 ya kadar verileri tutar
############ is

a = b = 385
if a is b:
    print("Doğru")
a = 385
b = 385
if a is b:
    print("Doğru")
else:
    print("Yanlış")

a = 1
b = 1.0
print(a == b) # True
print(a is b) # False

########## in
liste = [1,2,3,4]
if 2 in liste:
    print("içerdema")

# sözlükte key bazında bakar

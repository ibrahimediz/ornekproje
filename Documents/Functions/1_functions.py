"""
def 
return
parametre tanımı
"""

def fonk(): # tanımlama
    pass

fonk() # çağırma
a = 5
# def fonk(a,b):
#     print(a+b)

# fonk(b=3,a=2)

def fonk(a,b=0): # non-default argument follows default argument
    print(a)
    if b:
        print(a+b)
fonk(2)
fonk(2,3)
print(type(fonk)) # "<class 'function'>"
print(type(fonk(2,3))) # <class 'NoneType'>
a = fonk(2,3)
print(a) #  None
############################### return 
def fonk(a,b):
    return a+b
sonuc = fonk(1,2)
print(sonuc)
print(fonk(fonk(1,2),fonk(3,4)))


print(type(fonk)) # "<class 'function'>"
print(type(fonk(2,3))) # <class 'int'>
print(type(fonk("2","3"))) # <class 'str'>

def fonk(a,b):
    return a,b,a+b
print(type(fonk("2","3"))) # <class 'tuple'> # 2,3,5
sonuc = "{0} + {1} = {2}".format(*fonk(2,3))
print(sonuc)


def fonk(a,b):
    return a,b,a+b
    print("ÇALIŞMAZ")
print(type(fonk("2","3"))) # <class 'tuple'> # 2,3,5
sonuc = "{0} + {1} = {2}".format(*fonk(2,3))
print(sonuc)
#################### str format açıklama
#### 1
# var1 = "Merhaba %s" %"ibrahim"
# print(var1)
# #### 2
# var1 = "Merhaba {0}".format("ibrahim")
# #### 3
# isim = "ibrahim"
# var1 = f"Merhaba {isim}"
# # "\" #escape sequence
# var1 = 'Ankara\'da'
# var1 = '\n\b\a\t'
# # "ali;veli;123123\n"
# var1 = "C:\talat\nalan\birgun.html"
# print(var1)
# var1 = r"C:\talat\nalan\birgun.html"
# sayi = 2
# var1 = fr"C:\talat\nalan\birgun{sayi}.html"
# print(var1)
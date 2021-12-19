"""
def 
return 
parametre
"""

# def fonk(): # fonksiyon tanımlama
#     pass

# fonk() # fonk çağırma

# def fonk(a,b):
#     print(a+b)

# fonk(2, 3)

# fonk(b=3, a=2)

# def fonk(a:int,b:int) -> None:
#     pass


# default tanımlama
# ****
# non-default argument follows default argument
# ****

def fonk(a,b=0):
    print(a)
    if b:
        print(a+b)

fonk(2)
fonk(2,3)
# her fonksiyonun bir tipi vardır
print(type(fonk)) # class func
print(type(fonk(2,3))) # NoneType

a = fonk(2,3)
print(a) # None
###################### return
def fonk(a,b):
    return a+b

sonuc = fonk(1,2)
print(sonuc)

# tuple döner

def fonk(a,b):
    return a,b,a+b
print(type(fonk("2","3"))) # tuple (2,3,5)
sonuc = "{} + {1} = {2}".format(*fonk(2,3))

# ekbilgi - str formatlama
# s string olduğunu gösterir 

#### 1 
var1 = "Merhaba %s" %"İbrahim"
print(var1)
#### 2
var1 = "Merhaba {}".format("İbrahim")
#### 3
isim = "İbrahim"
var1 = f"Merhaba {isim}"

# "\" espace sequence
var1 = 'Ankara\'da'
var1 = '\n\b\a\t'


#  r ile row string haline getirebiliriz
var1 = "c:\talat\nalan\birgün.html"
print(var1)
var1 = r"c:\talat\nalan\birgün.html"
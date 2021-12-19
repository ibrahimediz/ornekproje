a = 5
def fonk(a,b):
    print(a+b)

fonk(b=3,a=2)

#def fonk(a,b=0,c): # non-default argument follows default argument
def fonk(a, b=0):
    print(a)
    if b:
        print(a+b)
fonk(2)
fonk(2,3)


var1 = "Merhaba %s" %"ibrahim"
print(var1)
#### 2
var1 = "Merhaba {0}".format("ibrahim")
#### 3
isim = "ibrahim"
var1 = f"Merhaba {isim}"
# "\" #escape sequence

var1 = r"C:\talat\nalan\birgun.html"
sayi = 2
var1 = fr"C:\talat\nalan\birgun{sayi}.html"
print(var1)


def fonk(a,b):
    return a,b,a+b
print(type(fonk("2","3"))) # <class 'tuple'> # 2,3,5
sonuc = "{0} + {1} = {2}".format(*fonk(2,3)) # unpack operator sayesinde !!!!!!!!!!!
print(sonuc)


def fonk(*args):
    print(type(args))

fonk()
fonk(1,2)
fonk(1,2,3,"4",3,2,1,1,2)
def fonk(*args):
    sonuc = 0
    for item in liste:
        if isinstance(item,int) : sonuc += item
    return sonuc

def fonk(*args):
    return sum([i for i in args if isinstance(i, int)])

def bizimRange(sayi):
    adim = 0
    while adim < sayi:
        yield adim
        adim += 1

print(type(bizimRange(5))) # <class 'generator'>
print(bizimRange(5)) # <generator object bizimRange at 0x7f72aa421ba0>
for i in bizimRange(6):
    print(i)

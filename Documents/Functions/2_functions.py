"""
*args
**kwargs
yield
"""
# def fonk(*args):
#     print(type(args))

# fonk()
# fonk(1,2)
# fonk(1,2,3,"4",3,2,1,1,2)
# def fonk(*args):
#     sonuc = 0
#     for item in liste:
#         if isinstance(item,int) : sonuc += item
#     return sonuc

# def fonk(*args):
#     return sum([i for i in args if isinstance(i, int)])

# liste = [1,2,3,2,2,1,1,]
# print(fonk(*liste))

def fonk(**kwargs):
    print(type(kwargs))

fonk()
fonk(param1="Jamiryo",param2="Deneme")


# sozluk = {"1":"Bir",
# "2":"iki"}
# print(sozluk.items()) #[('1', 'Bir'), ('2', 'iki')]
# for key,value in sozluk.items():
#     print(key,value)
##################################### kwargs
# a,b,c ="ali"
# print(a,b,c)

# def fonk(**kwargs):
#     for key,value in kwargs.items():
#         if key == "Selam":
#             print("Merhaba",value)
#         if key == "hal":
#             print("Nasılsın",value)

# fonk(Selam="YemekSepeti",hal="İbrahim")
# fonk(Selam="YemekSepeti")
# fonk(hal="İbrahim")
# fonk()

# def fonk(a,b,*args,**kwargs):
#     print(a,b)
#     print(args)
#     print(kwargs)

# fonk(1,2,3,4,5,6,7,8,deneme=123)
# from typing import Union
# def fonk(a:Union(int,str)):

# def fonk(a,b,/,c,d,*,e,f):
#     print(a,b,c,d,e,f)


# fonk(1,2,3,4,e=2,f=3)


############################# yield
# print(type(range(1,2)))
# def bizimRange(sayi):
#     adim = 0
#     while adim < sayi:
#         yield adim
#         adim += 1

# print(type(bizimRange(5))) # <class 'generator'>
# print(bizimRange(5)) # <generator object bizimRange at 0x7f72aa421ba0>
# for i in bizimRange(6):
#     print(i)
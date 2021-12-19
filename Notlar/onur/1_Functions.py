# var_1 = r"C:\Program Files\...."

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

# liste = [1,2,3,2,2,1,1,]
# print(fonk(*liste))

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

#######################Yield##################
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

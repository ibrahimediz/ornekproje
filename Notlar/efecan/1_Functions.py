# def fonk(a,b):
#     return a,b,a+b
# print(type(fonk("2","3"))) # <class 'tuple'>
#########################
# def fonk(a,b):
#     return a,b,a+b
# sonuc = "{0} + {1} = {2}".format(*fonk(2,3)) # <class 'tuple'> # 2,3,5
# print(sonuc)
##########################

#################### str format açıklama
#### 1
# var1 = "Merhaba %s" %"ibrahim"
# print(var1)
# #### 2
# var1 = "Merhaba {0}".format("ibrahim")
# #### 3
# isim = "ibrahim"
# var1 = f"Merhaba {isim}"


##################
# # "\" #escape sequence
# var1 = 'Ankara\'da'
# var1 = '\n\b\a\t'
# # "ali;veli;123123\n"
# var1 = "C:\talat\nalan\birgun.html"
# print(var1)
# var1 = r"C:\talat\nalan\birgun.html"

##################################################
#birden fazla veriyi yollamak için
# def fonk(*args): #--> basında yıldız olduğu için hepsini tuple olarak alır
#     print(type(args))

# fonk()
#aynı kod
# def fonk(*args):
#     return sum([i for i in args if isinstance(i, int)])
##################################################
# """ **kwargs yolladığımız argumantları fonksiyona
# key value ilişkisiyle yollar"""

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
#############################################
# def fonk(a,b,*args,**kwargs):
#     print(a,b)
#     print(args)
#     print(kwargs)

# fonk(1,2,3,4,5,6,7,8,deneme=123)

#üçünü aynı fonksiyonda kullanma
###########################################

#yıldızdan (*) sonrasında parametre adı belirtilmeli
# slaştan (/) sonra belirtmeye gerek yık

# def fonk(a,b,/,c,d,*,e,f):
#     print(a,b,c,d,e,f)


# fonk(1,2,3,4,e=2,f=3)
#############################################

#yeild fonksiyon tipini generator yapıyor
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
###############################################
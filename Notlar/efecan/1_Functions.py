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

# nonlocal ---> bir üst
# global ----> en dışarıdaki değeri değişirir

###############################################
#                       lambda          #
# def fonk(x):
#     return x**2

# fonk = lambda x:x**2  ---> iki fonksiyonda aynı

# liste = ["ayşe","şermin","çisem","ışıl","ibrahim","şahan","sevil","beril"]
# liste.sort()
# print(liste) # ['ayşe', 'beril', 'ibrahim', 'sevil', 'çisem', 'ışıl', 'şahan', 'şermin']
# alfabe = "abcçdefghıijklmnoöprsştuüvyz"
# cevrim = {x:alfabe.index(x) for x in alfabe }
# print(sorted(liste,key=lambda x:cevrim.get(x[0]))) # ['ayşe', 'beril', 'çisem', 'ışıl', 'ibrahim', 'sevil', 'şahan', 'şermin']

####################  bulidin  #################

# map --> bir fonsitonu liste'ye uygulamak için kullanılır

# sayilar = "000012123123"
# liste = list(sayilar)
# liste = list(map(int,liste)) ---> int(liste[i]) ayını şey
         
#                       örnek
# print(map(lambda x:x**2,liste)) # <map object at 0x7fc77c746eb0>
# print(*map(lambda x:x**2,liste)) # 1 4 9 16

################### filter #####################3

# liste = [1,2,3,2,2,3,2,1,1,2,2,23,34,231,12,123,34,45,4,6]
# liste = list(filter(lambda x:x>10,liste))
# print(liste)

# liste = [1,2,3,2,2,"3",2,1,1,2,2,23,"34","231","12","123",34,45,4,6]
# liste = list(filter(lambda x:not isinstance(x, str),liste))
# print(liste)
############### dict update #####################
# sozluk = {}
# sozluk = {"1":"Bir","2":"iki"}
# sozluk2 = {"1":"Uno","2":"Dos","3":"Tres"}
# sozluk.update([("2","Two")])
# print(sozluk)
######################## zip ####################

# liste1 = ["A1","A2","A3","A4"]
# liste2 = [20,50,40] 
# print(*zip(liste1,liste2)) # ('A1', 20) ('A2', 50) ('A3', 40)
# sozluk = {}
# sozluk.update(zip(liste1,liste2))
# print(sozluk)

######################## unzip ####################
#print(*zip(*zip(liste1,liste2))) # ('A1', 'A2', 'A3') (20, 50, 40)

####################### enumerate ###################

# liste1 = ["A1","A2","A3","A4"]
# print(*enumerate(liste1)) #(0, 'A1') (1, 'A2') (2, 'A3') (3, 'A4')
# for _id,value in enumerate(liste1):
#     print(f"{_id}:{value}")

####################### all any #####################

# all ---> tamammı doğruysa true döner

# a = ""
# if a:
#     print("Dolu")
# else:
#     print("Boş")
# liste1 = ["",0,[]]
# liste2 = ["1",1,[1,]]
# print(all(liste1))
# print(all(liste2))

#any ---> en azından biri doğru olursa true döner 

# a = ""
# if a:
#     print("Dolu")
# else:
#     print("Boş")
# liste3 = ["",0,[1,]]
# print(any(liste3))

##########################################

# exec --> içine aldığı kodu python yorumlayıcıya alır ve çalıştırır 

# eval --> ("a+3") gibi matematiksel işlemleri yapar

##########################################


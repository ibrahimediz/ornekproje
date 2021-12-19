"""
lambda
global
nonlocal
recursion
built-ins
"""
######################
# a = 5
# def fonk():
#     a =3
#     print("1. Fonksiyonun içinden:",a)

# print("1. Dışardan:",a)
# fonk()
# print("2. Dışarıdan:",a)
# """
# 1. Dışardan: 5
# 1. Fonksiyonun içinden: 3
# 2. Dışarıdan: 5
# """
######################
# a = 5 
# def fonk():
#     global a 
#     a = 3
#     print("1. Fonksiyonun içinden:",a)

# print("1. Dışardan:",a)
# fonk()
# print("2. Dışarıdan:",a)
# """
# 1. Dışardan: 5
# 1. Fonksiyonun içinden: 3
# 2. Dışarıdan: 3
# """
##########################################
# a = 5
# def fonk():
#     a = 3
#     print("1. Fonksiyonun içinden:",a)
#     def icFonk():
#         global a 
#         a = 8
#         print("1. İç Fonk:",a)
#     icFonk()
#     print("2. Fonksiyonun içinden:",a)

# print("1. Dışardan:",a)
# fonk()
# print("2. Dışarıdan:",a)
# """
# 1. Dışardan: 5
# 1. Fonksiyonun içinden: 3
# 1. İç Fonk: 8
# 2. Fonksiyonun içinden: 3
# 2. Dışarıdan: 8
# """
#####################################

# a = 5
# def fonk():
#     a = 3
#     print("1. Fonksiyonun içinden:",a)
#     def icFonk():
#         nonlocal a 
#         a = 8
#         print("1. İç Fonk:",a)
#     icFonk()
#     print("2. Fonksiyonun içinden:",a)

# print("1. Dışardan:",a)
# fonk()
# print("2. Dışarıdan:",a)
# """
# 1. Dışardan: 5
# 1. Fonksiyonun içinden: 3
# 1. İç Fonk: 8
# 2. Fonksiyonun içinden: 8
# 2. Dışarıdan: 5
# """

#####################################
# def fonk(x):
#     return x**2

# fonk = lambda x:x**2
# liste = ["ayşe","şermin","çisem","ışıl","ibrahim","şahan","sevil","beril"]
# liste.sort()
# print(liste) # ['ayşe', 'beril', 'ibrahim', 'sevil', 'çisem', 'ışıl', 'şahan', 'şermin']
# alfabe = "abcçdefghıijklmnoöprsştuüvyz"
# cevrim = {x:alfabe.index(x) for x in alfabe }
# print(cevrim)
# """
# {'a': 0, 'b': 1, 'c': 2, 'ç': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 
# 'ı': 9, 'i': 10, 'j': 11, 'k': 12, 'l': 13, 'm': 14, 'n': 15,
# 'o': 16, 'ö': 17, 'p': 18, 'r': 19, 's': 20, 'ş': 21, 
# 't': 22, 'u': 23, 'ü': 24, 'v': 25, 'y': 26, 'z': 27}
# """
# print(sorted(liste,key=lambda x:cevrim.get(x[0]))) # ['ayşe', 'beril', 'çisem', 'ışıl', 'ibrahim', 'sevil', 'şahan', 'şermin']

################################### recursion
# def reco(metin):
#     if len(metin) == 1:
#         print(metin)
#     else:
#         print(metin)
#         reco(metin[1:])

# reco("Yemeksepeti")


# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(6000)
# print(sys.getrecursionlimit())


# def faktoriyel(sayi):
#     sonuc = 1
#     for i in range(1,sayi+1):
#         sonuc *= i
#     return sonuc

# print(faktoriyel(6))

# def faktoriyelreco(sayi):
#     if sayi == 1:
#         return 1
#     else:
#         return sayi * faktoriyelreco(sayi-1)
    
# print(faktoriyelreco(6))


##################################### builtins
"""
map
filter
zip
enumerate
all,any
eval,exec
sorted
reversed
ord
chr
"""
# sayilar = "000012123123"
# liste = list(sayilar)
# liste = list(map(int,liste))
# liste = [1,2,3,4]
# print(map(lambda x:x**2,liste)) # <map object at 0x7fc77c746eb0>
# print(*map(lambda x:x**2,liste)) # 1 4 9 16

# liste = [1,2,3,2,2,3,2,1,1,2,2,23,34,231,12,123,34,45,4,6]
# liste = list(filter(lambda x:x>10,liste))
# print(liste)

# liste = [1,2,3,2,2,"3",2,1,1,2,2,23,"34","231","12","123",34,45,4,6]
# liste = list(filter(lambda x:not isinstance(x, str),liste))
# print(liste)

# sozluk = {}
# sozluk = {"1":"Bir","2":"iki"}
# sozluk2 = {"1":"Uno","2":"Dos","3":"Tres"}
# sozluk.update([("2","Two")])
# print(sozluk)

#######################zip

# liste1 = ["A1","A2","A3","A4"]
# liste2 = [20,50,40] 
# print(*zip(liste1,liste2)) # ('A1', 20) ('A2', 50) ('A3', 40)
# sozluk = {}
# sozluk.update(zip(liste1,liste2))
# print(sozluk)
# print(*zip(*zip(liste1,liste2))) # ('A1', 'A2', 'A3') (20, 50, 40)


############################# enumerate
# liste1 = ["A1","A2","A3","A4"]
# print(*enumerate(liste1)) #(0, 'A1') (1, 'A2') (2, 'A3') (3, 'A4')
# for _id,value in enumerate(liste1):
#     print(f"{_id}:{value}")
########################## all any
# a = ""
# if a:
#     print("Dolu")
# else:
#     print("Boş")
# liste1 = ["",0,[]]
# liste2 = ["1",1,[1,]]
# liste3 = ["",0,[1,]]
# print(all(liste1)) # False 
# print(all(liste2)) # True
# #######################
# print(all(liste1)) # False
# print(any(liste3)) # True
################################

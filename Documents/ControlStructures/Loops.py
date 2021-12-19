"""
* unpack operator
range
for
while
break
continue
else
"""
# liste = [1,2,3,4]
# print(liste,liste) # [1, 2, 3, 4] [1, 2, 3, 4]
# print(*liste,sep="-") # 1-2-3-4
# sozluk = {"1":"Bir","2":"İki"}
# print(*sozluk) # 1 2
############################## range
print("range(0,4)",*range(0,4))
print("range(4)",*range(4))
print("range(10,5,-1)",*range(10,5,-1))
print("range(5,12,2)",*range(5,12,2))
# ################################
# for i in range(4):
#     print(i)
# liste = [1,2,3,4,5]
#        0 1 2 3 4 
# for i in range(len(liste)):
#     print(liste[i])
# liste = [1,2,3,4,5,7]
# for item in liste:
#     print(item)
# print(item)


# for i in range(4):
#     i = i*8
#     print(i)
# print(i) # ???

# a = 0
# while a < 5:
#     print(a)
#     a += 1

##################################################
# for i in range(4):
#     i = i*8
#     print(i)
# else:
#     print("İyi Günler Dileriz")
# print(i) # ???

# a = 0
# while a < 5:
#     print(a)
#     a += 1
# else:
#     print("İyi Günler")
############################################ break
# for i in range(4):
#     if i == 1:
#         break
#     i = i*8
#     print(i)

# else:
#     print("İyi Günler Dileriz")
# print(i) # ???
# a = 0
# while a < 5:
#     print(a)
#     if a == 3:
#         break
#     a += 1
# else:
#     print("İyi Günler")
############################################# continue
# for i in range(4):
#     if i == 1:
#         continue
#     i = i*8
#     print(i)
# else:
#     print("İyi Günler Dileriz")
# print(i) # ???

# a = 0
# while a < 5:
#     a += 1
#     print(a)
#     if a == 3:
#         continue
# else:
#     print("İyi Günler")
############################################## 

sozluk = {x:x**2 for x in range(3)}
liste = [x for x in range(3)]
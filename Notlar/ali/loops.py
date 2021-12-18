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
# print(liste,liste)
# print(*liste,sep="-")

# sozluk = {"1":"Bir"}
# sozluk.get("1")
# sozluk["1"]
# sozluk.setdefault("2","iki")
# print(sozluk.keys())
# print(sozluk.values())
# print(sozluk.items())

# for i in range(4):
#     print(i)

# liste = [1,2,3,4]
# for i in range(len(liste)):
#     print(liste[i])

# for i in range(4):
#     if i == 1:
#         continue
#     i = i*8
#     print(i)
# else:
#     print("İyi Günler Dileriz")
# print(i) # ???

a = 0
while a < 5:
    a += 1
    print(a)
    if a == 3:
        continue
else:
    print("İyi Günler")

birler = {"0":"","1":" bir ",
"2":" iki ",
"3":" üç ",
"4":" dört ",
"5":" beş ",
"6":" altı ",
"7":" yedi ",
"8":" sekiz ",
"9":" dokuz "}
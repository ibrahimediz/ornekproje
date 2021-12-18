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

# #sep parametresi default /n tanımlıdır. 
# print(liste,liste)
# print(*liste) # tek tek ekrana basar

# sozluk = {"1":"Bir","2":"İki"}
# print(*sozluk) # 1 2

################## range
# range fonksiyonu generator bir fonkdur
print("range(10,5,-1)",*range(10,5,-1))
print("range(5,12,2)",*range(5,12,2))

###############
# dynamic tip tanımı 
# pythonda for each yapısı for yapısına gömülmüştür
for i in range(4):
    print(i)

liste = [1,2,3,4,5]

for i in range(len(liste)):
    print(liste[i])

# for ve while döngüden çıkmadan son kez kontrol eder.
# eğer koşul sağlanmıyosa false döner ve else koşulunu sağlar
# for i in range(4):
#     i = i *8
#     print(i)
# print(i)

# a = 0

# while a < 5:
#     print(a)
#     a +=1

for i in range(4):
    i = i *8
    print(i)
else:
    print("İyi günler")

####### break - döngü kırmak için kullanılır.
# break ile else aynı anda çalışmaz

##### contiune - belirli işlemi pas geçmeye yarar


# 3 tip hata çeşiti vardır 
# Base excep
# 
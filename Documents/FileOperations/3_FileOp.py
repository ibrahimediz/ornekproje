"""
csv
json
open
"""
"""
Text-Binary
"""
# /workspace/ornekproje/deneme.csv
# dosya = open("deneme.csv")
# print(dosya) # <_io.TextIOWrapper name='deneme.csv' mode='r' encoding='UTF-8'>
"""
r öntanımlı okuma
w yazma modu yazma dosya var ise siler
a ekleme modu yazma dosya yoksa oluşturur varsa sonuna kadar okur ve yazar
x oluşturma modu yazma dosya varsa hata verir yoksa oluşturur
r+,w+,a+,x+
"""
def dosyaAc(adres,param=0):
    from os import path
    mod = ""
    if path.exists(adres):
        mod = "a+" if param == 1 else "r+"
    else:
        mod = "w+"
    return open(adres,mod)

# dosya = dosyaAc("deneme.csv") # <_io.TextIOWrapper name='deneme.csv' mode='r+' encoding='UTF-8'>
# print(dosya)
"""
read => str <= int
readline => str <=int
readlines => list
------------------------------
write <= str
writelines <= list
------------------------------
flush()
close()
------------------------------
tell => int
seek <= int
------------------------------
"""
# print("1",dosya.read())
"""
ali;veli;123
deneme;deneme;1234
"""
# print(dosya.tell())
# print(dosya.seek(0))
# print("2",dosya.readline()) # ali;veli;123
# print(dosya.tell())
# print(dosya.seek(0))
# print("3",dosya.readlines()) #['ali;veli;123\n', 'deneme;deneme;1234\n']



# dosya = dosyaAc("heart.csv")
# for _id,item in enumerate(dosya.readlines()[1:6]):
#     print(f"{_id}:{item.split(',')}")



# dosya = dosyaAc("heart.csv",param=1)
# # dosya = open("heart.csv","a+")
# dosya.write("Jamiryo\n")
# dosya.close()

# with open(adres) as dos:
#     dos.read()

# with open("heart.csv") as d1, open("heart2.csv") as d2:
#     print(set(d2.readlines()).symmetric_difference(set(d1.readlines())))

# # open(adres,mod,encoding="UTF-8")
# print("Jamiryo",file=open("deneme.csv","a+"))


#unpack operator *
#in: [1, 2, 3, 4]
#out: 1 2 3 4

liste = [1, 2, 3, 4]
print(*liste) # 1 2 3 4

#sep="" alir, default bosluk
print(*liste, sep="-") # 1-2-3-4

sozluk = {"1":"Bir", "2":"Iki"}
print(*sozluk) #Key bazli unpack yapar

####
#range

print(*range(5))

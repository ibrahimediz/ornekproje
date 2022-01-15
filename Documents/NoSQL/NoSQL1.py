import pymongo 
cli = pymongo.MongoClient("mongodb+srv://dbuser:dbUser123@cluster0.6iawp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# print(*cli.list_database_names(),sep="\n")
db = cli["patika"]
print(*db.list_collection_names(),sep="\n")
col = db["153yemeksepeti"]


# # insert one
# veri = {"adi":"Taksim","soyadi":"Dayı","adres":"İstanbul"}
# sonuc = col.insert_one(veri)
# print(sonuc.inserted_id) # 61e275df16fb9806384dfef9




# listeVeri = [{"adi":"Taksim","soyadi":"Dayı","adres":"İstanbul"},
# {"adi":"Artiz","soyadi":"Dayı","adres":"Bazar","age":"65"},
# {"adi":"Möge","soyadi":"Apla","adres":"İstanbul"},
# {"adi":"Cihangir","soyadi":"Dayı","adres":"İstanbul"},
# {"adi":"1 Milyon Mehmet","soyadi":"Dayı","adres":"İstanbul"},
# ]


# sonuc = col.insert_many(listeVeri)
# print(*sonuc.inserted_ids,sep="\n")
"""
61e276456893b3b928e0e4ad
61e276456893b3b928e0e4ae
61e276456893b3b928e0e4af
61e276456893b3b928e0e4b0
61e276456893b3b928e0e4b1
"""

#id leri kendimiz verdik
listeVeri = {"1":{"id":1,"adi":"Taksim","soyadi":"Dayı","adres":"İstanbul"},
"2":{"id":2,"adi":"Artiz","soyadi":"Dayı","adres":"Bazar","age":"65"},
"3":{"id":3,"adi":"Möge","soyadi":"Apla","adres":"İstanbul"},
"4":{"adi":"Cihangir","soyadi":"Dayı","adres":"İstanbul"}}
def fonk(key,value):
    sozluk = {}
    sozluk["_id"] = key
    sozluk.update(value)
    return sozluk
print([fonk(key,value) for key,value in listeVeri.items()])

sonuc = col.insert_many([fonk(key,value) for key,value in listeVeri.items()])
print(*sonuc.inserted_ids,sep="\n")
"""
1
2
3
4
"""

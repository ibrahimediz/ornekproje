import pymongo 
cli = pymongo.MongoClient("mongodb+srv://dbuser:dbUser123@cluster0.6iawp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# print(*cli.list_database_names(),sep="\n")
db = cli["patika"]
# print(*db.list_collection_names(),sep="\n")
col = db["yemeksepeti"]
# veri = {"adi":"Taksim","soyadi":"Dayı","adres":"İstanbul"}
# sonuc = col.insert_one(veri)
# print(sonuc.inserted_id) # 61dac9791c01238612d829f4

# listeVeri = [{"adi":"Taksim","soyadi":"Dayı","adres":"İstanbul"},
# {"adi":"Artiz","soyadi":"Dayı","adres":"Bazar","age":"65"},
# {"adi":"Möge","soyadi":"Apla","adres":"İstanbul"},
# {"adi":"Cihangir","soyadi":"Dayı","adres":"İstanbul"},
# {"adi":"1 Milyon Mehmet","soyadi":"Dayı","adres":"İstanbul"},
# ]
# sonuc = col.insert_many(listeVeri)
# print(*sonuc.inserted_ids,sep="\n")



# listeVeri = [{"_id":1,"adi":"Taksim","soyadi":"Dayı","adres":"İstanbul"},
# {"_id":2,"adi":"Artiz","soyadi":"Dayı","adres":"Bazar","age":65},
# {"_id":3,"adi":"Möge","soyadi":"Apla","adres":"İstanbul"},
# {"_id":4,"adi":"Cihangir","soyadi":"Dayı","adres":"İstanbul"},
# {"_id":5,"adi":"1 Milyon Mehmet","soyadi":"Dayı","adres":"İstanbul"},
# ]
# sonuc = col.insert_many(listeVeri)
# print(*sonuc.inserted_ids,sep="\n")
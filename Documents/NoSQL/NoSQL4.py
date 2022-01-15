"""
update_one
update_many
"""
import pymongo 
cli = pymongo.MongoClient("mongodb+srv://dbuser:dbUser123@cluster0.6iawp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# print(*cli.list_database_names(),sep="\n")
db = cli["patika"]
# print(*db.list_collection_names(),sep="\n")
col = db["153yemeksepeti"]
### update_one
# sart = {"soyadi":"Dayı","id":{"$eq":2}}
# print("Başlangıç",*col.find(sart,{}),sep="\n")


# sart = {"soyadi":"Dayı","id":{"$eq":2}}
# veri = {"$set":{"adres":"Yozgat"}}
# sonuc = col.update_one(sart, veri)
# print(sonuc.modified_count)

# sart = {"soyadi":"Dayı","id":{"$eq":2}}
# print("Bitiş",*col.find(sart,{}),sep="\n")

######### update many

# col = db["153yemeksepeti"]
# sart = {"soyadi":"Dayı","id":{"$eq":2}}
# print("Başlangıç",*col.find(sart,{}),sep="\n")


# sart = {"soyadi":"Dayı","id":{"$eq":2}}
# veri = {"$set":{"adres":"Yozgat"}}
# sonuc = col.update_many(sart, veri)
# print(sonuc.modified_count)

# sart = {"soyadi":"Dayı","id":{"$eq":2}}
# print("Bitiş",*col.find(sart,{}),sep="\n")


# drop collection
db = cli["patika"]
# print(*db.list_collection_names(),sep="\n")
col = db["153yemeksepeti"]
col.drop()
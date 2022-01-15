"""
delete_one
delete_many
"""
import pymongo 
cli = pymongo.MongoClient("mongodb+srv://dbuser:dbUser123@cluster0.6iawp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# print(*cli.list_database_names(),sep="\n")
db = cli["patika"]
# print(*db.list_collection_names(),sep="\n")
col = db["153yemeksepeti"]

# delete_one
# sonuclar = col.find({"soyadi":"Dayı","adres":"İstanbul","_id":{"$eq":1}},{})
# print("Başlangıç",*sonuclar,sep="\n")

# sonuc = col.delete_one({"soyadi":"Dayı","adres":"İstanbul","_id":{"$eq":1}})
# print(sonuc.deleted_count)

# sonuclar = col.find({"soyadi":"Dayı","adres":"İstanbul","_id":{"$eq":1}},{})
# print("Bitiş",*sonuclar,sep="\n")

# delete_many
# sonuclar = col.find({"soyadi":"Dayı","adres":"İstanbul"},{})
# print("Başlangıç",*sonuclar,sep="\n")

# sonuc = col.delete_many({"soyadi":"Dayı","adres":"İstanbul"})
# print(sonuc.deleted_count)

# sonuclar = col.find({"soyadi":"Dayı","adres":"İstanbul"},{})
# print("Bitiş",*sonuclar,sep="\n")
import pymongo 
cli = pymongo.MongoClient("mongodb+srv://dbuser:dbUser123@cluster0.6iawp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# print(*cli.list_database_names(),sep="\n")
db = cli["patika"]
print(*db.list_collection_names(),sep="\n")
col = db["153_yemeksepeti"]

veri = {"adi":"Fatih","soyadi":"Terim","adres":"Sariyer","mahlas":"Imparator"}
col.insert_one(veri)
import pymongo 
cli = pymongo.MongoClient("mongodb+srv://dbuser:dbUser123@cluster0.6iawp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# print(*cli.list_database_names(),sep="\n")
db = cli["patika"]
print(*db.list_collection_names(),sep="\n")
col = db["153_yemeksepeti"]


yeni_veri = {"adi":"yilan","soyadi":"serdar","adres":"deepturkishweb"}

col.insert_one(yeni_veri)
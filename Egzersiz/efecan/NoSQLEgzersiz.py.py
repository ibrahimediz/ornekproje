import pymongo 
cli = pymongo.MongoClient("mongodb+srv://dbuser:dbUser123@cluster0.6iawp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cli["patika"]
print(*db.list_collection_names(),sep="\n")
col = db["153yemeksepeti"]

veri = {"adi":"Sezercik","soyadi":"undefined","adres":"acıların içinde","nasıl_abi":"Kıyak"}
col.insert_one(veri)
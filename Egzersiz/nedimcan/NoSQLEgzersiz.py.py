import pymongo 
cli = pymongo.MongoClient("mongodb+srv://dbuser:dbUser123@cluster0.6iawp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# print(*cli.list_database_names(),sep="\n")
db = cli["patika"]
print(*db.list_collection_names(),sep="\n")
col = db["153_yemeksepeti"]


# yukarıdaki kod bloğunu kullanarak 
# {"adi":"","soyadi":"","adres":""}  fieldları koleksiyona ekleyiniz, ek olarak bir field daha ekleyelim.

data = {"adi":"homeless","soyadi":"emanuel","adres":"tarla","ulke":"zimbabwe","yas":29}
col.insert_one(data)
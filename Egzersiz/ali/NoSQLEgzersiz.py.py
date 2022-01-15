import pymongo 
cli = pymongo.MongoClient("mongodb+srv://dbuser:dbUser123@cluster0.6iawp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# print(*cli.list_database_names(),sep="\n")
db = cli["patika"]
print(*db.list_collection_names(),sep="\n")
col = db["153yemeksepeti"]

# yukarıdaki kod bloğunu kullanarak 
row={"adi":"Ali","soyadi":"Mansur","adres":"Akıncılar","whoAdded":"AliMansur"}  #fieldları koleksiyona ekleyiniz, ek olarak bir field daha ekleyelim.
sonuc = col.insert_one(row)
# print(sonuc.inserted_id) 
import pymongo 
cli = pymongo.MongoClient("mongodb+srv://dbuser:dbUser123@cluster0.6iawp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# print(*cli.list_database_names(),sep="\n")
db = cli["patika"]
print(*db.list_collection_names(),sep="\n")
col = db["153_yemeksepeti"]


# yukarıdaki kod bloğunu kullanarak 
# fieldları koleksiyona ekleyiniz, ek olarak bir field daha ekleyelim.

data = {"adi":"Josep","soyadi":"Guardiola","adres":"Ingiltere", 'nickname':'Pep'}  
data = {"adi":"Gazinocular Krali","soyadi":"Alaattin","adres":"deep turkish web", 'genre':'Comedy'}  

# col.insert_one(data)

for i in col.find():
    print(i)
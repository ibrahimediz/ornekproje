import pymongo 
cli = pymongo.MongoClient("mongodb+srv://dbuser:dbUser123@cluster0.6iawp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# print(*cli.list_database_names(),sep="\n")
db = cli["patika"]
print(*db.list_collection_names(),sep="\n")
col = db["153yemeksepeti"]

data = {"adi":"Jamiryo","soyadi":"Guavara","adres":"Küba", "favorite":"Puro"}
insert_data = col.insert_one(data)
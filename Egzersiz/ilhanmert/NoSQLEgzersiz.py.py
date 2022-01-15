import pymongo 
cli = pymongo.MongoClient("mongodb+srv://dbuser:dbUser123@cluster0.6iawp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# print(*cli.list_database_names(),sep="\n")
db = cli["patika"]
print(*db.list_collection_names(),sep="\n")
col = db["153_yemeksepeti"]

# mydata={"adi":"ilhan","soyadi":"m","adres":"123"}
# col.insert_one(mydata)

sonuclar = col.find() 
for item in sonuclar:
    print(item)
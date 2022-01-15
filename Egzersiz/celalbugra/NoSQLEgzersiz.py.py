import pymongo 
cli = pymongo.MongoClient("mongodb+srv://dbuser:dbUser123@cluster0.6iawp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# print(*cli.list_database_names(),sep="\n")
db = cli["patika"]
print(*db.list_collection_names(),sep="\n")
col = db["153_yemeksepeti"]

data_dict = {'adi':'celal bugra','soyadi':'kaya','adres':'istanbul'}

result = col.insert_one(data_dict)
print(result.inserted_id)
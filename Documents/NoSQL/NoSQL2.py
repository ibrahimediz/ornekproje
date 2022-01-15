import pymongo 
cli = pymongo.MongoClient("mongodb+srv://dbuser:dbUser123@cluster0.6iawp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# print(*cli.list_database_names(),sep="\n")
db = cli["patika"]
# print(*db.list_collection_names(),sep="\n")
col = db["153_yemeksepeti"]

# sonuclar = col.find() # select *
# find({where için yazılacak},{select ile from arasına yazılacaklar}) 
############## sütunlar nasıl listelenir
# sonuclar = col.find({},{"_id":0,"adi":0,"soyadi":1}) #hata verir
# sonuclar = col.find({},{"_id":0,"adi":1,"soyadi":1})
# sonuclar = col.find({},{"_id":0,"adi":0})
# for item in sonuclar:
#     print(item)
##################### şart yazımı
# sart = {"adres":"deepturkishweb"}
# sart = {"soyadi":{"$gt":"B"}}
# sart = {"$or":[{"soyadi":{"$gt":"B"}},{"soyadi":"Alaattin"}]}
# sonuclar = col.find(sart,{"_id":0,"soyadi":1})
# print(*sonuclar,sep="\n")


"""
NAME	DESCRIPTION
$eq	It will match the values that are equal to a specified value.
$gt	It will match the values that are greater than a specified value.
$gte	It will match all the values that are greater than or equal to a specified value.
$in	It will match any of the values specified in an array.
$lt	It will match all the values that are less than a specified value.
$lte	It will match all the values that are less than or equal to a specified value.
$ne	It will match all the values that are not equal to a specified value.
$nin	It will match none of the values specified in an array.
"""

# sart = {"age":{"$in":[18,25]}}
# sart = {"soyadi":{"$regex":"^G"}}
# sonuclar = col.find(sart,{"_id":0,"soyadi":1})
# print(*sonuclar,sep="\n")
# """
# {'soyadi': 'Guardiola'}
# {'soyadi': 'Guavara'}
# """


sart = {"$or":[{"soyadi":{"$gt":"B"}},{"soyadi":"Alaattin"}]}
sonuclar = col.find(sart,{"_id":0,"adi":1,"soyadi":1}).sort("adi",-1).limit(2)
print(*sonuclar,sep="\n")
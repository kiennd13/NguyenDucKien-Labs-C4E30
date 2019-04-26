import pymongo
client = pymongo.MongoClient("mongodb+srv://kiennd13:jxDB1SH3TY0rBbpf@cluster0-nfuqv.mongodb.net/test?retryWrites=true")
db = client.bike


def add_bike(name,daily,image,year):
    db.bike.insert_one({"Name":name,"Daily":daily,"Image":image,"Year":year})

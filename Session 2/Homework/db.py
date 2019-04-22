import pymongo
client = pymongo.MongoClient("mongodb+srv://kiennd13:jxDB1SH3TY0rBbpf@cluster0-nfuqv.mongodb.net/test?retryWrites=true")
db = client.test

# db.foods.save({"name" : "cơm rang","price" : 20})
# db.foods.insert_one({"name" : "Phở gà", "price":25})
# db.foods.insert_one({"name" : "Phở bò", "price":30})
# print(list(db.foods.find({})))
# print(list(db.foods.find({"name":"Phở bò","price":30})))
# db.foods.update_one({"name": "Phở gà"}, {"$set": {"price":30}})
# db.foods.delete_one({"name": "cơm rang"})

def get_all():
    return list(db.foods.find({}))
def add_food(name,price):
    db.foods.insert_one({"name":name,"price":price})
def get_food_by_name(name):
    return db.foods.find_one({"name":name})
def update(name,price):
    db.foods.update_one({"name":name},{"$set":{"price":price}})




import pymongo
 

client = pymongo.MongoClient("mongodb+srv://admin:2fG9mSJu5OGSiWtI@demo-cluster-mvmw2.mongodb.net/test?retryWrites=true")
db = client.test

def update(name,price,image_url):
    db.foods.update_one({'name':name},{'$set':{'price':price,'image_url':image_url}})

def get_food_by_name(name):
    """
    Tìm một món ăn theo tên
    """
    return db.foods.find_one({"name":name})

def get_all(): 
    """
    Lấy tất cả các food
    """
    return list(db.foods.find({}))

def add_food(name,price,image_url):
    """
    Thêm một món ăn
    """
    db.foods.insert_one({"name":name,'price':price,'image_url':image_url})


# add_food('cơm rang',30)



# jxDB1SH3TY0rBbpf
from flask import Flask, render_template,request,url_for,redirect
from db import get_all,add_food,get_food_by_name,update
app = Flask(__name__)
# new_list_food = [
#      {
#        'name': "Cơm rang",
#        'prices' : "30k",
#        'jpg' : "https://media.cooky.vn/recipe/g3/27249/s800x500/recipe-cover-r27249.jpg"
#     },
#     {
#         'name' : "Phở bò",
#         'prices' : "25k",
#         'jpg' : "https://daynauan.info.vn/images/mon-viet/pho-ha-noi.jpg"
#     }
# ]

@app.route('/food-edit/<name>')
def edit_food(name):
    food = get_food_by_name(name)
    return render_template('food-edit.html', food = food)
@app.route('/food-edit/<name>',methods = ["POST"])
def post_edit_food(name):
    food_name = request.form.get("name")
    food_prices = request.form.get("price")
    update(food_name,food_prices)
    return render_template('new_list_food.html',a = get_all())
@app.route('/list_food',methods = ["POST"])
def food():
    food_name = request.form.get("ten_mon")
    food_prices = request.form.get("gia")
    # food_jpg = request.form.get("link_anh")
    add_food(food_name,food_prices)
    # food = {
    #     'name' : food_name,
    #     'prices' : food_prices,
    #     'jpg' : food_jpg
    # }
    # new_list_food.append(food)
    return redirect(url_for('index'))
@app.route('/list_food')
def index():
    return render_template('new_list_food.html',a = get_all())

if __name__ == '__main__':
  app.run(host = '127.0.0.1', port=8000, debug=True)
 
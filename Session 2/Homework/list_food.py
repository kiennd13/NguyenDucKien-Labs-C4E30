from flask import Flask, render_template, request
app = Flask(__name__)
list_food = [
    {
       'name': "Cơm rang",
       'prices' : "30k",
       'jpg' : "https://media.cooky.vn/recipe/g3/27249/s800x500/recipe-cover-r27249.jpg"
    },
    {
        'name' : "Phở bò",
        'prices' : "25k",
        'jpg' : "https://daynauan.info.vn/images/mon-viet/pho-ha-noi.jpg"
    }
    ]
@app.route('/list_food',methods=["POST"])
def post_food():
    food_name = request.form.get('ten_mon')
    food_price = request.form.get('gia')
    food_jpg = request.form.get("link_anh")
    food = {
        'name' : food_name,
        'prices' : food_price,
        'jpg' : food_jpg
           }
    list_food.append(food)
    return render_template('list_food.html', a = list_food)
@app.route('/list_food')
def index():
    return render_template('list_food.html', a = list_food)

if __name__ == '__main__':
  app.run(host = '127.0.0.1', port=8000, debug=True)
 
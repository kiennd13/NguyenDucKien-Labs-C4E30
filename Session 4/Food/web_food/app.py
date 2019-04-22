from flask import Flask, render_template, request, redirect, url_for
from db import get_all, add_food, get_food_by_name,update
app = Flask(__name__)
 
@app.route('/food-edit/<name>')
def edit_food(name):
    """
    Nhận tên món và hiển thị form sửa món ăn
    """
    food = get_food_by_name(name)
    return render_template('food-edit.html',food=food)

@app.route('/food-edit/<name>',methods=['POST'])
def post_edit_food(name):
  """
  Sửa món ăn theo tên
  """
  food_price=request.form.get('price')
  food_img=request.form.get('image_url')
  update(name,food_price,food_img)

  return redirect(url_for('get_food'))
  
@app.route('/')
def get_food():
  """
  Hiển thị các món đang có
  """

  return render_template('food.html',data=get_all())

@app.route('/',methods=["POST"])
def post_food():
  """
  Thêm một món ăn
  """
  food_name = request.form.get('name')
  food_price = request.form.get('price')
  food_image = request.form.get('image_url')
  add_food(food_name,food_price,food_image)

  return render_template('food.html',data=get_all())


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 
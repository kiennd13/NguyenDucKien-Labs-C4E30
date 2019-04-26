from flask import Flask, render_template, request, redirect, url_for, session, flash
from db import get_all, add_food, get_food_by_name,update
app = Flask(__name__)
app.secret_key = "31051995a@"
@app.route('/food-edit/<name>')
def edit_food(name):
    """
    Nhận tên món và hiển thị form sửa món ăn
    """
    if "username" in session:
      food = get_food_by_name(name)
      return render_template('food-edit.html',food=food)
    else:
      return redirect(url_for("login"))

@app.route('/food-edit/<name>',methods=['POST'])
def post_edit_food(name):
  """
  Sửa món ăn theo tên
  """
  if "username" in session:
    food_price=request.form.get('price')
    food_img=request.form.get('image_url')
    update(name,food_price,food_img)
    return redirect(url_for('get_food'))
  else:
    return redirect(url_for("login"))
@app.route('/')
def get_food():
  """
  Hiển thị các món đang có
  """
  if "username" in session:
    return render_template('food.html',data=get_all())
  else :
    return redirect(url_for("login"))
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

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods = ["POST"])
def post_login():
    error = None
    user_name = request.form.get('username')
    password = request.form.get('password')
    if user_name == 'admin' and password == 'admin':
        session["username"] = user_name
        return redirect(url_for("get_food"))
    else :
        error = 'Invalid username or password. Please try again!'
        return render_template('login.html', error = error)
@app.route("/css_test")
def test_css():
  return render_template("css_test.html")

@app.route("/logout")
def logout():
  session.pop('username')
  return redirect(url_for("login"))

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=7500, debug=True)
 
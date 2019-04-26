# from flask import Flask, render_template,redirect,url_for,request
# app = Flask(__name__)


# @app.route('/login')
# def login():
#     return render_template('login.html')

# @app.route('/login', methods = ["POST"])
# def post_login():
#     user_name = request.form.get('username')
#     password = request.form.get('password')
#     if user_name == 'admin' and password == 'admin':
#         return "Login Successful!"
#     else :
#         return redirect(url_for("login"))

# if __name__ == '__main__':
#   app.run(host = '127.0.0.1', port=8000, debug=True)
 
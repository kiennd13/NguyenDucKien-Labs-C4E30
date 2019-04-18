from flask import Flask, render_template, request,redirect,url_for
app = Flask(__name__)

@app.route('/login', methods=["POST"])
def login():
    error = None
    if request.form['username'] != 'admin' or \
         request.form['password'] != 'admin':
        error = 'Login Fail!'
        return render_template('login.html',error = error)
    else:
        return "Login Successful!"
	
@app.route('/login')
def index():
    return render_template('login.html')
if __name__ == '__main__':
  app.run(host = '127.0.0.1', port=8000, debug=True)
 
# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route('/hello/<user>/<int:score>')
# def hello_name(user,score):
#    return render_template('hello.html',name = user, marks = score)

# if __name__ == '__main__':
#    app.run(debug = True)

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

if __name__ == '__main__':
   app.run(debug = True)
 
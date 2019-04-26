from flask import Flask, render_template,redirect,request,url_for
from db3 import add_bike
app = Flask(__name__)


@app.route('/new_bike')
def new_bike():
    return render_template('bike.html')

@app.route('/new_bike',methods=["POST"])
def add_bike9():
    model = request.form.get("model")
    daily = request.form.get("daily")
    image = request.form.get("image")
    year = request.form.get("year")
    print({"model":model,"daily":daily,"image":image,"year":year})
    add_bike(model,daily,image,year)
    return redirect(url_for("new_bike"))
    

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 
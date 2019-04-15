from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<weight>/<height>')
def index(weight,height):
    a = float(weight) / ((float(height)/100)*(float(height)/100))
    if a < 16 :
        return "Severely underweight"
    elif a <= 18.5:
        return "Underweight"
    elif a < 25 :
        return "Normal"
    elif a <30 :
        return "Overweight"
    else:
        return "Obese"

@app.route('/bmi2/<weight>/<height>')
def cal(weight,height):
    a = float(weight) / ((float(height)/100)*(float(height)/100))
    return render_template('bmi.html', bmi = a)

if __name__ == '__main__':
  app.run(host = '127.0.0.1', port=5000, debug=True)
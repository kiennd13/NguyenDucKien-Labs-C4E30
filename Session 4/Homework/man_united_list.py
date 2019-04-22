from flask import Flask, render_template,request,url_for,redirect
from db2 import get_player_MU
app = Flask(__name__)


@app.route('/man_united')
def index():
    return render_template('united.html',list_player = get_player_MU())

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 
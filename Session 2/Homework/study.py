from flask import Flask, render_template, redirect, url_for 
app = Flask(__name__)


@app.route('/about-me')
def about_me():
    information = {
        'name' : 'Nguyễn Đức Kiên',
        'work' : 'Network Engineer',
        'school' : 'PTIT',
        'organization' : 'FPT Telecom'
    }
    return render_template('study.html', infor = information)
    
@app.route('/school')
def a():
    return redirect('http://techkids.vn', code=302)


if __name__ == '__main__':
  app.run(host = '127.0.0.1', port=5000, debug=True)
 
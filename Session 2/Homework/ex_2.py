from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def index(username):
    Users = {
        "Hoa" : {
            "name" : "HoaPT",
            "age" : "29",
            'work' : 'Assistant',
            'school' : 'NEU',
            'organization' : 'Huawei'
        },
        "Kien": {
            "name" : "KienND",
            "age" : "25",
            'work' : 'Network Engineer',
            'school' : 'PTIT',
            'organization' : 'FPT Telecom'
        }
    }
    if username not in Users.keys():
        return "User not found"
    else:    
        return render_template('profile.html', a = Users, b = Users[username])
        
if __name__ == '__main__':
  app.run(host = '127.0.0.1', port=5000, debug=True)




# user = {
#       "Huy" : {
#             "name" : "NQHuy",
#             "age" : "29"
#         },
#         "Kien": {
#             "name" : "KienND",
#             "age" : "25"
#         }
# }
# for v in user.values():
#     print(v['name'])
#     print(v['age'])
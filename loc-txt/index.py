from flask import Flask, render_template, request, redirect,json
import os
app = Flask(__name__)
app.debug = True


def find(username):
    '''
        根据用户名查找是否已经注册，如果是，返回用户的全部信息，如果不是，返回None
    '''
    file = open("PY_Level4/20/20/users.txt","r")
    js = file.read()
    users = json.loads(js)
    file.close()
    for user in users:
        if user['username'] == username:
            return user
    return None

#关于返回的数字为什么要转成字符串：因为我返回数字，发现TypeError: The view function did not return a valid response. The return type must be a string, dict, tuple, Response instance, or WSGI callable, but it was a int.
@app.route('/admin', methods=['GET'])
def admin():
    return render_template('admin.html')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def home1():
    if request.form.get("p")=="0":
      try:
        file = open("PY_Level4/20/20/static/images/items/photos.txt","r")
        js = file.read()
        photos = json.loads(js)
        file.close()
        return str(photos)
      except:
        return "555"
    else:
        try:
          file = open("PY_Level4/20/20/static/images/items/"+str(request.form.get("im1"))+".txt","r")
          return file.read()
        except:
          return "555"
        
  
# 在下方写你的代码：设置登录路由(请求方式为POST)
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get("yhm")
    password = request.form.get("mm")
    try:
      user = find(username)
    except:
          return "555"  
    if user is None:
        return "122" #用户不存在
    elif user["password"] != password:
        return "122" #密码错误
    else:
        return "200"

@app.route('/rm', methods=['POST'])
def rm():
    mm = request.form.get("mm")
    id = int(request.form.get("id"))

    if mm=="1":
      try: 
        file = open("PY_Level4/20/20/static/images/items/photos.txt","r")
        js = file.read()
        photos = json.loads(js)
        file.close()
        os.remove("PY_Level4/20/20/static/images/items/"+str(photos[id]["imid"])+".txt")
        photos.pop(id)
        js = json.dumps(photos)
        file = open("PY_Level4/20/20/static/images/items/photos.txt","w")
        file.write(js)
        file.close()
        return "211"  
      except:
          return "555"  
    else:
        return "555"
 

# 在下方写你的代码：注册的路由(请求方式为POST)
@app.route('/register', methods=['POST'])
def register():
    username = request.form.get("yhm")
    password = request.form.get("mm")
    try:
      user = find(username)
      if user is not None:
          return "152" #已注册
      users.append({'username': username, 'password': password})
    except:
        users=[{'username': username, 'password': password}]
    js = json.dumps(users)
    file = open("PY_Level4/20/20/users.txt","w")
    file.write(js)
    file.close()
    return "211" #okk

@app.route('/tp', methods=['POST'])
def tp():

    try:
        file = open("PY_Level4/20/20/static/images/items/photos.txt","r")
        js = file.read()
        photos = json.loads(js)
        file.close()
        for i in photos:
            a = i
        file = open("PY_Level4/20/20/static/images/items/%s.txt"%str(a["imid"]+1),"w")
        file.write(request.form.get("im"))
        file.close()
        photos.append({'name':request.form.get("yhm"),'imid':a["imid"]+1})
        js = json.dumps(photos)
        file = open("PY_Level4/20/20/static/images/items/photos.txt","w")
        file.write(js)
        file.close()
    except:
        photos=[{'name':request.form.get("yhm"),'imid':1}]
        file = open("PY_Level4/20/20/static/images/items/1.txt","w")
        file.write(request.form.get("im"))
        file.close()
        js = json.dumps(photos)
        file = open("PY_Level4/20/20/static/images/items/photos.txt","w")
        file.write(js)
        file.close()

    return "211" #okk
    


app.run(host='127.0.0.1', port=8000)
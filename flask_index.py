from flask import Flask,render_template

app = Flask(__name__)

@app.route("/mother")

def mother_webpage():
    name = "Preeti Awasthi" # write your name
    age = "42" # write your age

    return render_template('index.html' , name = name , age = age)
 
@app.route("/father")

def father_webpage():
    name = "Rajiv Awasthi" # write your name
    age = "45" # write your age

    return render_template('index1.html' , name = name , age = age)


@app.route("/me")

def me_webpage():
    name = "Aniket Awasthi" # write your name
    age = "18" # write your age

    return render_template('index2.html' , name = name , age = age)

@app.route("/friend")

def friend_webpage():
    name = "Kumar Aryan" # write your name
    age = "18" # write your age

    return render_template('index3.html' , name = name , age = age)

app.run(debug = True)
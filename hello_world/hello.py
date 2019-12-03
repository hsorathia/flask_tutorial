from flask import Flask

# creating a variable that represents our application

app = Flask(__name__)

# decorator for flask that tells the app which page the user is loading
@app.route("/")

# hello function should run everytime someone uses our app
def hello():
        
    return "Hello world"
    # value = str(pow(3,2))
    # return value

app.run()
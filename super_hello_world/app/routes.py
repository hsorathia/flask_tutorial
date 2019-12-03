from app import app
from flask import render_template


@app.route("/")
def home():
    myName = {'name': 'habib'}
    return '''
    <html>
        <head>
            <title>Home</title>
        </head>
        <body>
            <h1>hi, ''' + myName['name'] + '''</h1>
        </body>
    </html>
    '''
    # return render_template('home.html', title="whoa")

@app.route("/loops")
def loops():
    MyCars = ['hyundai sonata', 'toyota camry', 'toyota sienna']
    return render_template('loops.html', title="for loops!", cars=MyCars)

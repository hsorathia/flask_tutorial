from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/login", methods=['GET', 'POST'])
def Login():
    form=LoginForm()
    if form.validate_on_submit():
        flash('logged in succesfully')
        return redirect('/home')
    return render_template('login.html', form=form)

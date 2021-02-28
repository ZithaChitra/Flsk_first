# pip install flask
# pip install flask-wtf
# pip install email_validator
# pip install flask-sqlalchemy

from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from models import User, Post



app = Flask(__name__)
app.config["SECRET_KEY"] = "d879e696ab6a235dbd2ca303cccbc1b7"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
# create a database instance
# SQLAlchemy lets you interact with a database in an object oriented way
# It also lets you use different databases without changing your python code

db = SQLAlchemy(app)
# SQLAlchemy let's you represent your database structure as classes
# The classes are called models
# Each class will be it's own table in the database
# First, let's create the user class to hold our users



posts = [
	{
		"author": "Blessing Chitra",
		"title": "Blog Post 1",
		"content": "First post content",
		"date_posted": "27 Feb 2021",
	},

	{
		"author": "Nqobizitha Chitra",
		"title": "Blog Post 2",
		"content": "Second post content",
		"date_posted": "27 Feb 2021",
	}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html", posts= posts)


@app.route("/about")
def about():
	return render_template("about.html", title="about")


@app.route("/register", methods=["GET", "POST"])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f"Account created for {form.username.data}!", "success")
		return redirect(url_for("home"))
	return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["Get", "POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == "chitra@me.com" and form.password.data == "123":
			flash("You have been logged in!", "success")
			return redirect(url_for("home"))
		else:
			flash("LogIn unsuccessful. Please check username and password", "danger")

	return render_template("login.html", title="login", form=form)

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")
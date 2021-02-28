# pip install flask
# pip install flask-wtf
# pip install email_validator
# pip install flask-sqlalchemy

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


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
from flaskblog import routes
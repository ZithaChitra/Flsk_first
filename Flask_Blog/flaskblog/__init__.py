# pip install flask
# pip install flask-wtf
# pip install email_validator
# pip install flask-sqlalchemy

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



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
bcrypt = Bcrypt(app)

# We will add some functionality to our database models
# and then it will handle all the sessions in the background for us
login_manager = LoginManager(app)

from flaskblog import routes
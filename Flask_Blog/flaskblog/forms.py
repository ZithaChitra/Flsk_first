from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
	username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email',
                        validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

	# def validate_field(self, field):
	# 	if True:
	# 		raise ValidationError("Validation Message")

	def validate_username(self, username):
		# checks if user already exists in the database
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError("That username is taken. Please use a different username.")

	
	def validate_email(self, email):
		# checks if user already exists in the database
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError("That email is taken. Please use a different email.")


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


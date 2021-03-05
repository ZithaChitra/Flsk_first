from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
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


class UpdateAccountForm(FlaskForm):
	username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email',
                        validators=[DataRequired(), Email()])
	picture = FileField("Update Profile Picture", validators=[FileAllowed(["jpg", "png"])])
	
	submit = SubmitField('Update')

	# def validate_field(self, field):
	# 	if True:
	# 		raise ValidationError("Validation Message")

	def validate_username(self, username):
		if username.data != current_user.username:
			# checks if user already exists in the database
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError("That username is taken. Please use a different username.")

	
	def validate_email(self, email):
		if email.data != current_user.email:
			# checks if user already exists in the database
			user = User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError("That email is taken. Please use a different email.")



class PostForm(FlaskForm):
	title = StringField("Title", validators=[DataRequired()])
	content = TextAreaField("Content", validators=[DataRequired()])
	submit = SubmitField("Post")



# Form for when they first go to the reset password
# page, where they can submit their email account 
# to where the instructions for reseting the password
# will be sent.
class RequestResetForm(FlaskForm):
	email = StringField("Email", validators=[DataRequired(), Email()])
	submit = SubmitField("Request password reset", validators=[])

	# check that an account exists for the given email address
	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is None:
			raise ValidationError("There is no account with that email. You must register first.")
			
# Form for when they do actually reset their password
class RequestPasswordForm(FlaskForm):
	password = PasswordField("Password", validators=[DataRequired()])
	confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
	submit = SubmitField("Reset Password")
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired


class AddUserForm(FlaskForm):
    username = StringField("Username", validators=[
        InputRequired(message="Username cannot be empty")])
    password = PasswordField("Password", validators=[
        InputRequired(message="Password cannot be empty")])
    email = StringField("Email", validators=[
                        InputRequired(message="Email cannot be empty")])
    first_name = StringField("First Name", validators=[
                             InputRequired(message="First Name cannot be empty")])
    last_name = StringField("Last Name", validators=[
                            InputRequired(message="Last Name cannot be empty")])


class LoginUserForm(FlaskForm):
    username = StringField("Username", validators=[
                           InputRequired(message="Username cannot be empty")])
    password = PasswordField("Password", validators=[
                             InputRequired(message="Password cannot be empty")])


class AddFeedbackForm(FlaskForm):
    title = StringField("Title", validators=[
                        InputRequired(message="Title cannot be empty")])
    content = StringField("Content", validators=[
                          InputRequired(message="Content cannot be empty")])

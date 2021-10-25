from flask import Flask, request, flash, redirect, render_template, session
from models import db, connect_db, User, Feedback
from forms import AddUserForm, LoginUserForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///users"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'HelloWorld'

connect_db(app)


@app.route('/')
def index():
    return redirect('/register')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = AddUserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        new_user = User.register(
            username, password, email, first_name, last_name)
        db.session.add(new_user)
        db.session.commit()

        session['username'] = new_user.username

        flash('Welcome! Account created successfully!')
        return redirect(f'/users/{new_user.username}')
    else:
        return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginUserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)
        if user:
            flash(f'Welcome back {user.first_name}')
            session['username'] = user.username
            return redirect(f'/users/{user.username}')
        else:
            form.username.errors = ['Invalid username/password']

    return render_template('login.html', form=form)


@app.route('/users/<username>')
def secret(username):
    user = User.query.get(username)

    if "username" not in session:
        flash("Please login first!")
        return redirect('/')
    return render_template('secret.html', user=user)


@app.route('/logout')
def logout():
    session.pop('username')
    flash("Successfully logged out!")
    return redirect('/')

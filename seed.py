from app import app
from models import db, User, Feedback
from flask_bcrypt import Bcrypt


db.drop_all()
db.create_all()


def hashed(pwd):
    bcrypt = Bcrypt()
    hashed = bcrypt.generate_password_hash(pwd)
    hashed_utf8 = hashed.decode('utf8')
    return hashed_utf8


u1 = User(
    username="jimjam5227",
    password=hashed('Agnusdei1968!'),
    email="jimjam5227@gmail.com",
    first_name="Jimmy",
    last_name="Yee"
)

u2 = User(
    username="mrmonkey1",
    password=hashed('mrmonkey1'),
    email="MojoJojo1@mojojo.com",
    first_name="Mojo",
    last_name="Jojo"
)

u3 = User(
    username="homersimpson",
    password=hashed('homersimpson'),
    email="homersimpson@homersimpson.com",
    first_name="Homer",
    last_name="Simpson"
)

f1 = Feedback(
    title="My First Feedback",
    content="It is I. Mojo Jojo!",
    username="mrmonkey1"
)

f2 = Feedback(
    title='Mmmmm Donuts',
    content='(Drools)',
    username='homersimpson'
)

db.session.add_all([u1, u2, u3, f1, f2])
db.session.commit()

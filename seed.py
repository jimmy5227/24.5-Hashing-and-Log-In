from app import app
from models import db, User
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


db.session.add(u1)
db.session.commit()

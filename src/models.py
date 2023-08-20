from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class FavoritesPeople(db.Model):
    __tablename__ = 'favoritesperson'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    person_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites_people = db.relationship(FavoritesPeople, backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(30), unique=True, nullable=False)
    eye_color = db.Column(db.String(30), unique=False, nullable=True)
    hair_color = db.Column(db.String(30), unique=False, nullable=True)
    height = db.Column(db.Float, unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    favorites_people = db.relationship(FavoritesPeople, backref='people', lazy=True) 

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "eye_color":self.eye_color,
            "hair_color": self.hair_color,
            "height": self.height,
            "age": self.age
        }



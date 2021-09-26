from app.models import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

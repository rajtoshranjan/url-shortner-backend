from .extensions import db

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        pass

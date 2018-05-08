from app import db

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    location = db.Column(db.String(200))

    def __repr__(self):
        return '<Video {}>'.format(self.title)

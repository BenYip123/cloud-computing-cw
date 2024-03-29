from __init__ import db


album_image = db.Table('album_image', db.Model.metadata,
    db.Column('album_id', db.Integer, db.ForeignKey('album.id'), primary_key = True),
    db.Column('image_id', db.Integer, db.ForeignKey('image.id'), primary_key = True)
 )

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    sub = db.Column(db.Integer, unique=True)
    email = db.Column(db.String(80), unique=True)
    picture = db.Column(db.String(80), nullable=True)
    given_name = db.Column(db.String(80))
    family_name = db.Column(db.String(80))

    user_image = db.relationship("Image", primaryjoin="User.id==Image.user_id")
    user_album = db.relationship("Album", primaryjoin="User.id==Album.user_id")

    def __repr__(self):
        return f'User ({self.id} {self.sub} {self.email} {self.picture} {self.given_name} {self.family_name})'

class Image(db.Model):
    __tablename__ = 'image'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    date_uploaded = db.Column(db.DateTime, nullable = False)
    caption = db.Column(db.String(150))

    def __repr__(self):
        return f'Image ({self.id} {self.user_id} {self.date_uploaded} {self.caption})'

class Album(db.Model):
    __tablename__ = 'album'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    title = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, nullable = False)

    images = db.relationship("Image", secondary=album_image, backref=db.backref('albums'))

    def __repr__(self):
        return f'Album ({self.id} {self.user_id} {self.title} {self.date_created})'
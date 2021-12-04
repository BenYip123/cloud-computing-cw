from api import db

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
        return f'User ({self.id} {self.sub})'

class Image(db.Model):
    __tablename__ = 'image'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable = False)
    date_uploaded = db.Column(db.DateTime, nullable = False)
    caption = db.Column(db.String(150))
    image_album = db.relationship("Album", primaryjoin="Image.id==Album.image_id")

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Album(db.Model):
    __tablename__ = 'album'
    id = db.Column(db.Integer, primary_key = True)
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    title = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, nullable = False)
    album_image = db.relationship("Image", primaryjoin="Album.id==Image.album_id")

    def __repr__(self):
        return '<id {}>'.format(self.id)
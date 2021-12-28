from models import User
from models import Image
from models import Album

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import datetime
from sqlalchemy import desc
from sqlalchemy import exc

from __init__ import db

def db_commit_add(row):
	db.session.add(row)
	db.session.commit()

def db_commit_delete(row):
	db.session.delete(row)
	db.session.commit()

def db_add_user(sub, email, picture, given_name, family_name):
	try:
		user = User(sub = sub, email = email, picture = picture, given_name = given_name, family_name = family_name)
		db.session.add(user)
		db.session.commit()
	except exc.SQLAlchemyError as e:
		db.session.rollback()
		return False
	else:
		return True
		

def db_add_image(user_id, album_id = 0, date_uploaded = datetime.datetime.now(), caption = ''):
	try:
		image = Image(user_id = user_id, album_id = album_id, date_uploaded = date_uploaded, caption = caption)
		db.session.add(image)
		db.session.commit()
	except exc.SQLAlchemyError as e:
		db.session.rollback()
		return False
	else:
		return True

def db_add_album(title, user_id, image_id = 0, date_created = datetime.datetime.now()):
	try:
		album = Album(title = title, image_id = image_id, user_id = user_id, date_created = date_created)
		db.session.add(album)
		db.session.commit()
	except exc.SQLAlchemyError as e:
		db.session.rollback()
		return False
	else:
		return True

def db_delete_user(user_id):
	try:
		User.query.filter_by(id = user_id).delete()
		db.session.commit()
	except exc.SQLAlchemyError as e:
		db.session.rollback()
		return False
	else:
		return True

def db_delete_image(image_id):
	try:
		Image.query.filter_by(id = image_id).delete()
		db.session.commit()
	except exc.SQLAlchemyError as e:
		db.session.rollback()
		return False
	else:
		return True

def db_delete_album(album_id):
	try:
		Album.query.filter_by(id = album_id).delete()
		db.session.commit()
	except exc.SQLAlchemyError as e:
		db.session.rollback()
		return False
	else:
		return True

#search for a user in the User table by id
def db_get_user_by_id(user_id):
	try:
		user = User.query.filter_by(id = user_id).first()
	except exc.SQLAlchemyError as e:
		return (False)
	else:
		return (True, user)

#search for an image in the Image table by id
def db_get_image_by_id(image_id):
	try:
		image = Image.query.filter_by(id = image_id).first()
	except exc.SQLAlchemyError as e:
		return (False)
	else:
		return (True, image)

#search for an album in the Album table by id
def db_get_album_by_id(album_id):
	try:
		album = Album.query.filter_by(id = album_id).first()
	except exc.SQLAlchemyError as e:
		return (False)
	else:
		return (True, album)


#search for a user in the User table by email
def db_get_user_by_email(email):
	try:
		user = User.query.filter_by(email = email).first()
	except exc.SQLAlchemyError as e:
		return (False)
	else:
		return (True, user)

#search for a user by their name
def db_get_user_by_name(firstname, surname):
	try:
		user = User.query.filter_by(given_name = firstname, family_name = surname).first()
	except exc.SQLAlchemyError as e:
		return (False)
	else:
		return (True, user)

#search for all images from a specific user id
def db_get_image_by_user_id(user_id):
	try:
		image = Image.query.filter_by(user_id = user_id).all()
	except exc.SQLAlchemyError as e:
		return (False)
	else:
		return (True, image)

#search for the n most recent images from all users
def db_get_n_recent_images(n):
	try:
		image = Image.query.order_by(desc(Image.date_uploaded)).limit(n).all()
	except exc.SQLAlchemyError as e:
		return (False)
	else:
		return (True, image)

#search for all albums from a specific user id
def db_get_album_by_user_id(user_id):
	try:
		album = Album.query.filter_by(user_id = user_id).all()
	except exc.SQLAlchemyError as e:
		return (False)
	else:
		return (True, album)

#search for albums that contain a specific image id
def db_get_album_by_image_id(image_id):
	try:
		album = Album.query.filter_by(image_id = image_id).all()
	except exc.SQLAlchemyError as e:
		return (False)
	else:
		return (True, album)

#search for user's n most recent albums (default 50 if not specified)
def db_get_users_n_recent_albums(user_id, n=50):
	try:
		album = Album.query.filter_by(user_id = user_id).order_by(desc(Album.date_created)).limit(n).all()
	except exc.SQLAlchemyError as e:
		return (False)
	else:
		return (True, album)

#search for albums by title
def db_get_album_by_title(title):
	try:
		album = Album.query.filter_by(title = title).first()
	except exc.SQLAlchemyError as e:
		return (False)
	else:
		return (True, album)

#get all images from a specific album_id
def db_get_all_images_from_album(album_id):
	try:
		image = Image.query.filter(Image.albums.any(id=album_id)).all()
	except exc.SQLAlchemyError as e:
		return (False)
	else:
		return (True, image)

#get all albums from a specific image_id (all albums that the image is in)
def db_get_all_albums_from_images(image_id):
	try:
		album = Album.query.filter(Album.images.any(id=image_id)).all()
	except exc.SQLAlchemyError as e:
		return (False)
	else:
		return (True, album)

#add to the album_image table
def db_add_album_image(album_id, image_id):
	try:
		image = Image.query.filter(Image.id==image_id).first()
		album = Album.query.filter(Album.id==album_id).first()
		album.images.append(image)
		db.session.add(album)
		db.session.commit()
	except exc.SQLAlchemyError as e:
		db.session.rollback()
		return False
	else:
		return True

#query_user1 = User.query.filter_by(email = "user1@gmail.com").first()

#image1 = db_add_image(user_id = query_user1.id, caption = "hello")

user1 = db_add_user(5, "fdsfs", "jfdisfs", "name", "afds")
print(user1)

search = db_get_user_by_name("name", "afds")
print(search[0])
print(search[1])
print(search[1].family_name)
print(search)
if(search[0]):
	print("retrieved: " +str(search[1]))
else:
	print("database failure")

print(db_get_album_by_title("title2"))
print(db_get_album_by_user_id(1))
print(db_delete_user(search[1].id))

#example insert into album_image
print(db_add_album_image(album_id=2, image_id=3))

#example getting all images from a specific album
album = db_get_album_by_user_id(1)
print(album)
print(db_get_all_images_from_album(album[1][1].id))

#example getting all albums from a specific image
image = db_get_image_by_id(3)
print(image)
print(db_get_all_albums_from_images(image[1].id)[1])
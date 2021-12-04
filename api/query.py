from models import User
from models import Image
from models import Album

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import datetime
from sqlalchemy import desc

from __init__ import db

def db_commit_add(row):
	db.session.add(row)
	db.session.commit()

def db_commit_delete(row):
	db.session.delete(row)
	db.session.commit()

def db_add_user(sub, email, picture, given_name, family_name):
	user = User(sub = sub, email = email, picture = picture, given_name = given_name, family_name = family_name)
	db.session.add(user)
	db.session.commit()

def db_add_image(user_id, album_id = 0, date_uploaded = datetime.datetime.now(), caption = ''):
	image = Image(user_id = user_id, album_id = album_id, date_uploaded = date_uploaded, caption = caption)
	db.session.add(image)
	db.session.commit()

def db_add_album(title, user_id, image_id = 0, date_created = datetime.datetime.now()):
	album = Album(title = title, image_id = image_id, user_id = user_id, date_created = date_created)
	db.session.add(album)
	db.session.commit()

def db_delete_user(user_id):
	User.query.filter_by(id = user_id).delete()
	db.session.commit()

def db_delete_image(image_id):
	Image.query.filter_by(id = image_id).delete()
	db.session.commit()

def db_delete_album(album_id):
	Album.query.filter_by(id = album_id).delete()
	db.session.commit()

#search for a user in the User table by id
def db_get_user_by_id(user_id):
	user = User.query.filter_by(id = user_id).first()
	return user

#search for an image in the Image table by id
def db_get_image_by_id(image_id):
	image = Image.query.filter_by(id = image_id).first()
	return image

#search for an album in the Album table by id
def db_get_album_by_id(album_id):
	album = Album.query.filter_by(id = album_id).first()
	return album


#search for a user in the User table by email
def db_get_user_by_email(email):
	user = User.query.filter_by(email = email).first()
	return user

#search for a user by their name
def db_get_user_by_name(firstname, surname):
	user = User.query.filter_by(given_name = firstname, family_name = surname).first()
	return user

#search for all images from a specific user id
def db_get_image_by_user_id(user_id):
	image = Image.query.filter_by(user_id = user_id).all()
	return image

#search for the n most recent images from all users
def db_get_n_recent_images(n):
	image = Image.query.order_by(desc(Image.date_uploaded)).limit(n).all()
	return image

#search for all albums from a specific user id
def db_get_album_by_user_id(user_id):
	album = Album.query.filter_by(user_id = user_id).all()
	return album

#search for albums that contain a specific image id
def db_get_album_by_image_id(image_id):
	album = Album.query.filter_by(image_id = image_id).all()
	return album

#search for user's n most recent albums (default 50 if not specified)
def db_get_users_n_recent_albums(user_id, n=50):
	album = Album.query.filter_by(user_id = user_id).order_by(desc(Album.date_created)).limit(n).all()
	return album

#search for albums by title
def db_get_album_by_title(title):
	album = Album.query.filter_by(title = title).all()
	return album

#query_user1 = User.query.filter_by(email = "user1@gmail.com").first()

#image1 = db_add_image(user_id = query_user1.id, caption = "hello")

#search = db_get_user_by_name("name", "surname")
#print(search)


from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Creator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), unique=True, nullable=False)
    text = db.Column(db.Text, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('creator.id'), nullable=False)
    likes = db.Column(db.Integer)
    views = db.Column(db.Integer)
    comments = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    creator = db.relationship('Creator', backref=db.backref('videos', lazy=True))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class UserCreator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('creator.id'), nullable=False)
    auto_track = db.Column(db.Boolean, default=False)

    user = db.relationship('User', backref=db.backref('user_creators', lazy=True))
    creator = db.relationship('Creator', backref=db.backref('user_creators', lazy=True))
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    subscription = db.Column(db.String(50), nullable=False, default='free')  # Abonnement: free, pro, premium

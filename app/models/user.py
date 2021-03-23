from datetime import datetime
from app.app import db
from app.models.key import Key

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20))
    user_email = db.Column(db.String(60), unique=True, index=True)
    user_password = db.Column(db.String(80))
    create_date = db.Column(db.DateTime, default=datetime.now)
    last_login_date = db.Column(db.DateTime, default=datetime.utcnow())
    is_confirmed = db.Column(db.Boolean, default=False, nullable=False)
    role = db.Column(db.String(25), default='Guest', nullable=False)
    keys = db.relationship('Key', backref='user', lazy=True)
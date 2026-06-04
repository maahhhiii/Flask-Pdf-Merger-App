from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    session_id = db.Column(db.String(120), nullable=False)
    filename = db.Column(db.String(255), nullable=False)

    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
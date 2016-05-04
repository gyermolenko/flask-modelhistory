from sqlalchemy.dialects.postgresql import JSON
from app import db


class HistoryModel(db.Model):
    __tablename__ = 'history'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, nullable=True)
    object_type = db.Column(db.String(32), nullable=False)
    object_id = db.Column(db.Integer, nullable=False)
    data = db.Column(JSON)


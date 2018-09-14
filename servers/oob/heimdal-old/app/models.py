from app import db
from sqlalchemy.dialects.postgresql import JSON

class Result(db.Model):
    __tablename__ = 'servers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    address = db.Column(db.String(128), unique=False, nullable=False)
    host_status = db.Column(db.String(16), unique=False, nullable=False)

    def __init__(self, url, result_all, result_no_stop_words):
        self.name = name
        self.address = address
        self.host_status = host_status

    def __repr__(self):
        return '<id {}>'.format(self.id)
        

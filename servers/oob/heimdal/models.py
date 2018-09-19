#from sqlalchemy import Column, Integer, Text  
#from sqlalchemy.dialects.postgresql import JSON, JSONB
#from app import db

#class Result(db.Model):
#    __tablename__ = 'servers'
#
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(80), unique=False, nullable=False)
#    address = db.Column(db.String(128), unique=False, nullable=False)
#    host_status = db.Column(db.String(16), unique=False, nullable=False)
#
#    def __init__(self, name, address, host_status):
#        self.name = name
#        self.address = address
#        self.host_status = host_status
#
#    def __repr__(self):
#        return '<id {}>'.format(self.id)
    

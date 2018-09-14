from app import *

app = Flask(__name__, instance_relative_config=True)

class Seed():
    __tablename__ = 'servers'
    hosts = [{ 'name' : '127.0.0.1', 'address': '127.0.0.1', 'host_status': 'Unknown'},
            { 'name' : 'localhost', 'address': '127.0.0.1', 'host_status': 'Unknown'}]

    #db.bulk_insert()
    db.session.add(hosts)
    db.session.commit()


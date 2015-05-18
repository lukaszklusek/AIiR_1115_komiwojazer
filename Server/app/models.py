'''
Po każdej zmianie w strukturze bazy trzeba albo utworzyć ją od nowa (db_create.py)
albo zmigrować starą (zachowując dane);
    db_migrate.py - utworzenie nowej wersji bazy
    db_upgrade(downgrade.py) - upgrade(downgrade) obecnej bazy do nowej(poprzedniej) wersji utworzonej przez db_migrate.py
                                (wszystkie wersje są składowane w db_repository)
'''
from app import db
import datetime
from sqlalchemy import CheckConstraint

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(120))
    active = db.Column(db.Boolean)

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.active = True

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<User %r>' % self.email

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    input = db.Column(db.String(1024))
    output = db.Column(db.String(1024))
    time_started = db.Column(db.DateTime)
    time_finished = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    state = db.Column(db.String(10))
    progress = db.Column(db.Integer, CheckConstraint('progress>=0 & progress<=100'),default=0)

    def init_from_file(self, filepath, user):
        self.time_started = datetime.datetime.now()
        self.state = "working"
        file = open(filepath, 'r')
        self.input = file.read()
        self.user_id = user.id


    def add_waiting_task(self, user):
        self.user_id = user.id
        self.state="waiting"
        return self

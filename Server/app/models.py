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
    time_started = db.Column(db.DateTime)
    time_finished = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    state = db.Column(db.String(10))
    max_value = db.Column(db.Integer)
    points = db.Column(db.Integer)
    progress = db.Column(db.Integer, CheckConstraint('progress>=0 & progress<=100'),default=0)

    def init_from_file(self, filepath, user):
        self.time_started = datetime.datetime.now()
        self.state = "ready"
        self.user_id = user.id
        file = open(filepath, 'r')
        self.points = int(file.readline())
        self.max_value = int(file.readline())

        for i in range(1,self.points + 1):
            point = PointIn()
            x, y = file.readline().split()
            point.add_new_point(self.id, i ,int(x),int(y))
            db.session.add(point)
            db.session.commit()

    def add_waiting_task(self, user):
        self.user_id = user.id
        self.state="waiting"
        return self

class PointIn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'))

    def add_new_point(self, task, number, x , y):
        self.task_id = task
        self.x = x
        self.y = y
        self.number = number
        return self


class PointOut(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'))

    def add_new_point(self, task, number, x , y):
        self.task_id = task
        self.x = x
        self.y = y
        self.number = number
        return self
from db import db


class TaskModel(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    # task_id = db.Column(db.Integer, primary_key=True)
    # task_id = db.Column(db.String(80))
    schedule_time = db.Column(db.String(80))
    lines = db.Column(db.String(120))
    disruption = db.relationship("DisruptionModel", backref="tasks", lazy=True, uselist=False)
    # disruption = db.relationship("DisruptionModel", lazy=True)
    # disruption = db.relationship("DisruptionModel", lazy="dynamic")
    # disruption = db.relationship("DisruptionModel", backref="tasks", lazy="dynamic")
    # items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, schedule_time, lines):
        self.schedule_time = schedule_time
        self.lines = lines

    def json(self):
        return {
            "id": self.id,
            "schedule_time": self.schedule_time,
            "lines": self.lines
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    # @classmethod
    # def find_by_username(cls, username):
    #     return cls.query.filter_by(username=username).first()

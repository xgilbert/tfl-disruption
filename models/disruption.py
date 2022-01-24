from db import db


class DisruptionModel(db.Model):
    __tablename__ = "disruptions"

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey("tasks.id"), nullable=False)
    category = db.Column(db.String(80))
    description = db.Column(db.String(250))

    def __init__(self, category, description, task_id):
        self.category = category
        self.description = description
        self.task_id = task_id

    def json(self):
        return {
            "id": self.id,
            "task_id": self.task_id,
            "category": self.category,
            "description": self.description
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
    def find_by_task_id(cls, _id):
        return cls.query.filter_by(task_id=_id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()


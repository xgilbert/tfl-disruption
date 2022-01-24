from flask import Flask, request
from flask_restful import Resource, Api

from db import db
from resources.disruption import DisruptionCreate
from resources.welcome import Welcome
from resources.user import UserRegister
from resources.task import Task, TaskList, TaskCreate
from resources.disruption import DisruptionCreate


app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "3bce79429ad6b79670e4e800fb4a57b9"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///disruptions.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
api = Api(app)

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Welcome, "/")
api.add_resource(UserRegister, "/register")
api.add_resource(TaskCreate, '/tasks')
api.add_resource(TaskList, "/tasks")
api.add_resource(Task, '/tasks/<int:task_id>')
api.add_resource(DisruptionCreate, '/disruptions')


if __name__ == "__main__":
    from db import db

    db.init_app(app)
    # app.run(host="0.0.0.0", port=port, debug=True)
    app.run(host="localhost", port=5555, debug=True)

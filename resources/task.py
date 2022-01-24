from flask_restful import Resource, reqparse

from models.task import TaskModel
from controller import Controller

task_controller = Controller()

class Task(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "schedule_time",
        type=str,
        required=False,
        help="If None, task run immediately."
        )
    parser.add_argument(
        "lines",
        type=str,
        required=True,
        help="This field cannot be blank."
        )
    
    @classmethod
    def get(cls, task_id):
        task = TaskModel.find_by_id(task_id)
        if task:
            return task.json()
        return {"message": "Task not found"}, 404

    @classmethod
    def put(cls, task_id):
        data = cls.parser.parse_args()
        task = TaskModel.find_by_id(task_id)

        if task:
            task.schedule_time = data["schedule_time"]
            # @TODO case if task has been run already
            task.lines = data["lines"]
        else:
            task = TaskModel(task_id, **data)

        task.save_to_db()

        return task.json()

    @classmethod
    def delete(cls, task_id):
        task = TaskModel.find_by_id(task_id)
        if task:
            task.delete_from_db()
        return {"message": " deleted successfully."}, 200


class TaskCreate(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "schedule_time",
        type=str,
        required=False,
        help="If None, task run immediately."
        )
    parser.add_argument(
        "lines",
        type=str,
        required=True,
        help="This field cannot be blank."
        )

    @classmethod
    def post(cls):
        data = Task.parser.parse_args()

        # @TODO check that line id is valid
        
        # if no schedule_time then run immediately
        if data["schedule_time"] is None:
            data["schedule_time"] = "now"

        task = TaskModel(data["schedule_time"], data["lines"])
        task.save_to_db()

        # run/schedule task
        # task_controller.run_task(task)
        task_controller.schedule_task(task)        

        return {"message": "Task created successfully."}, 201


class TaskList(Resource):
    @classmethod
    def get(cls):
        # @TODO add disruptions for tasks that have been run
        return {"tasks": [task.json() for task in TaskModel.find_all()]}

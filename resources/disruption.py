from flask_restful import Resource, reqparse
from models.disruption import DisruptionModel


class DisruptionCreate(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'category',
        type=str,
        required=False,
        help=""
        )
    parser.add_argument(
        'description',
        type=str,
        required=False,
        help=""
        )
    parser.add_argument(
        'task_id',
        type=int,
        required=False,
        help=""
        )
    
    # @classmethod
    # def get(cls, task_id):
    #     task = DisruptionModel.find_by_id(task_id)
    #     if task:
    #         return task.json()
    #     return {'message': 'Task not found'}, 404

    @classmethod
    def post(cls):
        data = DisruptionCreate.parser.parse_args()

        disruption = DisruptionModel(data["category"], data["description"], data["task_id"])
        disruption.save_to_db()

        return {"message": "Disruption created successfully."}, 201

    # @classmethod
    # def delete(cls, task_id):
    #     task = TaskModel.find_by_id(task_id)
    #     if task:
    #         task.delete_from_db()

    #     return {'message': 'Task deleted successfully.'}


# class DisruptionList(Resource):
#     @classmethod
#     def get(cls):
#         return {"tasks": [task.json() for task in TaskModel.find_all()]}


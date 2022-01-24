from flask_restful import Resource, reqparse
from models import disruption
from models.disruption import DisruptionModel


class Disruption(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "task_id",
        type=int,
        required=False,
        help=""
        )
    
    @classmethod
    def get(cls, task_id):
        disruption = DisruptionModel.find_by_task_id(task_id)
        if disruption:
            return disruption.json()
        return {"message": "Disruption not found. The tasks might not have been run."}, 404

    @classmethod
    def delete(cls, task_id):
        disruption = DisruptionModel.find_by_task_id(task_id)
        if disruption:
            disruption.delete_from_db()

        return {"message": "Disruption deleted successfully."}, 201


class DisruptionCreate(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "category",
        type=str,
        required=False,
        help=""
        )
    parser.add_argument(
        "description",
        type=str,
        required=False,
        help=""
        )
    parser.add_argument(
        "task_id",
        type=int,
        required=False,
        help=""
        )

    @classmethod
    def post(cls):
        data = DisruptionCreate.parser.parse_args()

        disruption = DisruptionModel(data["category"], data["description"], data["task_id"])
        disruption.save_to_db()

        return {"message": "Disruption created successfully."}, 201


class DisruptionList(Resource):
    @classmethod
    def get(cls):
        return {
            "disruptions": [disruption.json() for disruption in DisruptionModel.find_all()]
            }


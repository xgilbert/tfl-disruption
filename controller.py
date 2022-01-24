from datetime import datetime
import time
import sched
import threading
import logging

from tfl import TFL
from models.disruption import DisruptionModel

# make @staticmethod instead? unless add DTO and adapters?
class Controller:
    def run_task(self, task):
        task_id = task.id

        tfl = TFL()
        resp = tfl.get_disruptions(task.lines) # resp is array of JSON

        # @DEBUG
        logging.exception(task_id)
        logging.exception(task.schedule_time)
        logging.exception(task.lines)
        logging.exception(resp)

        for res in resp:
            category = res.get("category")
            description = res.get("description")
            
            disruption = DisruptionModel(
                task_id=task_id, category=category, description=description
                )
            disruption.save_to_db()


    def schedule_task(self, task):
        if task.schedule_time == "now":
            self.run_task(task)
        else:
            task_datetime = datetime.strptime(task.schedule_time, "%Y-%m-%dT%H:%M:%S")
            scheduler = sched.scheduler(time.time, time.sleep)
            task_event = scheduler.enter(
                (task_datetime - datetime.now()).seconds,
                1,
                self.run_task,
                (task,),
            )
            t = threading.Thread(target=scheduler.run)
            t.start()




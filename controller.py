from datetime import datetime
import time
import sched
import threading

from tfl import TFL
from models.disruption import DisruptionModel


class Controller:
    def run_task(self, task):
        tfl = TFL()
        resp = tfl.get_disruptions(task.lines)

        # @TODO @FIXME
        # array of JSON, not sure if several perturbations, in this case, loop through

        category = resp.get("category")
        description = resp.get("description")
        task_id = task.id

        disruption = DisruptionModel(category, description, task_id)
        disruption.save_to_db()


    def schedule_task(self, task):
        task_datetime = datetime.strptime(task.schedule_time, "%Y-%m-%dT%H:%M:%S")
        scheduler = sched.scheduler(time.time, time.sleep)
        task_event = scheduler.enter(
            (task_datetime - datetime.now()).seconds,
            1,
            self.execute_task,
            (task,),
        )
        t = threading.Thread(target=scheduler.run)
        t.start()




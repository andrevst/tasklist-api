from datetime import datetime

from flask import make_response, abort

def get_timestamp():
    return datetime.now().strftime(("%d-%m-%Y %H:%M:%S"))

# Data Mockup to serve with our API
TASKS = {
    "tarefa1": {
        "task_id" : "tarefa1",
        "tname": "lavar roupa",
        "tgroup": "Casa",
        "tdate": "10-02-2019",
        "done_flag": "y",
        "timestamp": get_timestamp()
    },
    "tarefa2": {
        "task_id" : "tarefa2",
        "tname": "API + WebApp deployed",
        "tgroup": "Oportunidades",
        "tdate": "10-02-2019",
        "done_flag": "n",
        "timestamp": get_timestamp()
    },
    "tarefa3": {
        "task_id" : "tarefa3",
        "tname": "Pegadinha no dia 01/04",
        "tgroup": "Brincadeira",
        "tdate": "01-04-2019",
        "done_flag": "n",
        "timestamp": get_timestamp()
    }
}

# Create a handler for our read (GET) task
def read():
    """
    This function responds to a request for /api/taks
    with the complete lists of tasks

    :return:        sorted list of tasks
    """
    # Create the list of tasks from our data
    return [TASKS[key] for key in sorted(TASKS.keys())]

def create(task):
    """
    This function creates a new task in the tasks structure
    based on the passed in task data
    :param task:  person to create in tasks structure
    :return:        201 on success, 406 on exists
    """
    task_id = task.get("task_id", None)
    tname = task.get("tname", None)
    tgroup = task.get("tgroup",None)
    tdate = task.get("tdate", None)
    doneflag = "n" 
    # user cannot create a done task

    # Does the task exist already?
    if task_id not in TASKS and task_id is not None:
        TASKS[task_id] = {
            "task_id": task_id,
            "tname": tname,
            "tgroup": tgroup,
            "tdate": tdate,
            "done_flag": doneflag,
            "timestamp": get_timestamp(),
        }
        return make_response(
            "{task_id} successfully created".format(task_id=task_id), 201
        )

    # Otherwise, it exists, that's an error
    else:
        abort(
            406,
            "Error, task id {task_id} already exists".format(task_id=task_id),
        )


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
    :param task:  task (to do item) to create in tasks structure
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

def read_a_task(task_id):
    """
    This function responds to a request for /api/task/{task_id}
    with one matching task from TASKS
    :param task_id:   unique identifier of a task
    :return:        task matching task_id
    """
    # Does the task exist in tasks?
    if task_id in TASKS:
        task = TASKS.get(task_id)

    # otherwise, nope, not found
    else:
        abort(
            404, "Task {task_id} not found".format(task_id=task_id)
        )

    return task

def update(task_id, task):
    """
    This function updates the status of an existing  in the task in the structure
    :param task_id:   unique identifier of a task
    :param task: unique task to update
    :return:        updated status at task structure
    """
    # Does the task exist in tasks?
    if task_id in TASKS:
        TASKS[task_id]["done_flag"] = task.get("done_flag")
        TASKS[task_id]["timestamp"] = get_timestamp()

        return TASKS[task_id]

    # otherwise, nope, that's an error
    else:
        abort(
            404, "Task {task_id} not found".format(task_id=task_id)
        )

def delete(task_id):
    """
    This function deletes a person from the tasks structure
    :param task_id:   unique identifier of a task
    :return:        200 on successful delete, 404 if not found
    """
    # Does the person to delete exist?
    if task_id in TASKS:
        del TASKS[task_id]
        return make_response(
            "{task_id} successfully deleted".format(task_id=task_id), 200
        )

    # Otherwise, nope, person to delete not found
    else:
        abort(
            404, "Task {task_id} not found".format(task_id=task_id)
        )

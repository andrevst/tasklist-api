from datetime import datetime

from flask import make_response, abort

from config import db
from models import (TaskList, TaskListSchema)

def get_timestamp():
    return datetime.now().strftime(("%d-%m-%Y %H:%M:%S"))


# Create a handler for our read (GET) task
def read():
    """
    This function responds to a request for /api/taks
    with the complete lists of tasks

    :return:        sorted list of tasks
    """
    # Create the list of tasks from our data
    tasks = TaskList.query.all()

    # Serialize the data for the response
    schema = TaskListSchema(many=True)
    data = schema.dump(tasks).data
    return data

def create(task):
    """
    This function creates a new task in the tasks structure
    based on the passed in task data
    :param task:  task (to do item) to create in tasks structure
    :return:        201 on success, 406 if task name is empty
    """
    tname = task.get("tname")
    # user cannot create task without name

    # Does the new task have a name? If no we can't insert it.
    # Can we insert it?
    if tname is not None:

        # Create a person instance using the schema and the passed in person
        schema = TaskListSchema()
        print(task)
        new_task = schema.load(task, session=db.session).data

        # Add the person to the database
        db.session.add(new_task)
        db.session.commit()

        # Serialize and return the newly created person in the response
        data = schema.dump(new_task).data

        return data, 201

    # Otherwise, nope, person exists already
    else:
        abort(409, "Task needs a name".format(tname=tname),)

def read_a_task(task_id):
    task = TaskList.query.filter(TaskList.task_id == task_id).one_or_none()

    # Check if it find a task
    if task is not None:

        # Serialize the data for the response
        schema = TaskListSchema()
        data = schema.dump(task).data
        return data

    # Otherwise, no, didn't find that task
    else:
        abort(
            404,
            "Task {task_id} not found".format(task_id=task_id),
        )

def update(task_id, task):
    """
    This function updates the status of an existing in the task in the structure
    :param task_id:   unique identifier of a task
    :param task: unique task to update
    :return:        updated status at task structure
    """
   # Get the task requested from the db into session
    update_task = TaskList.query.filter(TaskList.task_id == task_id).one_or_none()

    # Did we find the task?
    if update_task is not None: 

        # turn the passed in task into a db object
        schema = TaskListSchema()
        update = schema.load(task, session=db.session).data
        print(update)

        # Set the id to the task we want to update
        update.task_id = update_task.task_id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated task in the response
        data = schema.dump(update_task).data

        return data, 200
    # otherwise, nope, that's an error
    else:
        abort(
            404, "Task {task_id} not found".format(task_id=task_id),
        )

def delete(task_id):
    """
    This function deletes a task from the tasks structure
    :param task_id:   unique identifier of a task
    :return:        200 on successful delete, 404 if not found
    """
    # Get the task requested from the db into session
    delete_task = TaskList.query.filter(TaskList.task_id == task_id).one_or_none()

    # Did we find the task?
    if delete_task is not None: 
        db.session.delete(delete_task)
        db.session.commit()
        return make_response(
            "Task {task_id} deleted".format(task_id=task_id), 200
        )

    # Otherwise, nope, task to delete not found
    else:
        abort(
            404, "Task {task_id} not found".format(task_id=task_id)
        )

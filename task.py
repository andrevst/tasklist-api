from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%d-%m-%Y %H:%M:%S"))

# Data to serve with our API
TASKS = {
    "tarefa1": {
        "tname": "lavar roupa",
        "tgoup": "Casa",
        "tdate": "10-02-2019",
        "timestamp": get_timestamp()
    },
    "tarefa2": {
        "tname": "API + WebApp deployed",
        "tgoup": "Oportunidades",
        "tdate": "10-02-2019",
        "timestamp": get_timestamp()
    },
    "tarefa3": {
        "tname": "Pegadinha no dia 01/04",
        "tgoup": "Brincadeira",
        "tdate": "01-04-2019",
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

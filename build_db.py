import os
from config import db
from models import TaskList
from datetime import datetime

# Data to initialize database with
TASKS = [
     {
        "tname": "lavar roupa",
        "tgroup": "Casa",
        "tdate": datetime(2019, 3, 3, 10, 10, 10),
        "done_flag": "y"
    },
    {
        "tname": "API + WebApp deployed",
        "tgroup": "Oportunidades",
        "tdate": datetime(2019, 1, 4, 10, 10, 10),
        "done_flag": "n"
    },
    {
        "tname": "Pegadinha no dia 01/04",
        "tgroup": "Brincadeira",
        "tdate": datetime(2012, 3, 3, 10, 10, 10),
        "done_flag": "n"
    }
]

# Delete database file if it exists currently
if os.path.exists('tasks.db'):
    os.remove('tasks.db')

# Create the database
db.create_all()

# Iterate over the TASKS structure and populate the database
for task in TASKS:
    t = TaskList(tname=task['tname'], tgroup=task['tgroup'],
    tdate=task['tdate'], done_flag=task['done_flag'])
    db.session.add(t)

db.session.commit()

# tasklist-api

 This is a REST API providing access to a collection of tasks with CRUD access to an individual task within that collection. Here’s the API design:

**Action**|**HTTP Verb**|**URL Path**|**Description**
:-----:|:-----:|:-----:|:-----:
Create|POST|/api/task|Defines a unique URL to create a new task
Read|GET|/api/task|Defines a unique URL to read a collection of tasks
Read|GET|/api/task/taskId|Defines a unique URL to read a particular person in the task collection
Update|PUT|/api/task/{task_id}|Defines a unique URL to update an existing task
Delete|DELETE|/api/orders/{task_id}|Defines a unique URL to delete an existing task

This API provides data for an application based on the following mockup:
![Task App Mockup - Gerdau Challenge](https://i.imgur.com/AUOUzkP.png)

## Used Technologies:

 - Python 3.6
   - Flask 
   - Connexion
   -  SQLAlchemy
   -   Marshmallow 
  -   flask-cors library to set CORS(Cross-origin resource sharing) headers
 - Swagger
 - SQLite 3

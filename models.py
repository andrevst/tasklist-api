from datetime import datetime
from config import db, ma

class TaskList(db.Model):
    __tablename__ = 'task'
    task_id = db.Column(db.Integer, primary_key=True)
    tgroup = db.Column(db.String(32))
    tname = db.Column(db.String(128), index=True)
    tdate = db.Column(db.Date)
    done_flag = db.Column(db.String(1))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class TaskListSchema(ma.ModelSchema):
    class Meta:
        model = TaskList
        sqla_session = db.session   

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TaskTypeDto(Base):
    __tablename__ = 'TaskType'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
       return "<TaskType(name='%s')>" % (self.name)

class TaskDto(Base):
    __tablename__ = 'Task'
    id = Column(Integer, primary_key=True)
    taskType = Column(Integer, ForeignKey('TaskType.id'))
    text = Column(String)

    def __repr__(self):
       return "<Task(taskType='%s', text='%s', nickname='%s')>" % (self.taskType, self.text)

def createDefaultModels(session):
    taskTypes = session.query(TaskType)
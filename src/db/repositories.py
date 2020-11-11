from src.tasks.task_type import TaskType
from src.db.dtos import TaskTypeDto

class TaskRepository():
    def __init__(self, dbManager):
        self.dbManager = dbManager

    def createTask(self, task):
        taskString = self._taskTypeToString(task.taskType)

        with self.dbManager.connect() as session: 
            taskTypeID = self._getTaskTypeID(taskString, session)
            task = TaskDto(taskType=taskTypeID, text=task.name)
            session.add(taskTypeDto)
    
    def _getTaskTypeID(self, name, session):
        taskTypeDto = session.query(TaskTypeDto).filter_by(name=name).first()

        if taskTypeDto == None:
            taskTypeDto = TaskTypeDto(name=name)
            session.add(taskTypeDto)
            session.commit()
        
        return taskTypeDto.id

    def _taskTypeToString(self, taskType):
        if taskType == TaskType.TEXT:
            return "text"
        elif taskType == TaskType.REMINDER:
            return "reminder"
        else:
            raise Exception("TaskType " + taskType + " not recognized")
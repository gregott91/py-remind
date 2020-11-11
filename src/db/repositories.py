from src.tasks import TaskType
from src.db.dtos import TaskTypeDto, TaskDto

class TaskRepository():
    def __init__(self, dbManager, taskTypeRepository):
        self.dbManager = dbManager
        self.taskTypeRepository = taskTypeRepository

    def createTask(self, task):
        taskType = self.taskTypeRepository.getTaskType(task.taskType)

        with self.dbManager.connect() as session: 
            task = TaskDto(taskType=taskType.id, text=task.text)
            session.add(task)

class TaskTypeRepository():
    def __init__(self, dbManager):
        self.dbManager = dbManager

    def getTaskType(self, taskType):
        taskString = self._taskTypeToString(taskType)

        taskTypeDto = None
        with self.dbManager.connect() as session: 
            taskTypeDto = session.query(TaskTypeDto).filter_by(name=taskString).first()

            if taskTypeDto == None:
                taskTypeDto = TaskTypeDto(name=taskString)
                session.add(taskTypeDto)
                session.commit()
        
        return taskTypeDto

    def _taskTypeToString(self, taskType):
        if taskType == TaskType.TEXT:
            return "text"
        elif taskType == TaskType.REMINDER:
            return "reminder"
        else:
            raise Exception("TaskType " + taskType + " not recognized")
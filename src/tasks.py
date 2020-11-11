from enum import Enum

class TextTask():
    def __init__(self, text):
        self.text = text
        self.taskType = TaskType.TEXT

    def save(self, taskRepository):
        taskRepository.createTask(self)

class TaskType(Enum):
    TEXT = 1
    REMINDER = 2
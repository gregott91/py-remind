from src.tasks.task_type import TaskType

class TextTask():
    def __init__(self, text):
        self.text = text
        self.taskType = TaskType.TEXT

    def save(self, taskRepository):
        taskRepository.createTask(self)

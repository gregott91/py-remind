import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../..")

import unittest
from tests.data.data_tests_base import DataTestsBase
from src.db.connections import DBManager, DBOptions
from src.db.repositories import TaskTypeRepository
from src.tasks import TaskType

class DataTestsBase(DataTestsBase):
    def setUp(self):
        super().setUp()
        self.taskTypeRepository = TaskTypeRepository(self.dbManager)

    def test_gets_task_type(self):
        taskType = self.taskTypeRepository.getTaskType(TaskType.REMINDER)
        self.assertIsNotNone(taskType.id)

    def test_persists_task(self):
        taskTypeOne = self.taskTypeRepository.getTaskType(TaskType.REMINDER)
        taskTypeTwo = self.taskTypeRepository.getTaskType(TaskType.REMINDER)
        self.assertEqual(taskTypeOne.id, taskTypeTwo.id)

if __name__ == '__main__':
    unittest.main()
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../..")

import unittest
from src.db.connections import DBManager, DBOptions

class DataTestsBase(unittest.TestCase):
    def setUp(self):
        self.options = DBOptions('sqlite:///test.db', True)
        self.dbManager = DBManager(self.options)
        self.dbManager.initialize()

    def tearDown(self):
        dbPath = os.path.dirname(os.path.realpath(__file__)) + "/../../test.db"
        os.remove(dbPath)
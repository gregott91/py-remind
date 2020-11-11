import sys
from PyQt5.QtWidgets import QApplication
from src.configuration.configurator import configureUI
from src.listeners.exit_listener import ExitListener
from src.listeners.text_listener import TextListener
from src.db.connections import DBManager
from src.db.repositories import TaskRepository

app = QApplication([])
db = 'sqlite:///local.db'
dbManager = DBManager(db)
dbManager.initialize()
taskRepo = TaskRepository(dbManager)

exitListener = ExitListener(app)
textListener = TextListener(taskRepo)

window = configureUI(app, exitListener, textListener)
window.show()

sys.exit(app.exec_())

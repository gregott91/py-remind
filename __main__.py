import sys
from PyQt5.QtWidgets import QApplication
from src.configuration.configurator import configureUI, configureHotKeys

app = QApplication([])

configureHotKeys(app)

sys.exit(app.exec())

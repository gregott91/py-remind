import sys
from PyQt5.QtWidgets import QApplication
from src.configuration.configurator import configureUI
from src.listeners.exit_listener import ExitListener
from src.listeners.text_listener import TextListener

app = QApplication([])

exitListener = ExitListener(app)
textListener = TextListener()

window = configureUI(app, exitListener, textListener)
window.show()

sys.exit(app.exec_())
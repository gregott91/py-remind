from PyQt5.QtCore import Qt

class ExitListener():
    def __init__(self, app):
        self.app = app
    
    def subscribe(self, observable):
        observable.subscribe(self.keyChanged)

    def keyChanged(self, key):
        if key == Qt.Key_Escape:
            self.app.quit()
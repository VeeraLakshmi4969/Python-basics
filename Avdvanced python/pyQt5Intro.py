# PyQt5 introduction
import sys

from PyQt5.QtGui import QIcon
# This module(system) provides access to some variables used or maintained by the python interpreter
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")
        self.setWindowIcon(QIcon("1mb photo.jpg"))
        self.setGeometry(0,100,500,200)
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()

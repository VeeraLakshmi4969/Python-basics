# PyQt5 introduction
import sys

from PyQt5.QtGui import QIcon
# This module(system) provides access to some variables used or maintained by the python interpreter
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")
        self.setWindowIcon(QIcon("1mb photo.jpg"))
        self.setGeometry(0,100,500,200)

        label = QLabel ("This is a  label", self)
        label.setFont(QFont("Times New Roman",20))
        label.setGeometry(30,2,400,100)
        label.setStyleSheet("color: Blue;"
                            "background-color: pink;"
                            "text-decoration: underline;"
                            "font-weight: bold;")

        # label.setAlignment(Qt.AlignLeft)
        # label.setAlignment(Qt.AlignRight)
        # label.setAlignment(Qt.AlignTop)
        # label.setAlignment(Qt.AlignBottom)
        # label.setAlignment(Qt.AlignHCenter)
        # label.setAlignment(Qt.AlignVCenter)
        # label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        # label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter) OR
        label.setAlignment(Qt.AlignCenter)
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()

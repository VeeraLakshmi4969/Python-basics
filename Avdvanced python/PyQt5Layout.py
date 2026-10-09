import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("First", self)
        label2 = QLabel("Second", self)
        label3 = QLabel("Third", self)
        label4 = QLabel("Fourth", self)
        label5 = QLabel("Fifth", self)

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: blue;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: yellow;")
        label5.setStyleSheet("background-color: pink;")

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)
        central_widget.setLayout(vbox)
        # grid = QGridLayout()
        # grid.addWidget(label1,0,0)
        # grid.addWidget(label2,1,0)
        # grid.addWidget(label3,1,1)
        # grid.addWidget(label4,0,1)
        # grid.addWidget(label5,2,2)
        # central_widget.setLayout(grid)
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
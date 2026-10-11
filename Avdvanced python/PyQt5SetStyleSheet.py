# PyQt5 setStyleSheet()

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        central_widget.setLayout(hbox)

        self.setStyleSheet("""
            QPushButton {
                font-size: 40px; 
                font-family: Arial; 
                padding: 15px 75px; 
                margin: 25px; 
                border: 3px solid black; 
                border-radius: 15px;
            } 
            QPushButton#button1 { background: red; } 
            QPushButton#button2 { background: blue; } 
            QPushButton#button3 { background: pink; }

            QPushButton#button1:hover { background: darkred; } 
            QPushButton#button2:hover { background: darkblue; } 
            QPushButton#button3:hover { background: hotpink; }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()  # Use your custom MainWindow class here
    window.show()
    sys.exit(app.exec_())
# PyQt5 LineEdit Side by Side

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QPushButton, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("LineEdit Example")
        self.setGeometry(600, 400, 400, 120)

        # Create a central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Style the widgets
        self.line_edit.setStyleSheet("font-size: 25px; font-family: Arial;")
        self.button.setStyleSheet("font-size: 25px; font-family: Arial;")
        self.line_edit.setPlaceholderText("Enter your name")

        # --- USE QHBoxLayout FOR SIDE-BY-SIDE ALIGNMENT ---
        layout = QHBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)

        central_widget.setLayout(layout)

        # Connect button click signal
        self.button.clicked.connect(self.submit)

    def submit(self):
        text = self.line_edit.text()
        print(f"Hello {text}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
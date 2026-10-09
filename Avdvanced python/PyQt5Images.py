# PyQt5 images
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,500,500)

        label = QLabel(self)
        label.setGeometry(10,20,400,450)
        pixmap = QPixmap("1mb photo.jpg")
        label.setPixmap(pixmap)
        label.setScaledContents(True)

        label.setGeometry((self.width()-label.width())//2,
                          (self.width()-label.height())//2,
                          label.width(),
                          label.height())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
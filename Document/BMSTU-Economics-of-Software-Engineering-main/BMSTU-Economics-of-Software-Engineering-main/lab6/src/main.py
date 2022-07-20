from controllers.mainwindow_ctrl import CocomoMainwindow
from PyQt5.QtWidgets import QApplication
import sys


def main():
    app = QApplication(sys.argv)
    window = CocomoMainwindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()

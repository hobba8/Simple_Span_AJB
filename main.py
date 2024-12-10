'''
Adam Becker
1620
12/09/2024
'''


from PyQt6.QtWidgets import QApplication
from logic import *


def main():
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
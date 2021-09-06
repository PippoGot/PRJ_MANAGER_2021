from PyQt5 import QtWidgets as qtw

from windows.main.main_window import MainWindow

if __name__ == '__main__':
    import sys
    app = qtw.QApplication(sys.argv)

    mw = MainWindow(app)
    mw.show()

    app.exec_()
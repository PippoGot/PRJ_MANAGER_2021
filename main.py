# --- LIBRARIES ---
from PyQt5 import QtWidgets as qtw
import sys
# --- CUSTOM MODULES ---
from windows.main.main_window import MainWindow

def main():
    app = qtw.QApplication(sys.argv)

    mw = MainWindow(app)
    mw.show()

    app.exec_()

if __name__ == '__main__':
    main()
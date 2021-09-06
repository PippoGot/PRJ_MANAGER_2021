from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

from .ui_comp_editor import  Ui_comp_editor as ui

class CompEditor(qtw.QWidget, ui):
    """
    Popup window to edit a node before adding it to the component tree.
    Provides all the necessary widgets to edit a component node.
    """

    submit = qtc.pyqtSignal(object)

    def __init__(self):
        """
        Loads the UI window and connects the buttons signals to the proper slots.

        Args:
            node (ComponentNode): the node to edit in this window
        """

        super(CompEditor, self).__init__()
        self.setupUi(self)

        self.uiBtnCancel.clicked.connect(self.close)
        self.uiBtnOk.clicked.connect(self.submit_data)

        self.show()

    def submit_data(self):
        """
        Emits the data inserted in the editor.
        """

        data = [
            self.uiLEName.text(),
            self.uiTEDesc.toPlainText()
        ]

        self.submit.emit(data)
        self.close()
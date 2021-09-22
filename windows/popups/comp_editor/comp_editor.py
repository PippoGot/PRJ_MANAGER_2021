# libraries
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
# custom modules
from .ui_comp_editor import  Ui_comp_editor as ui

class CompEditor(qtw.QWidget, ui):
    """
    Popup window to edit a component before adding it to the model.
    Provides all the necessary widgets to edit a component.
    """

    submit = qtc.pyqtSignal(object) # emits all the data

    def __init__(self):
        """Loads the UI window, connects signals to slots and show itself."""

        super(CompEditor, self).__init__()
        self.setupUi(self)

        self.uiBtnCancel.clicked.connect(self.close)
        self.uiBtnOk.clicked.connect(self._submit_data)

        self.show()

    def _submit_data(self):
        """Emits the data inserted in the editor, then closes the popup."""

        data = {
            'name': self.uiLEName.text(),
            'desc': self.uiTEDesc.toPlainText()
        }

        self.submit.emit(data)
        self.close()

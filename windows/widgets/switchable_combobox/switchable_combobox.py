# --- LIBRARIES ---
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
# --- CUSTOM MODULES ---
from .ui_switchable_combobox import  Ui_SwitchableCombobox as ui

class SwitchableCombobox(qtw.QWidget, ui):

    def __init__(self):
        """Loads the UI."""

        super(SwitchableCombobox, self).__init__()
        self.setupUi(self)

        self.model = None
        self._is_editable = True
        self.set_editable(self._is_editable)

    def set_editable(self, editability: bool) -> None:
        """Changes the editability ogf the widget."""

        self._is_editable = editability

        if self._is_editable:
            self.stacked_widget.setCurrentIndex(1)
        else:
            self.stacked_widget.setCurrentIndex(0)

    def set_model(self, model):
        """Sets the model of the combobox."""

        self.model = model

    def set_text(self, text_value):
        """Sets the text to display in the line edit."""

        self.line_edit.setText(text_value)

    def get_text(self):
        """Returns the text currently on the line edit."""

        return self.line_edit.text()

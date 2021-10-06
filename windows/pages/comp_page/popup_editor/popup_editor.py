# libraries
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
# custom modules
from .ui_popup_editor import  Ui_popup_editor as ui
from core.enums import get_enum
from core.components.components_factory import create_default_component
from ....widgets.switchable_combobox.switchable_combobox import SwitchableCombobox

class PopupEditor(qtw.QWidget, ui):
    """
    Popup window to edit a component before adding it to the model.
    Provides all the necessary widgets to edit a component.
    """

    submit = qtc.pyqtSignal(object) # emits all the data

    def __init__(self, type_string):
        """Loads the UI window, connects signals to slots and show itself."""

        super(PopupEditor, self).__init__()
        self.setupUi(self)

        # self.tag_string = tag_string
        self.type_enum = get_enum(type_string)

        self.manufacture_entries_model = qtc.QStringListModel()
        self.manufacture_widget = SwitchableCombobox()
        self.manufacture_widget.set_model(self.manufacture_entries_model)
        self.uiManufactureFrame.layout().addWidget(self.manufacture_widget)

        self.status_entries_model = qtc.QStringListModel()
        self.status_widget = SwitchableCombobox()
        self.status_widget.set_model(self.status_entries_model)
        self.uiStatusFrame.layout().addWidget(self.status_widget)

        self.uiBtnCancel.clicked.connect(self.close)
        self.uiBtnOk.clicked.connect(self._submit_data)

        self._init_data()
        self._set_mode(type_string)
        self.show()

    def _init_data(self):
        """Fills in the widgets with data."""

        # self.uiTagDisplay.setText(self.tag_string)
        type_string = self.type_enum.value.lower()
        component = create_default_component(type_string)
        component_data = component.as_dict()

        self.uiNameEdit.setText(component_data['name'])
        self.uiDescEdit.setPlainText(component_data['desc'])
        self.uiCommentEdit.setPlainText(component_data['comment'])
        self.uiTypeDisplay.setText(self.type_enum.value)
        self.status_widget.set_text(component_data['status'].name.title())
        self.manufacture_widget.set_text(component_data['manufacture'].value)
        self.uiQtyEdit.setValue(1)
        self.uiCostEdit.setText('0.00')

    def _set_mode(self, type_string: str) -> None:
        """Changes the editor mode based on the type of component passed."""

        modes = {
            'project': self._mode_project,
            'placeholder': self._mode_poject,

            'assembly': self._mode_assembly,

            'jig': self._mode_leaf,
            'part': self._mode_leaf
        }

        mode = modes[type_string]()

    def _submit_data(self) -> None:
        """Emits the data inserted in the editor, then closes the popup."""

        data = {
            'name': self.uiNameEdit.text(),
            'desc': self.uiDescEdit.toPlainText(),
            'comment': self.uiCommentEdit.toPlainText(),
            'tp': self.type_enum,
            'status': self.status_widget.get_text(),
            'manufacture': self.manufacture_widget.get_text(),
            'qty': self.uiQtyEdit.value(),
            'cost': self.uiCostEdit.text()
        }

        self.submit.emit(data)
        self.close()

    # --- EDITOR MODES ---

    def _mode_project(self) -> None:
        """
        Changes the mode to the following rules:

        manufacture = not editable
        status = not editable
        cost = not editable
        """

        self.manufacture_widget.set_editable(False)
        self.status_widget.set_editable(False)
        self.uiCostEdit.setReadOnly(True)

    def _mode_assembly(self) -> None:
        """
        Changes the mode to the following rules:

        manufacture = not editable
        status = editable
        cost = not editable
        """

        self.manufacture_widget.set_editable(False)
        self.status_widget.set_editable(True)
        self.uiCostEdit.setReadOnly(True)

    def _mode_leaf(self) -> None:
        """
        Changes the mode to the following rules:

        manufacture = not editable
        status = editable
        cost = not editable
        """

        self.manufacture_widget.set_editable(True)
        self.status_widget.set_editable(True)
        self.uiCostEdit.setReadOnly(False)

# --- LIBRARIES ---
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
# --- CUSTOM MODULES ---
from .ui_comp_editor import  Ui_CompEditor as ui

class CompEditor(qtw.QWidget, ui):
    """Class for the component editor on the side of component page."""

    def __init__(self):
        """Loads the UI window and initialise the class variables."""

        super(CompEditor, self).__init__()
        self.setupUi(self)

        self.mapper = qtw.QDataWidgetMapper()
        self.set_model()

# --- MODELS MANAGEMENT ---

    def set_model(self, model = None):
        """Sets the editor model."""

        self.model = model
        self.current_index = qtc.QModelIndex()

        if self.model:
            self._map_editor_widgets()

    def _map_editor_widgets(self):
        """Initialize and connects the mapper to the widgets."""

        self.mapper.setModel(self.model)

        # general component info
        self.mapper.addMapping(self.uiNameEdit, 0)
        self.mapper.addMapping(self.uiDescEdit, 1)
        self.mapper.addMapping(self.uiCommentEdit, 2)
        self.mapper.addMapping(self.uiTypeDisplay, 3)
        self.mapper.addMapping(self.uiStatusDisplay, 4)
        self.mapper.addMapping(self.uiStatusEdit, 4)
        self.mapper.addMapping(self.uiManufactureDisplay, 5)
        self.mapper.addMapping(self.uiManufactureEdit, 5)
        self.mapper.addMapping(self.uiQtyEdit, 6)
        self.mapper.addMapping(self.uiCostEdit, 7)

        # purchasable component info
        self.mapper.addMapping(self.uiQtyPkgDisplay, 8)
        self.mapper.addMapping(self.uiSellerDisplay, 9)
        self.mapper.addMapping(self.uiLinkDisplay, 10)

    def update_current_index(self, new_index):
        """The new index is set as the current index of the editor."""

        self.current_index = new_index
        if not self.current_index.isValid(): return

        parent_index = self.current_index.parent()
        self.mapper.setRootIndex(parent_index)
        self.mapper.setCurrentModelIndex(self.current_index)

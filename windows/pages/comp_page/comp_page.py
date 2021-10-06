# --- LIBRARIES ---
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
# --- CUSTOM MODULES ---
from .ui_comp_page import  Ui_CompPage as ui
from .popup_editor.popup_editor import PopupEditor
from .comp_editor.comp_editor import CompEditor
from ..page_template import PageTemplate

class CompPage(PageTemplate, ui):
    """
    Main CompPage, displays the current working component tree and provides a
    component editor to edit the inserted nodes. Offers a toolkit of functions to
    add remove and swap nodes in the CompModel.
    Uses the CompEditor widget.
    """

    def __init__(self, comp_model):
        """Loads the UI window, generates the actions and sets the model."""

        super(CompPage, self).__init__()
        self.setupUi(self)

        self.comp_index = None
        self.comp_selection = None

        self.comp_editor = CompEditor()
        self.layout().addWidget(self.comp_editor)

        self.set_model(comp_model)

        self._create_actions()

# --- MODELS MANAGEMENT ---

    def set_model(self, comp_model):
        """Sets the editor's and view's model."""

        self.comp_model = comp_model
        self.uiCompView.setModel(self.comp_model)
        self.comp_editor.set_model(self.comp_model)

        if self.comp_model:
            self.comp_selection = self.uiCompView.selectionModel()
            self.comp_selection.currentChanged.connect(self._update_current_index)

    def _update_current_index(self, new_index):
        """Updates the current selected index."""

        self.comp_index = new_index
        self.comp_editor.update_current_index(new_index)

# --- EDIT ACTIONS ---

    def _open_editor(self):
        """Opens an editor popup to input the component data."""

        if not self.comp_index.isValid(): return

        action = self.sender()
        type_string = action.data()
        self.popup_editor = PopupEditor(type_string)
        self.popup_editor.submit.connect(self._add_node)

        component = self.comp_index.internalPointer()
        self.new_component_tag = component.increment(1)
        tag_string = self.new_component_tag.get_tag_string()

    def _add_node(self, data):
        """Adds the passed data to the model."""

        if not self.comp_model: return

        current_comp = self.comp_index.internalPointer()
        self.comp_model.insertRows(data, self.new_component_tag, self.comp_index)

    def _remove_node(self):
        """Removes the currently selected index from the model."""

        if not self.comp_index.isValid(): return

        self.comp_model.removeRows(self.comp_index)

# --- ACTIONS HANDLING ---

    def _create_actions(self):
        """Creates all of the actions usable in this page."""

        self.menuAddComponent = qtw.QMenu('Add Component')
        self.actions.append(self.menuAddComponent.menuAction())

        # --- ADD COMPONENT SUB-ACTIONS ---

        self.actAssembly = qtw.QAction('Assembly')
        self.actAssembly.triggered.connect(self._open_editor)
        self.actAssembly.setData('assembly')
        self.menuAddComponent.addAction(self.actAssembly)

        self.actPart = qtw.QAction('Part')
        self.actPart.triggered.connect(self._open_editor)
        self.actPart.setData('part')
        self.menuAddComponent.addAction(self.actPart)

        self.actJig = qtw.QAction('Jig')
        self.actJig.triggered.connect(self._open_editor)
        self.actJig.setData('jig')
        self.menuAddComponent.addAction(self.actJig)

        self.actPlaceholder = qtw.QAction('Placeholder')
        self.actPlaceholder.triggered.connect(self._open_editor)
        self.actPlaceholder.setData('placeholder')
        self.menuAddComponent.addAction(self.actPlaceholder)

        #--------------------------------------------------------------

        self.actRemoveComponent = qtw.QAction('Remove Component')
        self.actRemoveComponent.triggered.connect(self._remove_node)
        self.actions.append(self.actRemoveComponent)

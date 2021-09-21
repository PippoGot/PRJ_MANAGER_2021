# --- LIBRARIES ---
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
import os
# --- CUSTOM MODULES ---
# popups
from ..popups.comp_editor.comp_editor import CompEditor
# core
from core.components.components import Component
# models
from models.comp_model import CompModel
# UI
from .ui_main_window import Ui_MainWindow as ui

# --- CLASS ---
class MainWindow(qtw.QMainWindow, ui):

    def __init__(self, application):
        """Loads the UI window and creates the component model."""

    # ui setup
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.application = application

    # model creation
        self.comp_model = CompModel()
        self.uiCompView.setModel(self.comp_model)
        self.comp_selection = self.uiCompView.selectionModel()
        self.comp_index = None
        self.comp_selection.currentChanged.connect(self._update_current_index)

    # edit menu action connection
        self.uiActAddNode.triggered.connect(self.open_editor)
        self.uiActRemoveNode.triggered.connect(self.remove_node)

    def open_editor(self):
        """Opens an editor popup to input the component data."""

        self.comp_index = self.comp_selection.currentIndex()
        if not self.comp_index.isValid(): return

        self.comp_editor = CompEditor()
        self.comp_editor.submit.connect(self.add_node)

    def add_node(self, data):
        """Creates a component out of the passed data and adds it to the model."""

        new_node = Component(*data)

        current_comp = self.comp_index.internalPointer()
        self.comp_model.insertRows(new_node, self.comp_index)

    def remove_node(self):
        """Removes the currently selected node from the model."""

        if not self.comp_index.isValid(): return

        position = self.comp_index.row()
        self.comp_model.removeRows(position, self.comp_index.parent())

    def _update_current_index(self):
        """Updates the current selected index."""

        self.comp_index = self.comp_selection.currentIndex()

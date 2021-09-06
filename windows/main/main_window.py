# LIBRARIES
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
import os

# UI
from .ui_main_window import Ui_MainWindow as ui

# popups
from ..popups.comp_editor.comp_editor import CompEditor

# core
from core.nodes.nodes import Component
# models
from models.comp_model import CompModel

# --- CLASS ---
class MainWindow(qtw.QMainWindow, ui):
    def __init__(self, application):
        """
        Loads the UI window.
        """
    # ui setup
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.application = application

    # model creation
        self.compModel = CompModel()
        self.uiCompView.setModel(self.compModel)
        self.compSelection = self.uiCompView.selectionModel()

    # edit menu action connection
        self.uiActAddNode.triggered.connect(self.open_editor)
        self.uiActRemoveNode.triggered.connect(self.remove_node)

    def open_editor(self):
        self.compIndex = self.compSelection.currentIndex()
        if not self.compIndex.isValid(): return

        self.comp_editor = CompEditor()
        self.comp_editor.submit.connect(self.add_node)

    def add_node(self, data):
        new_node = Component(*data)

        currentComp = self.compIndex.internalPointer()
        position = len(currentComp)

        self.compModel.insertRows(position, new_node, self.compIndex)

    def remove_node(self):
        if not self.compIndex.isValid(): return

        position = self.compIndex.row()
        self.compModel.removeRows(position, self.compIndex)

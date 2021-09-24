# --- LIBRARIES ---
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
# --- CUSTOM MODULES ---
# widgets
from ..pages.comp_page.comp_page import CompPage
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
        self._generate_models()

    # page creation
        self._generate_pages()

    def _generate_models(self):
        """Generates all of the needed models."""

        self.comp_model = CompModel()

    def _generate_pages(self):
        """Generates the pages and adds them to the layout."""

        self.comp_page = CompPage(self.comp_model)
        self.uiCompPageFrame.layout().addWidget(self.comp_page)
        comp_page_action_list = self.comp_page.get_actions()

        self._add_actions(comp_page_action_list)

    def _add_actions(self, actions_list):
        """Extract and adds the actions from the pages to the menus."""

        for action in actions_list:
            self.uiMenuEdit.addAction(action)

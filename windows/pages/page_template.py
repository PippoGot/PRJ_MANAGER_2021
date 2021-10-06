# --- LIBRARIES ---
from PyQt5 import QtWidgets as qtw

class PageTemplate(qtw.QWidget):
    """Class for the basic template of a page with actions relative to only that page."""

    actions = []

    def _create_actions(self):
        """Creates all of the actions usable in this page."""

        raise NotImplementedError()

    def get_actions(self):
        """Returns the actions usable in this page:"""

        return self.actions
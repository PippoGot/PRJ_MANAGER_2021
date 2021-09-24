# --- LIBRARIES ---
from PyQt5 import QtCore as qtc
from typing import Any, Optional, Dict, List
# --- CUSTOM MODULES ---
from core.components.components import Component
from core.components.nodes import Node

class CompModel(qtc.QAbstractItemModel):
    """
    This class manages the model storing the main data structure
    of an assembly project.
    """

    def __init__(self, root: Optional[Component] = None) -> None:
        """Initialise the object parameters."""

        super(CompModel, self).__init__()

        self._init_base_components(root)
        self._retrieve_headers()

# --- INIT CUSTOM FUNCTIONS ---

    def _init_base_components(self, root: Optional[Component]) -> None:
        """Generates the initial components of the model."""

        if root:
            self.root = root
        else:
            self.root = Component(name='root', desc='no description')

        self.first = Component(name='Project', desc='Top level node, describe the project here!')
        self.root.add_child(self.first)

    def _retrieve_headers(self) -> None:
        """Extracts the headers from the root component after it is created."""

        self.HEADERS = self.root.get_fields_tuple()

# --- MODEL FUNCTIONS OVERWRITING ---

    def data(self, index, role):
        """
        Returns the data stored under the given role for the component referred to
        by the index.
        """

        if not index.isValid():
            return None

        component = index.internalPointer()

        if role == qtc.Qt.DisplayRole or role == qtc.Qt.EditRole:
            field = self.HEADERS[index.column()]
            return component.get_field(field)

    def setData(self, index, value, role = qtc.Qt.EditRole):
        """Used to edit and update the model items values."""

        if index.isValid() and role == qtc.Qt.EditRole:
            component = index.internalPointer()
            field = self.HEADERS[index.column()]

            component.replace_field(field, value)

            self.dataChanged.emit(index, index)
            return True
        return

    def flags(self, index):
        """
        Returns the item flags for the given index. This tells the program
        what can be done with the model items.
        """

        if not index.isValid():
            return qtc.Qt.NoItemFlags
        return qtc.Qt.ItemIsEnabled | qtc.Qt.ItemIsSelectable | qtc.Qt.ItemIsEditable

    def headerData(self, section, orientation, role):
        """
        Turns the data for the given role and section in the header with the specified orientation.
        For horizontal headers, the section number corresponds to the column number. Similarly, for
        vertical headers, the section number corresponds to the row number.
        The headers are taken from a list of string values.
        """

        if orientation == qtc.Qt.Horizontal and role == qtc.Qt.DisplayRole:
            return self.HEADERS[section].title()
        return None

    def index(self, row, column, parent_index):
        """
        Returns the index of the component in the model specified by the given row,
        column and parent index.

        When reimplementing this function in a subclass, call createIndex() to generate
        model indexes that other classes can use to refer to items in your model.
        """

        if not self.hasIndex(row, column, parent_index):
            return qtc.QModelIndex()
        elif not parent_index.isValid():
            parent_component = self.root
        else:
            parent_component = parent_index.internalPointer()

        child_component = parent_component.get_child_at(row)

        if child_component:
            return self.createIndex(row, column, child_component)

        return qtc.QModelIndex()

    def parent(self, index):
        """
        Returns the parent index of the model component with the given index.
        If the component has no parent, an invalid QModelIndex is returned.
        A common convention used in models that expose tree data structures is
        that only items in the first column have children.
        For that case, when reimplementing this function in a subclass the column of
        the returned QModelIndex would be 0.

        When reimplementing this function in a subclass, be careful to avoid calling
        QModelIndex member functions, such as parent(), since indexes belonging to
        your model will simply call your implementation, leading to infinite recursion.
        """

        if not index.isValid():
            return qtc.QModelIndex()

        child_component = index.internalPointer()
        parent_component = child_component.get_parent()

        if not parent_component:
            return qtc.QModelIndex()

        row = parent_component.get_row()
        return self.createIndex(row, 0, parent_component)

    def rowCount(self, parent_index):
        """
        Returns the number of rows under the given parent. When the parent is valid it means
        that is returning the number of children of parent.
        """

        if parent_index.column() > 0:
            return 0

        if not parent_index.isValid():
            parent_component = self.root
        else:
            parent_component = parent_index.internalPointer()

        return len(parent_component)

    def columnCount(self, parent_index):
        """
        Returns the number of columns for the children of the given parent.
        In most subclasses, the number of columns is independent of the parent.
        """

        return len(self.HEADERS)

    def insertRows(self, data_dict, parent_index = qtc.QModelIndex()):
        """
        Insert a node row in the specified position.
        """

        if parent_index.isValid():
            parent_component = parent_index.internalPointer()
        else:
            parent_component = self.first

        position = len(parent_component)

        self.beginInsertRows(parent_index.siblingAtColumn(0), position, position)

        component = self._data_to_component(data_dict)
        success = parent_component.add_child(component)

        self.endInsertRows()

        return success

    def removeRows(self, component_index = qtc.QModelIndex()):
        """
        Remove the row in the specified position.
        """

        parent_index = component_index.parent()
        position = component_index.row()

        if parent_index.isValid():
            parent_component = parent_index.internalPointer()
        else:
            parent_component = self.root

        self.beginRemoveRows(parent_index.siblingAtColumn(0), position, position)
        success = parent_component.remove_child_at(position)
        self.endRemoveRows()

        return success

# --- CUSTOM FUNCTIONS ---

    def _data_to_component(self, data_dict: Dict[str, Any]) -> Component:
        """Converts a data dictionary to a Component instance."""

        return Component(**data_dict)

    def get_components_list(self) -> List[Node]:
        """Returns the list of components inside the model."""

        return self.root.get_subtree_components()

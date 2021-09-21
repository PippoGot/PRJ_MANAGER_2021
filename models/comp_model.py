# --- LIBRARIES ---
from PyQt5 import QtCore as qtc
from typing import Any, Optional
# --- CUSTOM MODULES ---
from core.components.components import Component

class CompModel(qtc.QAbstractItemModel):
    """
    This class manages the model storing the main data structure
    of an assembly project.
    """

    HEADERS = [
    #     'ID',
        'name',
        'desc',
    #     'type',
    #     'manufacture',
    #     'status',
    #     'comment',
    #     'price',
    #     'quantity',
    #     'packageQuantity',
    #     'seller',
    #     'link',
    ]

    def __init__(self, root: Optional[Component] = None) -> None:
        """
        Initialise the object parameters.

        Args:
            root (Component): the root component of this model. Default is None.
        """

        super(CompModel, self).__init__()

        if root:
            self.root = root
        else:
            self.root = Component(name='root', desc='no description')

        self.first = Component(name='Project', desc='Top level node, describe the project here!')
        self.root.add_child(self.first)

# --- MODEL FUNCTIONS OVERWRITING ---

    def data(self, index, role):
        """
        Returns the data stored under the given role for the item referred to
        by the index.
        """

        if not index.isValid():
            return None

        item = index.internalPointer()

        if role == qtc.Qt.DisplayRole or role == qtc.Qt.EditRole:
            column = self.HEADERS[index.column()]
            return getattr(item, column)

    def setData(self, index, value, role = qtc.Qt.EditRole):
        """
        Used to edit and update the model items values.
        """

        if index.isValid() and role == qtc.Qt.EditRole:
            item = index.internalPointer()
            setattr(item, self.HEADERS[index.column()], value)
            self.dataChanged.emit(index, index)
            return True
        return

    def flags(self, index):
        """
        Returns the item flags for the given index. This tells the program
        what can be done with the model items.
        Numbers, types and some manufactures of the items are non-editable fields,
        the other fields are editable.
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

    def index(self, row, column, parent):
        """
        Returns the index of the item in the model specified by the given row, column and parent index.
        When reimplementing this function in a subclass, call createIndex() to generate model indexes
        that other components can use to refer to items in your model.
        """

        if not self.hasIndex(row, column, parent):
            return qtc.QModelIndex()
        elif not parent.isValid():
            parent_item = self.root
        else:
            parent_item = parent.internalPointer()

        child_item = parent_item.get_child_at(row)

        if child_item:
            return self.createIndex(row, column, child_item)

        return qtc.QModelIndex()

    def parent(self, index):
        """
        Returns the parent index of the model item with the given index. If the item has no parent,
        an invalid QModelIndex is returned.
        A common convention used in models that expose tree data structures is that only items in the first
        column have children. For that case, when reimplementing this function in a subclass the column of
        the returned QModelIndex would be 0.
        When reimplementing this function in a subclass, be careful to avoid calling QModelIndex member
        functions, such as parent(), since indexes belonging to your model will simply call your implementation,
        leading to infinite recursion.
        """

        if not index.isValid():
            return qtc.QModelIndex()

        child_item = index.internalPointer()
        parent_item = child_item.get_parent()

        if not parent_item:
            return qtc.QModelIndex()

        row = parent_item.get_index()
        return self.createIndex(row, 0, parent_item)

    def rowCount(self, parent):
        """
        Returns the number of rows under the given parent. When the parent is valid it means
        that is returning the number of children of parent.
        """

        if parent.column() > 0:
            return 0

        if not parent.isValid():
            parent_item = self.root
        else:
            parent_item = parent.internalPointer()

        return len(parent_item)

    def columnCount(self, parent):
        """
        Returns the number of columns for the children of the given parent.
        In most subclasses, the number of columns is independent of the parent.
        """

        return len(self.HEADERS)

    def insertRows(self, item, parent_index = qtc.QModelIndex()):
        """
        Insert a node row in the specified position.
        """

        if parent_index.isValid():
            parent_item = parent_index.internalPointer()
        else:
            parent_item = self.first

        position = len(parent_item)

        self.beginInsertRows(parent_index.siblingAtColumn(0), position, position)
        success = parent_item.add_child(item)
        self.endInsertRows()

        return success

    def removeRows(self, position, parent_index = qtc.QModelIndex()):
        """
        Remove the row in the specified position.
        """

        if parent_index.isValid():
            parent_item = parent_index.internalPointer()
        else:
            parent_item = self.root

        self.beginRemoveRows(parent_index.siblingAtColumn(0), position, position)

        child_item = parent_item.get_child_at(position)
        success = parent_item.remove_child(child_item)

        self.endRemoveRows()

        return success

# --- LIBRARIES ---
from typing import Optional, List, Any
from dataclasses import dataclass

@dataclass
class Node:
    """Class to implement the tree behaviour of the component."""

    def __post_init__(self):
        self.parent: Optional["Node"] = None
        self.children_list: List["Node"] = []

# --- MODIFIERS ---

    def add_child(self, child: "Node") -> bool:
        """
        Adds a child node to the children list of this node. If the passed argument
        is not an instance of this class InvalidTypeError is raised.
        Returns True if the operation succeeds.
        """

        if self.is_leaf():
            raise LeafNodeError(self)

        if not isinstance(child, Node):
            raise InvalidTypeError(self, child)

        self.children_list.append(child)
        child._set_parent(self)
        return True

    def remove_child(self, child: "Node") -> bool:
        """
        Removes the given child from the children list of this node. If the passed
        argument is not an instance of this class InvalidTypeError is raised.
        If the passed node is not in this node's children list
        InvalidChildError is raised. Returns True if the operation succeeds.
        """

        if not isinstance(child, Node):
            raise InvalidTypeError(self, child)

        if child not in self.children_list:
            raise InvalidChildError(child)

        self.children_list.remove(child)
        child._set_parent(None)
        return True

    def remove_child_at(self, position: int) -> bool:
        """Removes the child node at the specified index if possible."""

        if self.is_empty():
            raise EmptyNodeError(self)

        if not 0 <= position < len(self.children_list):
            raise InvalidChildIndexError(position)

        removed = self.children_list.pop(position)
        removed._set_parent(None)
        return True

    def _set_parent(self, parent: Optional["Node"]) -> None:
        """Sets the parent field of this node."""

        if self.is_root():
            raise RootNodeError(self)

        self.parent = parent

# --- GETTERS ---

    def get_parent(self) -> Optional["Node"]:
        """Returns the parent of this node."""

        return self.parent

    def get_children_list(self) -> List["Node"]:
        """Returns this node's children list."""

        return self.children_list

    def get_subtree_nodes(self) -> List["Node"]:
        """
        Returns a list of all the nodes in the subtree with this node as root.
        This method is recursive. This node is included.
        """

        nodes_list = []
        for node in self.children_list:
            nodes_list.extend(node.get_subtree_nodes())

        nodes_list.append(self)

        return nodes_list

    def get_child_at(self, position: int) -> "Node":
        """Returns the child at the specified position if present."""

        if self.is_empty():
            raise EmptyNodeError(self)

        if not 0 <= position < len(self.children_list):
            raise InvalidChildIndexError(position)

        return self.children_list[position]

    def get_row(self) -> int:
        """
        Returns this node's index in it's parent children list. If this is
        a root node it should return 0.
        """

        if not self.parent: return 0

        parent_children_list = self.parent.get_children_list()
        return parent_children_list.index(self)

    def get_recursive_str(self, indent_level: int = 0) -> str:
        """
        Returns a string with the nodes written in a tree structure with
        the following style:

        Node(data)         #root
            Node(data)     #root's child
            Node(data)     #root's child
                Node(data) #child of root's child
                Node(data) #child of root's child
            Node(data)     #root's child

        and so on. This method is recursive.
        """

        output_string = self.__str__() + '\n'

        indent_level += 1
        for child in self.children_list:
            output_string += indent_level*'    ' + child.get_recursive_str(indent_level)

        return output_string.strip()

# --- BOOLEANS ---

    def is_empty(self) -> bool:
        """Returns True if this Node has no children, False if it's populated."""

        return not len(self)

    def is_root(self) -> bool:
        """
        Checks if the node is a root. Overwrite this method to
        make this node behave like an absolute root node and prevent
        it from changing it's parent node.
        """

        return False

    def is_leaf(self) -> bool:
        """
        Checks if the node is a leaf. Overwrite this method to
        make this node behave like a leaf node and prevent it from having children.
        """

        return False

# --- DUNDERS ---

    def __len__(self) -> int:
        """The length of a Node is the number of children it has."""

        return len(self.children_list)

    def __bool__(self) -> bool:
        """If a Node exists, bool returns True."""

        return True

# --- CUSTOM EXCEPTIONS ---

class InvalidChildIndexError(Exception):
    """
    Reports that a passed index is out of bound for the extraction
    of the children from a node.
    """

    def __init__(self, position: int) -> None:
        self.position = position
        self.message = f'{type(self).__name__}: position {self.position} out of bound.'

        super().__init__(self.message)

class InvalidChildError(Exception):
    """
    Reports that the passed child is not in the current
    node children list.
    """

    def __init__(self, child: Node) -> None:
        self.child = child
        self.message = f'{type(self).__name__}: "{self.child}" is not in the children list.'

        super().__init__(self.message)

class InvalidTypeError(Exception):
    """Reports that the passed argument is not an instance of Node."""

    def __init__(self, right: Node, wrong: Any) -> None:
        self.right = right
        self.wrong = wrong
        right_class = type(self.right).__name__
        self.message = f'{type(self).__name__}: "{self.wrong}" is not an instance of {right_class} class.'

        super().__init__(self.message)

class EmptyNodeError(Exception):
    """Reports that the node has no children while trying to access them."""

    def __init__(self, node: Node) -> None:
        self.node = node
        self.message = f'{type(self).__name__}: "{self.node}" is empty.'

        super().__init__(self.message)

class RootNodeError(Exception):
    """Reports that the node's parent can't be edited."""

    def __init__(self, node: Node) -> None:
        self.node = node
        self.message = f'{type(self).__name__}: "{self.node}" can\'t have a parent.'

        super().__init__(self.message)

class LeafNodeError(Exception):
    """Reports that the parent node can't be edited."""

    def __init__(self, node: Node) -> None:
        self.node = node
        self.message = f'{type(self).__name__}: "{self.node}" can\'t have children.'

        super().__init__(self.message)

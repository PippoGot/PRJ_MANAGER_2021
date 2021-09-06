from dataclasses import dataclass

class InexistentChildIndexError(Exception):
    """
    Reports that a passed index is out of bound for the extraction
    of the children from a node.
    """

    def __init__(self, message = None, position = None):
        self.message = message
        self.position = position

    def __str__(self):
        if self.message:
            return f'{type(self).__name__}: {self.message}'
        else:
            return f'{type(self).__name__}: child at position {self.position} doesn\'t exist'

class InexistentChildError(Exception):
    """
    Reports that the passed component is not in the current component children list.
    """

    def __init__(self, message = None):
        self.message = message

    def __str__(self):
        if self.message:
            return f'{type(self).__name__}: {self.message}'
        else:
            return f'{type(self).__name__}: given child doesn\'t exist in this component'

class InvalidComponentError(Exception):
    """
    Reports that the passed argument is not an instance of Component.
    """

    def __init__(self, message = None):
        self.message = message

    def __str__(self):
        if self.message:
            return f'{type(self).__name__}: {self.message}'
        else:
            return f'{type(self).__name__}: the argument is not a Component'


@dataclass
class Component:
    """Class to pack all of the data for a certain component in a build."""

    name: str
    desc: str

    def __post_init__(self):
        self.parent = None
        self.children = []

    def add_child(self, child_component):
        """Adds a component to the children list of this node."""

        if not type(child_component).__name__ == type(self).__name__:
            raise InvalidComponentError()

        self.children.append(child_component)
        child_component.set_parent(self)
        return True

    def remove_child(self, child_component):
        """Removes the given child from this component's children list."""

        if child_component not in self.children:
            raise InexistentChildError()

        self.children.remove(child_component)
        child_component.set_parent(None)
        return True

    def set_parent(self, parent):
        """Sets the parent field of this component."""

        self.parent = parent

    def get_parent(self):
        """Returns the parent of this component."""

        return self.parent

    def get_child_at(self, position):
        """Returns the child at the specified position if present."""

        if not 0 <= position < len(self.children):
            raise InexistentChildIndexError(position=position)

        return self.children[position]

    def get_children_list(self):
        """Returns this component children list."""

        return self.children

    def get_index(self):
        """Returns this component index in the parent list."""

        if not self.parent: return 0

        parent_children_list = self.parent.get_children_list()
        return parent_children_list.index(self)

    def __len__(self):
        """The length of a component is the number of children it has."""

        return len(self.children)

    def __bool__(self):
        if self.name: return True
        return False

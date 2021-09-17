# libraries
from dataclasses import dataclass
# custom modules
import core.custom_exceptions as cexc

@dataclass
class Component:
    """Class to pack all of the data for a certain component in a build."""

    name: str
    desc: str

    def __post_init__(self):
        self.parent = None
        self.children = []

# --- MODIFIERS ---

    def add_child(self, child_component):
        """Adds a component to the children list of this node."""

        if not type(child_component).__name__ == type(self).__name__:
            raise cexc.InvalidComponentError(child_component)

        self.children.append(child_component)
        child_component._set_parent(self)
        return True

    def remove_child(self, child_component):
        """Removes the given child from this component's children list."""

        if not type(child_component).__name__ == type(self).__name__:
            raise cexc.InvalidComponentError(child_component)

        if child_component not in self.children:
            raise cexc.InvalidChildError(child_component)

        self.children.remove(child_component)
        child_component._set_parent(None)
        return True

    # def remove_child_at(self, position):
    #     """Removes the child component at the specified index if possible."""

    #     if not 0 <= position < len(self.children):
    #         raise cexc.InvalidChildIndexError(position)

    #     removed_component = self.children.pop(position)
    #     removed_component._set_parent(None)
    #     return True

    def _set_parent(self, parent_component):
        """Sets the parent field of this component."""

        self.parent = parent_component

# --- GETTERS ---

    def get_parent(self):
        """Returns the parent of this component."""

        return self.parent

    def get_children_list(self):
        """Returns this component children list."""

        return self.children

    def get_subtree_components(self):
        """Returns a list of all the components in the subtree with this node as root."""

        component_list = []
        for component in self.children:
            component_list.extend(component.get_subtree_components())

        component_list.append(self)

        return component_list

    def get_child_at(self, position: int):
        """Returns the child at the specified position if present."""

        if self.is_empty():
            raise cexc.EmptyComponentError(self)

        if not 0 <= position < len(self.children):
            raise cexc.InvalidChildIndexError(position)

        return self.children[position]

    def get_index(self):
        """Returns this component's index in the parent list."""

        if not self.parent: return 0

        parent_children_list = self.parent.get_children_list()
        return parent_children_list.index(self)

    def recursive_str(self, indent_level = 0):
        """Returns a string with the node written in a tree structure."""

        output_string = self.__str__() + '\n'

        indent_level += 1
        for child_component in self.children:
            output_string += indent_level*'    ' + child_component.recursive_str(indent_level)

        return output_string

# --- BOOLEANS ---

    def is_empty(self):
        """Returns True if this component has no children, False if is populated."""

        if not len(self): return True
        return False

# --- DUNDERS ---

    def __len__(self):
        """The length of a component is the number of children it has."""

        return len(self.children)

    def __bool__(self):
        """If a component exists, bool returns True."""

        return True

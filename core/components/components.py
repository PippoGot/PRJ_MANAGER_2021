 # --- LIBRARIES ---
from dataclasses import dataclass
from typing import NoReturn, Optional, List
# --- CUSTOM MODULES ---
import core.custom_exceptions as cexc

@dataclass
class Component:
    """
    This class packs all of the data for a component in an assembly build.
    Also it provides some method for the representation of the component, as
    well as fields and methods to structure the component into a tree.
    """

    name: str
    desc: str

    def __post_init__(self):
        self.parent: Optional["Component"] = None
        self.children: List["Component"] = []

# --- MODIFIERS ---

    def add_child(self, child_component: "Component") -> bool:
        """
        Adds a component to the children list of this component. If the passed argument
        is not an instance of this class InvalidExceptionError is raised.
        Returns True if the operation succeeds.
        """

        # checks if the argument is a valid instance
        if not type(child_component).__name__ == type(self).__name__:
            raise cexc.InvalidComponentError(child_component)

        # appends the component to the list and updates it's parent
        self.children.append(child_component)
        child_component._set_parent(self)
        return True

    def remove_child(self, child_component: "Component") -> bool:
        """
        Removes the given child from the children list of this component. If the passed
        argument is not an instance of this class InvalidExceptionError is raised.
        If the passed component is not in this component's children list
        InvalidChildError is raised. Returns True if the operation succeeds.
        """

        # checks if the argument is a valid instance
        if not type(child_component).__name__ == type(self).__name__:
            raise cexc.InvalidComponentError(child_component)
        # and is in the list
        if child_component not in self.children:
            raise cexc.InvalidChildError(child_component)

        # removes the component from the list and updates it's parent
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

    def _set_parent(self, parent_component: Optional["Component"]) -> None:
        """Sets the parent field of this component."""

        self.parent = parent_component

# --- GETTERS ---

    def get_parent(self) -> Optional["Component"]:
        """Returns the parent of this component."""

        return self.parent

    def get_children_list(self) -> List["Component"]:
        """Returns this component children list."""

        return self.children

    def get_subtree_components(self) -> List["Component"]:
        """
        Returns a list of all the components in the subtree with this component as root.
        This method is recursive.
        """

        # recursion first, the list is filled with all the children
        component_list = []
        for component in self.children:
            component_list.extend(component.get_subtree_components())

        # the list is competed with this component and then returned
        component_list.append(self)

        return component_list

    def get_child_at(self, position: int) -> "Component":
        """Returns the child at the specified position if present."""

        # checks if the component is empty
        if self.is_empty():
            raise cexc.EmptyComponentError(self)
        # or if the passed index is out of bounds
        if not 0 <= position < len(self.children):
            raise cexc.InvalidChildIndexError(position)

        # returns the requested component
        return self.children[position]

    def get_index(self) -> int:
        """
        Returns this component's index in it's parent list. If this is
        a root component the row it should return has value 0.
        """

        if not self.parent: return 0

        # extract the index from the parent
        parent_children_list = self.parent.get_children_list()
        return parent_children_list.index(self)

    def recursive_str(self, indent_level: int = 0) -> str:
        """
        Returns a string with the components written in a tree structure with
        the following style:

        Component(data)         #root
            Component(data)     #root's child
            Component(data)     #root's child
                Component(data) #child of root's child
                Component(data) #child of root's child
            Component(data)     #root's child

        and so on. This method is recursive as the name implies.
        """

        # this component is added to the output string
        output_string = self.__str__() + '\n'

        # the indentation level is rose by 1 with every nesting level
        indent_level += 1
        # gets the string for every child and concatenates it to the output string
        for child_component in self.children:
            output_string += indent_level*'    ' + child_component.recursive_str(indent_level)

        # returns the output string
        return output_string.strip()

# --- BOOLEANS ---

    def is_empty(self) -> bool:
        """Returns True if this component has no children, False if it's populated."""

        return not len(self)

# --- DUNDERS ---

    def __len__(self) -> int:
        """The length of a component is the number of children it has."""

        return len(self.children)

    def __bool__(self) -> bool:
        """If a component exists, bool returns True."""

        return True

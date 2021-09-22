 # --- LIBRARIES ---
from dataclasses import dataclass
import dataclasses
from typing import Tuple, Any, List
# --- CUSTOM MODULES ---
from .nodes import Node

@dataclass
class Component(Node):
    """
    This class packs all of the data for a component in an assembly build.
    Also it provides some method for the representation of the component.
    """

    name: str
    desc: str

    # HEADERS = [
    # #     'ID',
    # #     'type',
    # #     'manufacture',
    # #     'status',
    # #     'comment',
    # #     'price',
    # #     'quantity',
    # #     'packageQuantity',
    # #     'seller',
    # #     'link',
    # ]

    # --- MODIFIERS ---

    def replace_field(self, field: str, new_value: Any) -> None:
        """Replaces the value of a field inside the component with a new value."""

        if field not in self.get_fields_tuple():
            raise FieldNameError(field, self)

        setattr(self, field, new_value)

    # --- GETTERS ---

    def get_subtree_components(self) -> List[Node]:
        """Overwrites the name of the superclass method to make more sense."""

        return super().get_subtree_nodes()

    def get_fields_tuple(self) -> Tuple[str]:
        """Returns a tuple containing all of the fields in the component."""

        field_list = [field.name for field in dataclasses.fields(self)]
        return tuple(field_list)

    def get_field(self, field: str) -> Any:
        """
        Returns the value of the selected field. If a nonexistent field is
        passed, FieldNameError is raised.
        """

        if field not in self.get_fields_tuple():
            raise FieldNameError(field, self)

        return getattr(self, field)

    def as_dict(self):
        """Returns this class in dict form, field_name: field_value."""

        return dataclasses.asdict(self)

# --- CUSTOM EXCEPTIONS ---

class FieldNameError(Exception):
    """Reports that a passed field name does not exist in the component."""

    def __init__(self, field: str, component: Component) -> None:
        self.wrong_field = field
        self.component = component
        self.message = f'{type(self).__name__}: {self.wrong_field} doesn\'t exist in component {self.component}'

        super().__init__(self.message)

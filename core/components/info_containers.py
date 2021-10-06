# --- LIBRARIES ---
from dataclasses import dataclass
import dataclasses
from typing import Tuple, Any, Dict, Optional
# --- CUSTOM MODULES ---
from ..enums import TypeEnums, StatusEnums, ManufactureEnums

class InfoContainer:
    """Generalisation of an info container class."""

    # --- MODIFIERS ---

    def replace_field(self, field_name: str, new_value: Any) -> None:
        """Replaces the value of a field inside the container with a new value."""

        if field_name not in self.get_fields_tuple():
            raise FieldNameError(field_name, self)

        setattr(self, field_name, new_value)

    # --- GETTERS ---

    def get_field(self, field_name: str) -> Any:
        """
        Returns the value of the selected field. If a nonexistent field is
        passed, FieldNameError is raised.
        """

        if field_name not in self.get_fields_tuple():
            raise FieldNameError(field_name, self)

        value = getattr(self, field_name)

        if type(value) == TypeEnums or type(value) == ManufactureEnums:
            return value.value
        elif type(value) == StatusEnums:
            return value.name.title()

        return value

    def get_fields_tuple(self) -> Tuple[str, ...]:
        """Returns a tuple containing all of the fields in the component."""

        field_list = [field.name for field in dataclasses.fields(self) if not field.name[0] == '_']
        return tuple(field_list)

    def as_dict(self) -> Dict[str, Any]:
        """Returns this class in dict form, field_name: field_value."""

        return dataclasses.asdict(self)

@dataclass
class GeneralComponentInfo(InfoContainer):
    """Class to gather the general info of a component."""

    name: Optional[str] = 'Name'
    desc: Optional[str] = 'Describe here your component...'
    comment: Optional[str] = 'Write here your notes...'
    tp: Optional[TypeEnums] = TypeEnums.PLACEHOLDER
    status: Optional[StatusEnums] = StatusEnums.INVISIBLE
    manufacture: Optional[ManufactureEnums] = ManufactureEnums.ANY
    qty: Optional[int] = 0
    cost: Optional[float] = 0.00

@dataclass
class PurchasableComponentInfo(InfoContainer):
    """Class to gather the buying info of a hardware component."""

    qty_pkg: Optional[int] = 0
    seller: Optional[str] = 'Write here the seller of the component'
    link: Optional[str] = 'The link for the page goes here...'

# --- CUSTOM EXCEPTIONS ---

class FieldNameError(Exception):
    """Reports that a passed field name does not exist in the container."""

    def __init__(self, field: str, container: InfoContainer) -> None:
        self.wrong_field = field
        self.container = container
        self.message = f'{type(self).__name__}: {self.wrong_field} doesn\'t exist in container {self.container}'

        super().__init__(self.message)

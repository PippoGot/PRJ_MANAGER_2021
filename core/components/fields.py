# --- LIBRARIES ---
from dataclasses import dataclass
from typing import Any, Optional

# @dataclass
# class Field:
#     name: str
#     value: Optional[Any] = None
#     editable: Optional[bool] = True

#     def is_editable(self):
#         return self.editable

#     def get_name(self):
#         return self.name

#     def get_value(self):
#         return self.value

#     def set_name(self, new_name):
#         self.name = new_name

#     def set_value(self, new_value):

#         if not self.is_editable():
#             raise ImmutableFieldError(self)

#         self.value = new_value

#     def __repr__(self):
#         return f"'{self.name}' Field = '{self.value}', editablility = {self.editable}"


class ImmutableFieldError(Exception):
    """Reports that the field value can't be edited."""

    def __init__(self, field: Field) -> None:
        self.field = Field
        self.message = f'{type(self).__name__}: "{self.field}" can\'t be edited.'

        super().__init__(self.message)

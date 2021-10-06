# --- LIBRARIES ---
from dataclasses import dataclass
from typing import Optional

@dataclass
class Tag:
    """Class to keep track and perform operations to a component tag."""

    tag_string: str = '#000-000'
    _level: int = 0

    # --- MODIFIERS ---

    def increment(self, inc_qty: int) -> 'Tag':
        """
        Increments the tag according to the type and quantity passed, then returns
        a new tag item.
        """

        inc_level = self._level + 1

        if inc_level >= 4:
            inc_suffix = inc_string(self.suffix, inc_qty)

            return Tag(f'#{self.prefix[:]}-{inc_suffix}', inc_level)

        else:
            inc_prefix_char = inc_string(self.prefix[self._level], inc_qty)
            inc_prefix = self.prefix[:]

            temp_inc_prefix = ''
            for x in range(len(inc_prefix)):
                if x == inc_level - 1:
                    temp_inc_prefix += inc_prefix_char
                else:
                    temp_inc_prefix += inc_prefix[x]

            inc_prefix = temp_inc_prefix
            return Tag(f'#{inc_prefix}-{self.suffix[:]}', inc_level)

    def replace_tag(self, new_tag: 'Tag') -> None:
        """Replaces this instance's fields with the one of the passed tag instance."""

        self.tag_string = new_tag.get_tag_string()
        self._level = new_tag._get_level()

    # --- GETTERS ---

    def get_tag_string(self):
        """Returns the tag string."""

        return self.tag_string

    @property
    def prefix(self):
        """Returns the prefix string of the tag, the first 3 characters that have value."""

        return self.tag_string[1:4]

    @property
    def suffix(self):
        """Returns the suffix string of the tag, the last 3 characters that have value."""

        return self.tag_string[5:]

    def _get_level(self):
        """Returns the level."""

        return self._level

    def size(self) -> int:
        """Returns the size of the tag, defined in the following way:

        #   X      X      X    --    X      X      X
            |      |      |          |      |      |
            v      v      v          v      v      v
           36^3 + 36^4 + 36^5   +   36^2 + 36^1 + 36^0
        """

        size = convert_to_base_10(self.suffix) + convert_to_base_10(self.prefix[::-1])
        return size

# --- UTILITY FUNCTIONS ---

VALUES = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def inc_string(string: str, inc_qty: int) -> str:
    """Increments a string converted in base 36, by a given value."""

    value = convert_to_base_10(string) + inc_qty

    return convert_to_base_36(value)

def convert_to_base_10(string_number: str) -> int:
    """Converts a string of alphanumeric characters to a number in base 36."""

    exponent = 0
    value = 0

    for char in string_number:
        value += (36**exponent)*(VALUES.index(char))
        exponent += 1

    return value

def convert_to_base_36(value: int) -> str:
    """Converts an integer number to a string in base 36."""

    output_string = ''
    exponent = 0

    while value > 0:
        index_value = value % 36
        output_string += VALUES[index_value]

        value -= (36**exponent)*index_value
        exponent += 1

    return output_string[::-1]

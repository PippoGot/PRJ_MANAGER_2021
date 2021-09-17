# used in nodes.py

class InvalidChildIndexError(Exception):
    """
    Reports that a passed index is out of bound for the extraction
    of the children from a node.
    """

    def __init__(self, position):
        self.position = position
        self.message = f'{type(self).__name__}: position {self.position} out of bound'

        super().__init__(self.message)

class InvalidChildError(Exception):
    """Reports that the passed component is not in the current component children list."""

    def __init__(self, child_component):
        self.component = child_component
        self.message = f'{type(self).__name__}: "{self.component}" is not in the children list'

        super().__init__(self.message)

class InvalidComponentError(Exception):
    """Reports that the passed argument is not an instance of Component."""

    def __init__(self, obj):
        self.object = obj
        self.message = f'{type(self).__name__}: "{self.object}" is not an instance of Component class'

        super().__init__(self.message)

class EmptyComponentError(Exception):
    """Reports that the component has no children while trying to access them."""

    def __init__(self, component):
        self.component = component
        self.message = f'{type(self).__name__}: "{self.component}" is empty'

        super().__init__(self.message)

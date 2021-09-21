# --- LIBRARIES ---
from hypothesis.stateful import RuleBasedStateMachine, rule, invariant, Bundle, consumes, initialize
from hypothesis import strategies as st, settings, Verbosity
from unittest import TestCase
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
# --- CUSTOM MODULES ---
from core.components.components import Component
from models.comp_model import CompModel
from ..test_core.test_components import component_st

# don't need to test
# - column count
# - header data

class CompModelTest(RuleBasedStateMachine):
    """State machine to test the component model."""

    def __init__(self):
        """Creates the test CompModel and gets the two initial elements."""

        super().__init__()
        self.model = CompModel()

        self.components = [
                self.model.root,
                self.model.first
            ]

    def _create_index(self, item):
        """Generates the model index of a given component."""

        row = item.get_index()
        return self.model.createIndex(row, 0, item)

    @rule(item = component_st(), data = st.data())
    def add_component_to_model(self, item, data):
        """Adds a component to the model."""

        # gets a component from the added ones
        parent_item = data.draw(st.sampled_from(self.components))
        # creates the proper index
        parent_index = self._create_index(parent_item)
        # and adds it to the model
        self.model.insertRows(item, parent_index)

        # then checks if the added item is inside the data structure
        position = len(parent_item) - 1
        child_item = parent_item.get_child_at(position)
        assert child_item == item

        # and adds the item to the list of components to use it as random data
        self.components.append(item)

    @rule(data = st.data())
    def remove_component_from_model(self, data):
        """Removes a component from the model."""

        # gets a component from the added ones
        parent_item = data.draw(st.sampled_from(self.components))
        # if the component is empty returns because there is nothing to remove
        if parent_item.is_empty(): return

        # creates the index of the selected parent and generates a random position
        parent_index = self._create_index(parent_item)
        position = data.draw(st.integers(min_value = 0, max_value = len(parent_item) - 1))
        child_item = parent_item.get_child_at(position)

        # finally removes the generated row and updates the component list
        self.model.removeRows(position, parent_index)
        self.components = self.model.root.get_subtree_components()

    @invariant()
    def check_components(self):
        """
        After every step checks that the list of components contains all of the elements
        in the model.
        """

        # gets the list of components
        components_list = self.model.root.get_subtree_components()

        # for every one of them
        for component in self.components:
            # the index is generated
            component_index = self._create_index(component)
            # the parent index is extracted
            parent_index = self.model.parent(component_index)
            # as well as the parent item
            parent_item = parent_index.internalPointer()

            # then the parent is checked with the original component's parent
            assert parent_item == component.get_parent()
            assert component in components_list

        assert len(components_list) == len(self.components)

# --- TEST EXECUTION ---

Test = CompModelTest.TestCase
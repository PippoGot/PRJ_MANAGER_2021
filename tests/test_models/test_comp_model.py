# libraries
from hypothesis.stateful import RuleBasedStateMachine, rule, invariant, Bundle, consumes, initialize
from hypothesis import strategies as st, settings, Verbosity
from unittest import TestCase
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
# custom modules
from core.components.components import Component
from models.comp_model import CompModel
from ..test_core.test_components import component_st

# don't need to test
# - column count
# - header data

class CompModelTest(RuleBasedStateMachine):

    def __init__(self):
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

        parent_item = data.draw(st.sampled_from(self.components))
        parent_index = self._create_index(parent_item)
        self.model.insertRows(item, parent_index)

        position = len(parent_item) - 1
        child_item = parent_item.get_child_at(position)

        assert child_item == item
        self.components.append(item)

    @rule(data = st.data())
    def remove_component_from_model(self, data):
        """Removes a component from the model."""

        parent_item = data.draw(st.sampled_from(self.components))
        if parent_item.is_empty(): return

        parent_index = self._create_index(parent_item)
        position = data.draw(st.integers(min_value = 0, max_value = len(parent_item) - 1))
        child_item = parent_item.get_child_at(position)

        self.model.removeRows(position, parent_index)
        self.components = self.model.root.get_subtree_components()

    @invariant()
    def check_components(self):
        """
        After every step checks that the list of components contains all of the elements
        in the model.
        """

        components_list = self.model.root.get_subtree_components()

        for component in self.components:
            component_index = self._create_index(component)
            parent_index = self.model.parent(component_index)
            parent_item = parent_index.internalPointer()

            assert parent_item == component.get_parent()
            assert component in components_list

        assert len(components_list) == len(self.components)

# --- TEST EXECUTION ---

Test = CompModelTest.TestCase
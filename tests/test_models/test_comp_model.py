# --- LIBRARIES ---
from hypothesis.stateful import RuleBasedStateMachine, rule, invariant
from hypothesis import strategies as st
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

        self._update_components()

    def _create_index(self, component: Component) -> qtc.QModelIndex:
        """Generates the model index of a given component."""

        row = component.get_row()
        return self.model.createIndex(row, 0, component)

    def _update_components(self) -> None:
        """Updates the content of the components list."""

        self.components = self.model.get_components_list()

    #TODO change asdict
    @rule(component = component_st(), data = st.data())
    def add_component_to_model(self, component, data):
        """Adds a component to the model."""

        parent_component = data.draw(st.sampled_from(self.components))
        parent_index = self._create_index(parent_component)
        data_dict = component.as_dict()

        self.model.insertRows(data_dict, parent_index)

        position = len(parent_component) - 1
        child_component = parent_component.get_child_at(position)
        assert child_component == component

        self._update_components()

    @rule(data = st.data())
    def remove_component_from_model(self, data):
        """Removes a component from the model."""

        parent_component = data.draw(st.sampled_from(self.components))

        if parent_component.is_empty(): return

        position = data.draw(st.integers(min_value = 0, max_value = len(parent_component) - 1))
        component = parent_component.get_child_at(position)
        component_index = self._create_index(component)

        self.model.removeRows(component_index)

        self._update_components()

    @invariant()
    def check_components(self):
        """
        After every step checks that the list of components contains all of the elements
        in the model.
        """

        components_list = self.model.get_components_list()

        for component in self.components:
            component_index = self._create_index(component)
            parent_index = self.model.parent(component_index)
            parent_component = parent_index.internalPointer()

            assert parent_component == component.get_parent()
            assert component in components_list

        assert len(components_list) == len(self.components)

# --- TEST EXECUTION ---

Test = CompModelTest.TestCase
from hypothesis import given, settings, assume, strategies as st
from hypothesis import reproduce_failure, note

from core.nodes.nodes import Component

# settings(max_examples = 20)

@given(st.text(), st.text())
def test_component_creation(component_name, component_desc):
    test_component = Component(component_name, component_desc)

    assert component_name == getattr(test_component, "name")
    assert component_desc == getattr(test_component, "desc")
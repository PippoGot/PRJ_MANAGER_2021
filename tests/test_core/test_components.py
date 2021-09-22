# --- LIBRARIES ---
from hypothesis import given, strategies as st
from hypothesis import reproduce_failure, note
# --- CUSTOM MODULES ---
from core.components.components import Component
from core.components.nodes import InvalidChildError, InvalidChildIndexError, InvalidTypeError, EmptyNodeError

# --- STRATEGIES ---

@st.composite
def component_st(draw):
    """Defines how to create a Component strategy."""

    component = draw(st.builds(Component, st.text(), st.text()))
    return component

@st.composite
def populated_component_st(draw):
    """Defines how to create a populated Component strategy."""

    parent_component = draw(component_st())
    children_components = draw(st.lists(component_st()))

    for component in children_components:
        parent_component.add_child(component)

    return parent_component

@st.composite
def component_tree_st(draw):
    """Defines how to create a Component tree strategy."""

    parent_component = draw(component_st())
    children_components = draw(st.lists(populated_component_st()))

    for component in children_components:
        parent_component.add_child(component)

    return parent_component

# --- MODIFIERS TESTS ---

@given(populated_component_st(), component_st(), st.randoms())
def test_add_child(parent_component, child_component, random_data):
    """Tests the addition of a component in a parent component."""

    result = parent_component.add_child(child_component)
    position = len(parent_component) - 1

    assert parent_component.get_child_at(position) == child_component
    assert child_component.get_parent() == parent_component
    assert result == True

    try:
        parent_component.add_child(random_data)
    except InvalidTypeError:
        assert type(random_data) != type(child_component)

@given(populated_component_st(), component_st(), st.randoms())
def test_remove_child(parent_component, child_component, random_data):
    """Tests the removal of a component in a parent component."""

    initial_length = len(parent_component)
    parent_component.add_child(child_component)
    position = len(parent_component) - 1

    assert parent_component.get_child_at(position) == child_component

    result = parent_component.remove_child(child_component)

    assert len(parent_component) == initial_length
    assert result == True

    try:
        parent_component.remove_child(random_data)
    except InvalidTypeError:
        assert type(random_data) != type(child_component)

    try:
        parent_component.remove_child(child_component)
    except InvalidChildError:
        assert child_component not in parent_component.get_children_list()

# --- GETTERS TESTS ---

@given(populated_component_st(), st.integers())
def test_get_child_at(component, position):
    """Tests if the get_child_at method works with valid indexes."""

    try:
        child_at_position = component.get_child_at(position)
        assert child_at_position == component.get_children_list()[position]
    except InvalidChildIndexError:
        assert not 0 <= position < len(component)
    except EmptyNodeError:
        assert component.is_empty()

@given(populated_component_st())
def test_get_row(component):
    """Tests the get_row method. A component's index inside it's parent children list."""

    for child_component in component.get_children_list():
        child_row = child_component.get_row()

        assert child_component.get_parent() == component
        assert child_component == component.get_child_at(child_row)

@given(populated_component_st())
def test_get_subtree_components(root_component):
    """Tests if the functions returns a list containing the nodes in the subtree."""

    subtree_components_list = root_component.get_subtree_components()
    for component in subtree_components_list:
        while component.get_parent():
            component = component.get_parent()
        assert component == root_component
    assert len(subtree_components_list) > len(root_component)

@given(component_tree_st())
def test_get_recursive_str(component):
    """Tests if the recursive str function works as intended."""

    result_string = component.get_recursive_str()
    test_strings_list = result_string.split('    ')
    matching_strings_list = [string.replace('\n', '') for string in test_strings_list if string]

    components_list = component.get_subtree_components()
    components_str_list = [str(string) for string in components_list]

    for string in matching_strings_list:
        assert string in components_str_list
    assert len(matching_strings_list) == len(components_str_list)

# --- BOOLEANS TESTS ---

@given(st.one_of(component_st(), populated_component_st()))
def test_component_is_empty(component):
    """Tests if a Component is empty."""

    if component.is_empty():
        assert len(component) == 0

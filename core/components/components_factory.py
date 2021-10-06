# --- LIBRARIES ---
from typing import Callable, Dict, Any
# --- CUSTOM MODULES ---
from ..components import components as comp
from ..enums import get_enum

component_creation_dict: Dict[str, Callable[..., comp.BaseComponent]] = {
    'base': comp.BaseComponent,
    'project': comp.ProjectComponent,
    'assembly': comp.AssemblyComponent,
    'jig': comp.JigComponent,
    'part': comp.PartComponent,
    'placeholder': comp.PlaceholderComponent,
    'mechanical': comp.MechanicalComponent,
    'electronic': comp.ElectronicComponent,
    'electromechanical': comp.ElectromechanicalComponent,
    'consumable': comp.ConsumableComponent,
    'measured': comp.MeasuredComponent
}

# --- FACOTRY METHODS ---

def register_component(comp_type: str, comp_func: Callable[..., comp.BaseComponent]) -> None:
    """Registers a new type of component and the function to create it."""

    component_creation_dict[comp_type] = comp_func

def unregister_component(comp_type: str) -> None:
    """Unregisters a type of component from the factory."""

    component_creation_dict.pop(comp_type, None)

def create_component(data: Dict[str, Any]) -> comp.BaseComponent:
    """Creates a component of a specific type, given some data."""

    data_copy = data.copy()
    comp_type = data_copy['tp'].value
    if not comp_type: comp_type = 'base'

    try:
        creator_func = component_creation_dict[comp_type.lower()]
    except KeyError:
        raise ValueError(f'unknown component type {comp_type!r}') from None

    return creator_func(**data_copy)

def create_default_component(tpye_string: str) -> comp.BaseComponent:
    """Creates a component of the specific type with default data."""

    try:
        creator_func = component_creation_dict[tpye_string]
    except KeyError:
        raise ValueError(f'unknown component type {tpye_string!r}') from None

    return creator_func()

# --- UTILITY FUNCTIONS ---

def init_model_root() -> tuple[comp.BaseComponent, comp.ProjectComponent]:
    """Creates the root structure for the model using components."""

    root = create_component(
        {
            'name': 'root',
            'tp': get_enum('base')
        }
    )

    first = create_component(
        {
            'name': 'Project',
            'desc': 'Top level node, describe the project here!',
            'tp': get_enum('project')
        }
    )

    root.add_child(first)

    return root, first

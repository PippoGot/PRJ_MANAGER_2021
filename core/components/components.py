 # --- LIBRARIES ---
from dataclasses import dataclass
from typing import Tuple, Any, List, Dict
# --- CUSTOM MODULES ---
from .nodes import Node
from .info_containers import GeneralComponentInfo, PurchasableComponentInfo
from .tag import Tag
from ..enums import StatusEnums, TypeEnums, ManufactureEnums

# --- BASE COMPONENT ---

@dataclass
class BaseComponent(Node, GeneralComponentInfo, Tag):
    """This class packs all of the data for a component in an assembly build."""

# --- MISC COMPONENTS ---

class ProjectComponent(BaseComponent):
    """
    This class will contains all of the other components, the
    project you are building.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.replace_field('tp', TypeEnums.PROJECT)
        self.replace_field('manufacture', ManufactureEnums.ASSEMBLED)

class AssemblyComponent(BaseComponent):
    """
    This class represents a general assembly component, several
    components connected together.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.replace_field('tp', TypeEnums.ASSEMBLY)
        self.replace_field('manufacture', ManufactureEnums.ASSEMBLED)

class JigComponent(BaseComponent):
    """This class represents a jig or a jig assembly."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.replace_field('tp', TypeEnums.JIG)

class PartComponent(BaseComponent):
    """
    This class reimplements is_leaf to return true meaning this node can't have
    children. Represents a part made of single component in opposition to the assembly.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.replace_field('tp', TypeEnums.PART)

    def is_leaf(self):
        return True

# --- HARDWARE COMPONENTS ---

class PlaceholderComponent(PartComponent):
    """
    This class represents a blank spot to replace with a component
    in the near future.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.replace_field('tp', TypeEnums.PLACEHOLDER)
        self.replace_field('manufacture', ManufactureEnums.ANY)
        self.replace_field('status', StatusEnums.INVISIBLE)
        self.replace_field('cost', 0.0)

class HardwareComponent(PartComponent, PurchasableComponentInfo):
    """
    This class represents a hardware component, like something you buy
    at the store or online and doesn't need to be processed.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.replace_field('manufacture', ManufactureEnums.BOUGHT)

    # def get_fields_tuple(self):
    #     general_info_fields_list = list(PartComponent.get_fields_tuple(self))
    #     purchasable_info_fields_list = list(PurchasableComponentInfo.get_fields_tuple(self))

    #     return tuple(general_info_fields_list + purchasable_info_fields_list)

class MechanicalComponent(HardwareComponent):
    """This class represents mechanical hardware, for example screws or washers."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.replace_field('tp', TypeEnums.MECHANICAL)

class ElectronicComponent(HardwareComponent):
    """This class represents electronic hardware, for example cbles or boards."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.replace_field('tp', TypeEnums.ELECTRONIC)

class ElectromechanicalComponent(HardwareComponent):
    """This class represents electromechanical hardware, for example motors or servos."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.replace_field('tp', TypeEnums.ELECTROMECHANICAL)

class ConsumableComponent(HardwareComponent):
    """This class represents consumable items, for example glues or filament spools."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.replace_field('tp', TypeEnums.CONSUMABLE)

class MeasuredComponent(HardwareComponent):
    """This class represents mechanical hardware with a measure of length or surface."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.replace_field('tp', TypeEnums.MEASURED)

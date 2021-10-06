from enum import Enum

class StatusEnums(Enum):
    """Advancement status for a component."""

    NOT_DESIGNED = 0            # the component is not designed
    DESIGN_IN_PROGRESS = 1      # the component's design is in progress
    DESIGNED = 2                # the component is designed in CAD
    READY_FOR_PURCHASE = 3      # the component can be ordered
    READY_FOR_MANUFACTURE = 3   # the component can be manufactured
    WAITING_FOR_SHIPPING = 4    # the component is shipping
    TESTING = 4                 # the component is being tested
    CAD_POLISHING = 5           # the component's CAD files need some adjustments
    DONE = 6                    # the component is finished for this iteration

    HAS_CAD = 1001              # the component is designed or visible in CAD
    HASNT_CAD = 1002            # the component is not designed or visible in CAD
    DEPRECATED = 1003           # the component is no longer used or present in the design
    INVISIBLE = 1004            # the component should not be included in the BOM

class TypeEnums(Enum):
    """Components types."""

    BASE = "Base"

    PROJECT = "Project"
    ASSEMBLY = "Assembly"
    PART = "Part"

    MECHANICAL = "Mechanical"
    MEASURED = "Measured"
    ELECTRONIC = "Electronic"
    ELECTROMECHANICAL = "Electromechanical"
    CONSUMABLE = "Consumable"

    JIG = "Jig"
    PLACEHOLDER = "Placeholder"

class ManufactureEnums(Enum):
    """Components manufacture methods."""

    PRINTED = "3D printed"
    MACHINED = "Machined"
    MODIFIED_HARDWARE = "Modified Hardware"
    LASERCUT = "Lasercut"
    BOUGHT = "Bought"
    ASSEMBLED = "Assembled"

    ANY = "Any"

enums_dict = {
    # type
    "base": TypeEnums.BASE,
    "project": TypeEnums.PROJECT,
    "assembly": TypeEnums.ASSEMBLY,
    "part": TypeEnums.PART,
    "mechanical": TypeEnums.MECHANICAL,
    "measured": TypeEnums.MEASURED,
    "electronic": TypeEnums.ELECTRONIC,
    "electromechanical": TypeEnums.ELECTROMECHANICAL,
    "consumable": TypeEnums.CONSUMABLE,
    "jig": TypeEnums.JIG,
    "placeholder": TypeEnums.PLACEHOLDER
}

def get_enum(enum_name):
    """Returns the corresponding enum based on the passed string."""

    return enums_dict[enum_name]
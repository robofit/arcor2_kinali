from arcor2.data.common import Arcor2Enum
from dataclasses_jsonschema import JsonSchemaMixin


class MoveTypeEnum(Arcor2Enum):

    AVOID_COLLISIONS: str = "AvoidCollisions"
    LINE: str = "Line"
    SIMPLE: str = "Simple"

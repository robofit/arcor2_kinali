from typing import List
from dataclasses import dataclass

from dataclasses_jsonschema import JsonSchemaMixin

from arcor2.data.common import Pose, Joint, StrEnum, Position, Orientation


class MoveTypeEnum(StrEnum):

    AVOID_COLLISIONS: str = "AvoidCollisions"
    LINE: str = "Line"
    SIMPLE: str = "Simple"


@dataclass
class MoveRelativeParameters(JsonSchemaMixin):

    pose: Pose
    position: Position  # relative position
    orientation: Orientation  # relative orientation


@dataclass
class MoveRelativeJointsParameters(JsonSchemaMixin):

    joints: List[Joint]
    position: Position  # relative position
    orientation: Orientation  # relative orientation

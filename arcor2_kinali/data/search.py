from dataclasses import dataclass
from typing import List

from dataclasses_jsonschema import JsonSchemaMixin

from arcor2.data.common import Pose


@dataclass
class ScoredItem(JsonSchemaMixin):

    id: int
    item_pose: Pose
    search_score: float


@dataclass
class SearchOutput(JsonSchemaMixin):

    items: List[ScoredItem]
    container_pose: Pose


@dataclass
class GripperSetup(JsonSchemaMixin):

    pick_pose: Pose
    pick_speed: float
    pre_pick_opening: float
    pick_grip: float
    pick_force: float

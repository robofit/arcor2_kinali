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

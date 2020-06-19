from dataclasses import dataclass
from arcor2.data.common import StrEnum
from typing import List
from dataclasses_jsonschema import JsonSchemaMixin


class NotificationLevelEnum(StrEnum):

    INFO: str = "Info"
    WARN: str = "Warn"
    ERROR: str = "Error"


@dataclass
class DialogValue(JsonSchemaMixin):

    title: str
    content: str
    options: List[str]


@dataclass
class NotificationValue(JsonSchemaMixin):

    message: str
    level: NotificationLevelEnum
    created: int

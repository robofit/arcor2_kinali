from dataclasses import dataclass
from typing import Set

from arcor2 import rest
from arcor2.data.common import Pose
from arcor2.object_types.abstract import Generic, Robot, Settings


@dataclass
class KinaliSettings(Settings):
    url: str
    configuration_id: str


class KinaliMixin:

    @property
    def settings(self) -> KinaliSettings:
        return self._settings  # type: ignore  # TODO solve this using typing_extensions/Protocol?

    def cleanup(self) -> None:
        rest.put(f"{self.settings.url}/systems/destroy")

    def _active_configuration(self) -> str:
        return rest.get_primitive(f"{self.settings.url}/systems/active", str)

    def _get_configuration_ids(self) -> Set[str]:
        return set(rest.get_data(f"{self.settings.url}/systems"))

    def _create(self):
        if self._active_configuration() != self.settings.configuration_id:
            rest.put(f"{self.settings.url}/systems/{self.settings.configuration_id}/create")


class KinaliObject(KinaliMixin, Generic):

    def __init__(self, obj_id: str, name: str, settings: KinaliSettings) -> None:
        super(KinaliObject, self).__init__(obj_id, name, settings)
        self._create()


class KinaliRobot(KinaliMixin, Robot):

    def __init__(self, obj_id: str, name: str, pose: Pose, settings: KinaliSettings) -> None:
        super(KinaliRobot, self).__init__(obj_id, name, pose, settings)
        self._create()


__all__ = [
    KinaliSettings.__name__,
    KinaliObject.__name__,
    KinaliRobot.__name__
]

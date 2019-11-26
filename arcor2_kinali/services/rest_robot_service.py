from typing import Set, Optional, List
import os

from fastcache import clru_cache

from arcor2.services import RobotService
from arcor2.data.common import Pose, ActionMetadata, ActionPoint, Joint
from arcor2.action import action
from arcor2 import rest
from arcor2.object_types import Generic
from arcor2.data.object_type import ModelTypeEnum, MeshFocusAction
from arcor2.data.common import StrEnum


# TODO mixin for kinali services?
# TODO handle rest exceptions

URL = os.getenv("REST_ROBOT_SERVICE_URL", "http://127.0.0.1:13000")


def collision_id(obj: Generic) -> str:
    return obj.collision_model.type().value + "-" + obj.id


class MoveTypeEnum(StrEnum):

    AVOID_COLLISIONS: str = "AvoidCollisions"
    LINE: str = "Line"
    SIMPLE: str = "Simple"


class RestRobotService(RobotService):

    def __init__(self, configuration_id: str):

        super(RestRobotService, self).__init__(configuration_id)
        rest.put(f"{URL}/systems/{self.configuration_id}/create")  # TODO make this shared for all REST services (mixin?)

        self._robot_ids: Optional[Set[str]] = None

    @staticmethod
    def get_configuration_ids() -> Set[str]:
        return set(rest.get_data(f"{URL}/systems"))

    def add_collision(self, obj: Generic) -> None:
        if not obj.collision_model or obj.collision_model.type() == ModelTypeEnum.NONE:
            return
        params = obj.collision_model.to_dict()
        params["id"] = collision_id(obj)
        rest.put(f"{URL}/collisions/{obj.collision_model.type().value}", obj.pose, params)

    def remove_collision(self, obj: Generic) -> None:
        if not obj.collision_model or obj.collision_model.type() == ModelTypeEnum.NONE:
            return
        rest.delete(f"{URL}/collisions/{collision_id(obj)}")

    def get_robot_ids(self) -> Set[str]:

        if self._robot_ids is None:
            self._robot_ids = set(rest.get_data(f"{URL}/robots"))
        return self._robot_ids

    @clru_cache(maxsize=None)
    def get_robot_pose(self, robot_id: str) -> Pose:
        return rest.get(f"{URL}/robots/{robot_id}/pose", Pose)

    def stop(self, robot_id: str) -> None:
        rest.put(f"{URL}/robots/{robot_id}/stop")

    def robot_joints(self, robot_id: str) -> List[Joint]:
        return rest.get_list(f"{URL}/robots/{robot_id}/joints", Joint)

    @clru_cache(maxsize=None)
    def get_end_effectors_ids(self, robot_id: str) -> Set[str]:
        return set(rest.get_data(f"{URL}/robots/{robot_id}/endeffectors"))

    def get_end_effector_pose(self, robot_id: str, end_effector_id: str) -> Pose:
        return rest.get(f"{URL}/robots/{robot_id}/endeffectors/{end_effector_id}/pose", Pose)

    @action
    def end_effector_move(self, robot_id: str, end_effector_id: str, ap: ActionPoint, move_type: MoveTypeEnum,
                          speed: float) -> None:

        rest.put(f"{URL}/robots/{robot_id}/endeffectors/{end_effector_id}/move", ap.pose,
                 {"moveType": move_type.value, "speed": speed})

    @clru_cache(maxsize=None)
    def inputs(self, robot_id: str) -> Set[str]:
        return set(rest.get_data(f"{URL}/robots/{robot_id}/inputs"))

    @clru_cache(maxsize=None)
    def outputs(self, robot_id: str) -> Set[str]:
        return set(rest.get_data(f"{URL}/robots/{robot_id}/outputs"))

    @action
    def get_input(self, robot_id: str, input_id: str) -> float:
        super(RestRobotService, self).get_input(robot_id, input_id)
        return rest.get_float(f"{URL}/robots/{robot_id}/inputs/{input_id}")

    @action
    def set_output(self, robot_id: str, output_id: str, value: float) -> None:
        super(RestRobotService, self).set_output(robot_id, output_id, value)
        rest.put(f"{URL}/robots/{robot_id}/outputs/{output_id}", params={"value": value})

    def focus(self, mfa: MeshFocusAction) -> Pose:
        return rest.get(f"{URL}/utils/focus", Pose)

    @clru_cache(maxsize=None)
    def grippers(self, robot_id: str) -> Set[str]:
        return set(rest.get_data(f"{URL}/robots/{robot_id}/grippers"))

    @action
    def gripper_grip(self, robot_id: str, gripper_id: str, position: float, speed: float, force: float) -> None:
        rest.put(f"{URL}/robots/{robot_id}/grippers/{gripper_id}/grip", params={"position": position,
                                                                                "speed": speed,
                                                                                "force": force})

    @action
    def gripper_opening(self, robot_id: str, gripper_id: str, position: float, speed: float) -> None:
        rest.put(f"{URL}/robots/{robot_id}/grippers/{gripper_id}/opening", params={"position": position,
                                                                                   "speed": speed})

    @action
    def gripper_gripped(self, robot_id: str, gripper_id: str) -> bool:
        return rest.get_bool(f"{URL}/robots/{robot_id}/grippers/{gripper_id}/gripped")

    @clru_cache(maxsize=None)
    def suctions(self, robot_id: str) -> Set[str]:
        return set(rest.get_data(f"{URL}/robots/{robot_id}/suctions"))

    @action
    def suctions_suck(self, robot_id: str, suction_id: str) -> None:
        rest.put(f"{URL}/robots/{robot_id}/suctions/{suction_id}/suck")

    @action
    def suctions_release(self, robot_id: str, suction_id: str) -> None:
        rest.put(f"{URL}/robots/{robot_id}/suctions/{suction_id}/release")

    @action
    def suctions_attached(self, robot_id: str, suction_id: str) -> bool:
        return rest.get_bool(f"{URL}/robots/{robot_id}/suctions/{suction_id}/attached")

    end_effector_move.__action__ = ActionMetadata(free=True, blocking=True)
    get_input.__action__ = ActionMetadata(free=True, blocking=True)
    set_output.__action__ = ActionMetadata(free=True, blocking=True)
    gripper_grip.__action__ = ActionMetadata(free=True, blocking=True)
    gripper_opening.__action__ = ActionMetadata(free=True, blocking=True)
    gripper_gripped.__action__ = ActionMetadata(free=True, blocking=True)
    suctions_suck.__action__ = ActionMetadata(free=True, blocking=True)
    suctions_release.__action__ = ActionMetadata(free=True, blocking=True)
    suctions_attached.__action__ = ActionMetadata(free=True, blocking=True)


RestRobotService.DYNAMIC_PARAMS = {
    "robot_id": (RestRobotService.get_robot_ids, set()),
    "end_effector_id": (RestRobotService.get_end_effectors_ids, {"robot_id"}),
    "gripper_id": (RestRobotService.grippers, {"robot_id"}),
    "suction_id": (RestRobotService.suctions, {"robot_id"}),
    "input_id": (RestRobotService.inputs, {"robot_id"}),
    "output_id": (RestRobotService.outputs, {"robot_id"})
}

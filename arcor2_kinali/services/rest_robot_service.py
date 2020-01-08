from typing import Set, Optional, List
import os
from dataclasses import dataclass

from dataclasses_jsonschema import JsonSchemaMixin

from arcor2.services import RobotService
from arcor2.data.common import Pose, ActionMetadata, RobotJoints, Joint, RelativePose, StrEnum, Position, Orientation
from arcor2.action import action
from arcor2 import rest
from arcor2.object_types import Generic
from arcor2.data.object_type import ModelTypeEnum, MeshFocusAction

# TODO handle rest exceptions

URL = os.getenv("REST_ROBOT_SERVICE_URL", "http://127.0.0.1:13000")


def collision_id(obj: Generic) -> str:
    assert obj.collision_model is not None
    return obj.collision_model.type().value + "-" + obj.id


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


class RestRobotService(RobotService):
    """
    REST interface to the robot service.
    """

    def __init__(self, configuration_id: str):

        super(RestRobotService, self).__init__(configuration_id)
        # TODO make this shared for all REST services (mixin?)
        rest.put(f"{URL}/systems/{self.configuration_id}/create")

        self._robot_ids: Optional[Set[str]] = None

    @staticmethod
    def get_configuration_ids() -> Set[str]:
        return set(rest.get_data(f"{URL}/systems"))

    def add_collision(self, obj: Generic) -> None:
        if not obj.collision_model or obj.collision_model.type() == ModelTypeEnum.NONE:
            return
        params = obj.collision_model.to_dict()
        params["id"] = collision_id(obj)

        # TODO temporary hack
        if obj.collision_model.type() == ModelTypeEnum.MESH:
            params["mesh_scale_x"] = 1.0
            params["mesh_scale_y"] = 1.0
            params["mesh_scale_z"] = 1.0
            params["transform_id"] = "world"

        rest.put(f"{URL}/collisions/{obj.collision_model.type().value}", obj.pose, params)

    def remove_collision(self, obj: Generic) -> None:
        if not obj.collision_model or obj.collision_model.type() == ModelTypeEnum.NONE:
            return
        rest.delete(f"{URL}/collisions/{collision_id(obj)}")

    def get_robot_ids(self) -> Set[str]:

        if self._robot_ids is None:
            self._robot_ids = set(rest.get_data(f"{URL}/robots"))
        return self._robot_ids

    def get_robot_pose(self, robot_id: str) -> Pose:
        return rest.get(f"{URL}/robots/{robot_id}/pose", Pose)

    def stop(self, robot_id: str) -> None:
        rest.put(f"{URL}/robots/{robot_id}/stop")

    def robot_joints(self, robot_id: str) -> List[Joint]:
        return rest.get_list(f"{URL}/robots/{robot_id}/joints", Joint)

    def get_end_effectors_ids(self, robot_id: str) -> Set[str]:
        return set(rest.get_data(f"{URL}/robots/{robot_id}/endeffectors"))

    def get_end_effector_pose(self, robot_id: str, end_effector_id: str) -> Pose:
        return rest.get(f"{URL}/robots/{robot_id}/endeffectors/{end_effector_id}/pose", Pose)

    @action
    def move(self, robot_id: str, end_effector_id: str, pose: Pose, move_type: MoveTypeEnum,
             speed: float = 0.5) -> None:
        """
        Moves the robot's end-effector to a specific pose.
        :param robot_id: Unique robot id.
        :param end_effector_id: Unique end-effector id.
        :param pose: Target pose.
        :param move_type: Type of move.
        :param speed: Speed of move.
        :return:
        """

        rest.put(f"{URL}/robots/{robot_id}/endeffectors/{end_effector_id}/move", pose,
                 {"moveType": move_type.value, "speed": speed})

    @action
    def move_relative(self, robot_id: str, end_effector_id: str, pose: Pose, rel_pose: RelativePose,
                      move_type: MoveTypeEnum, speed: float = 0.5) -> None:
        """
        Moves the robot's end-effector to a specific pose.
        :param robot_id: Unique robot id.
        :param end_effector_id: Unique end-effector id.
        :param pose: Target pose.
        :param rel_pose: Relative pose.
        :param move_type: Type of move.
        :param speed: Speed of move.
        :return:
        """

        body = MoveRelativeParameters(pose, rel_pose.position, rel_pose.orientation)
        rest.put(f"{URL}/robots/{robot_id}/endeffectors/{end_effector_id}/move_relative", body,
                 {"moveType": move_type.value, "speed": speed})

    @action
    def move_relative_joints(self, robot_id: str, end_effector_id: str, joints: RobotJoints,
                             rel_pose: RelativePose, move_type: MoveTypeEnum, speed: float = 0.5) -> None:
        """
        Moves the robot's end-effector relatively to specific joint values.
        :param robot_id: Unique robot id.
        :param end_effector_id: Unique end-effector id.
        :param joints: Target joints.
        :param rel_pose: Relative pose.
        :param move_type: Type of move.
        :param speed: Speed of move.
        :return:
        """

        body = MoveRelativeJointsParameters(joints.joints, rel_pose.position, rel_pose.orientation)
        rest.put(f"{URL}/robots/{robot_id}/endeffectors/{end_effector_id}/move_relative_joints", body,
                 {"moveType": move_type.value, "speed": speed})

    @action
    def set_joints(self, robot_id: str, joints: RobotJoints, move_type: MoveTypeEnum, speed: float = 0.5) -> None:

        assert robot_id == joints.robot_id
        rest.put(f"{URL}/robots/{robot_id}/joints", joints.joints, {"moveType": move_type.value, "speed": speed})

    def inputs(self, robot_id: str) -> Set[str]:
        return set(rest.get_data(f"{URL}/robots/{robot_id}/inputs"))

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
        return rest.put(f"{URL}/utils/focus", mfa, data_cls=Pose)

    def grippers(self, robot_id: str) -> Set[str]:
        return set(rest.get_data(f"{URL}/robots/{robot_id}/grippers"))

    @action
    def grip(self, robot_id: str, gripper_id: str, position: float, speed: float, force: float) -> None:
        rest.put(f"{URL}/robots/{robot_id}/grippers/{gripper_id}/grip", params={"position": position,
                                                                                "speed": speed,
                                                                                "force": force})

    @action
    def set_opening(self, robot_id: str, gripper_id: str, position: float, speed: float) -> None:
        rest.put(f"{URL}/robots/{robot_id}/grippers/{gripper_id}/opening", params={"position": position,
                                                                                   "speed": speed})

    @action
    def is_item_gripped(self, robot_id: str, gripper_id: str) -> bool:
        return rest.get_bool(f"{URL}/robots/{robot_id}/grippers/{gripper_id}/gripped")

    def suctions(self, robot_id: str) -> Set[str]:
        return set(rest.get_data(f"{URL}/robots/{robot_id}/suctions"))

    @action
    def suck(self, robot_id: str, suction_id: str) -> None:
        rest.put(f"{URL}/robots/{robot_id}/suctions/{suction_id}/suck")

    @action
    def release(self, robot_id: str, suction_id: str) -> None:
        rest.put(f"{URL}/robots/{robot_id}/suctions/{suction_id}/release")

    @action
    def is_item_attached(self, robot_id: str, suction_id: str) -> bool:
        return rest.get_bool(f"{URL}/robots/{robot_id}/suctions/{suction_id}/attached")

    move.__action__ = ActionMetadata(free=True, blocking=True)
    move_relative.__action__ = ActionMetadata(free=True, blocking=True)
    set_joints.__action__ = ActionMetadata(free=True, blocking=True)
    get_input.__action__ = ActionMetadata(free=True, blocking=True)
    set_output.__action__ = ActionMetadata(free=True, blocking=True)
    grip.__action__ = ActionMetadata(free=True, blocking=True)
    set_opening.__action__ = ActionMetadata(free=True, blocking=True)
    is_item_gripped.__action__ = ActionMetadata(free=True, blocking=True)
    suck.__action__ = ActionMetadata(free=True, blocking=True)
    release.__action__ = ActionMetadata(free=True, blocking=True)
    is_item_attached.__action__ = ActionMetadata(free=True, blocking=True)


RestRobotService.DYNAMIC_PARAMS = {
    "robot_id": (RestRobotService.get_robot_ids.__name__, set()),
    "end_effector_id": (RestRobotService.get_end_effectors_ids.__name__, {"robot_id"}),
    "gripper_id": (RestRobotService.grippers.__name__, {"robot_id"}),
    "suction_id": (RestRobotService.suctions.__name__, {"robot_id"}),
    "input_id": (RestRobotService.inputs.__name__, {"robot_id"}),
    "output_id": (RestRobotService.outputs.__name__, {"robot_id"})
}

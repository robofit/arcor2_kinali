from typing import Callable, List, Set, TYPE_CHECKING, TypeVar

from arcor2 import DynamicParamTuple as DPT, rest
from arcor2.action import action
from arcor2.data.common import ActionMetadata, Joint, Pose, ProjectRobotJoints
from arcor2.data.object_type import MeshFocusAction
from arcor2.parameter_plugins.relative_pose import RelativePose

from arcor2_kinali.data.robot import MoveRelativeJointsParameters, MoveRelativeParameters, MoveTypeEnum
from arcor2_kinali.object_types.kinali_object import KinaliRobot


# mypy work-around by GvR (https://github.com/python/mypy/issues/5107#issuecomment-529372406)
if TYPE_CHECKING:
    F = TypeVar('F', bound=Callable)

    def lru_cache(maxsize: int = 128, typed: bool = False) -> Callable[[F], F]:
        pass
else:
    from functools import lru_cache


class RestRobot(KinaliRobot):
    """
    REST interface to the robot service.
    """

    def move_to_pose(self, end_effector_id: str, target_pose: Pose, speed: float) -> None:

        rest.put(f"{self.settings.url}/endeffectors/{end_effector_id}/move", target_pose,
                 {"moveType": MoveTypeEnum.AVOID_COLLISIONS.value, "speed": speed})

    def move_to_joints(self, target_joints: List[Joint], speed: float) -> None:

        rest.put(f"{self.settings.url}/joints", target_joints,
                 {"moveType": MoveTypeEnum.AVOID_COLLISIONS.value, "speed": speed})

    def stop(self) -> None:
        rest.put(f"{self.settings.url}/stop")

    def robot_joints(self) -> List[Joint]:
        return rest.get_list(f"{self.settings.url}/joints", Joint)

    @lru_cache()
    def get_end_effectors_ids(self) -> Set[str]:
        return set(rest.get_data(f"{self.settings.url}/endeffectors"))

    def get_end_effector_pose(self, end_effector_id: str) -> Pose:
        return rest.get(f"{self.settings.url}/endeffectors/{end_effector_id}/pose", Pose)

    @action
    def move(self, end_effector_id: str, pose: Pose, move_type: MoveTypeEnum,
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

        assert 0.0 <= speed <= 1.0

        rest.put(f"{self.settings.url}/endeffectors/{end_effector_id}/move", pose,
                 {"moveType": move_type.value, "speed": speed})

    @action
    def move_relative(self, end_effector_id: str, pose: Pose, rel_pose: RelativePose,
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

        assert 0.0 <= speed <= 1.0

        body = MoveRelativeParameters(pose, rel_pose.position, rel_pose.orientation)
        rest.put(f"{self.settings.url}/endeffectors/{end_effector_id}/moveRelative", body,
                 {"moveType": move_type.value, "speed": speed})

    @action
    def move_relative_joints(self, end_effector_id: str, joints: ProjectRobotJoints,
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

        assert 0.0 <= speed <= 1.0

        body = MoveRelativeJointsParameters(joints.joints, rel_pose.position, rel_pose.orientation)
        rest.put(f"{self.settings.url}/endeffectors/{end_effector_id}/moveRelativeJoints", body,
                 {"moveType": move_type.value, "speed": speed})

    @action
    def set_joints(self, joints: ProjectRobotJoints, move_type: MoveTypeEnum,
                   speed: float = 0.5) -> None:

        assert 0.0 <= speed <= 1.0
        # assert robot_id == joints.robot_id
        rest.put(f"{self.settings.url}/joints", joints.joints, {"moveType": move_type.value, "speed": speed})

    @lru_cache()
    def inputs(self) -> Set[str]:
        return set(rest.get_data(f"{self.settings.url}/inputs"))

    @lru_cache()
    def outputs(self) -> Set[str]:
        return set(rest.get_data(f"{self.settings.url}/outputs"))

    @action
    def get_input(self, input_id: str) -> float:
        return rest.get_primitive(f"{self.settings.url}/inputs/{input_id}", float)

    @action
    def set_output(self, output_id: str, value: float) -> None:

        assert 0.0 <= value <= 1.0
        rest.put(f"{self.settings.url}/outputs/{output_id}", params={"value": value})

    @action
    def get_output(self, output_id: str) -> float:
        return rest.get_primitive(f"{self.settings.url}/outputs/{output_id}", float)

    def focus(self, mfa: MeshFocusAction) -> Pose:
        return rest.put(f"{self.settings.url}/utils/focus", mfa, data_cls=Pose)

    @lru_cache()
    def grippers(self) -> Set[str]:
        return set(rest.get_data(f"{self.settings.url}/grippers"))

    @action
    def grip(self, gripper_id: str, position: float = 0.0, speed: float = 0.5, force: float = 0.5) -> \
            None:

        assert 0.0 <= position <= 1.0
        assert 0.0 <= speed <= 1.0
        assert 0.0 <= force <= 1.0

        rest.put(f"{self.settings.url}/grippers/{gripper_id}/grip",
                 params={"position": position, "speed": speed, "force": force})

    @action
    def set_opening(self, gripper_id: str, position: float = 1.0, speed: float = 0.5) -> None:

        assert 0.0 <= position <= 1.0
        assert 0.0 <= speed <= 1.0

        rest.put(f"{self.settings.url}/grippers/{gripper_id}/opening",
                 params={"position": position, "speed": speed})

    @action
    def get_gripper_opening(self, gripper_id: str) -> float:

        return rest.get_primitive(f"{self.settings.url}/grippers/{gripper_id}/opening", float)

    @action
    def is_item_gripped(self, gripper_id: str) -> bool:
        return rest.get_primitive(f"{self.settings.url}/grippers/{gripper_id}/gripped", bool)

    @lru_cache()
    def suctions(self) -> Set[str]:
        return set(rest.get_data(f"{self.settings.url}/suctions"))

    @action
    def suck(self, suction_id: str) -> None:
        rest.put(f"{self.settings.url}/suctions/{suction_id}/suck")

    @action
    def release(self, suction_id: str) -> None:
        rest.put(f"{self.settings.url}/suctions/{suction_id}/release")

    @action
    def is_item_attached(self, suction_id: str) -> bool:
        return rest.get_primitive(f"{self.settings.url}/suctions/{suction_id}/attached", bool)

    move.__action__ = ActionMetadata(blocking=True)  # type: ignore
    move_relative.__action__ = ActionMetadata(blocking=True)  # type: ignore
    move_relative_joints.__action__ = ActionMetadata(blocking=True)  # type: ignore
    set_joints.__action__ = ActionMetadata(blocking=True)  # type: ignore
    get_input.__action__ = ActionMetadata(blocking=True)  # type: ignore
    set_output.__action__ = ActionMetadata(blocking=True)  # type: ignore
    get_output.__action__ = ActionMetadata(blocking=True)  # type: ignore
    grip.__action__ = ActionMetadata(blocking=True)  # type: ignore
    set_opening.__action__ = ActionMetadata(blocking=True)  # type: ignore
    get_gripper_opening.__action__ = ActionMetadata(blocking=True)  # type: ignore
    is_item_gripped.__action__ = ActionMetadata(blocking=True)  # type: ignore
    suck.__action__ = ActionMetadata(blocking=True)  # type: ignore
    release.__action__ = ActionMetadata(blocking=True)  # type: ignore
    is_item_attached.__action__ = ActionMetadata(blocking=True)  # type: ignore


RestRobot.DYNAMIC_PARAMS = {
    "end_effector_id": DPT(RestRobot.get_end_effectors_ids.__name__, set()),
    "gripper_id": DPT(RestRobot.grippers.__name__, set()),
    "suction_id": DPT(RestRobot.suctions.__name__, set()),
    "input_id": DPT(RestRobot.inputs.__name__, set()),
    "output_id": DPT(RestRobot.outputs.__name__, set())
}

RestRobot.CANCEL_MAPPING = {
    RestRobot.move.__name__: RestRobot.stop.__name__,
    RestRobot.move_relative.__name__: RestRobot.stop.__name__,
    RestRobot.move_relative_joints.__name__: RestRobot.stop.__name__,
    RestRobot.set_joints.__name__: RestRobot.stop.__name__
}

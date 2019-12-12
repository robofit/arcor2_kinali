from typing import Iterator, Set, Optional, List

from arcor2.object_types import Robot
from arcor2.data.common import Pose, ActionMetadata, Joint, RelativePose, RobotJoints
from arcor2.data.object_type import MeshFocusAction, Models
try:
    # for development
    from arcor2_kinali.services.rest_robot_service import RestRobotService, MoveTypeEnum
except ImportError:
    # for execution package
    from ..services.rest_robot_service import RestRobotService, MoveTypeEnum
from arcor2.action import action
from arcor2.exceptions import Arcor2Exception

# TODO how to copy docstrings of methods from service?


class RestRobot(Robot):
    """
    REST interface to the robot.
    """

    def __init__(self, robot_api: RestRobotService, obj_id: str, pose: Pose,
                 collision_model: Optional[Models] = None) -> None:

        super(RestRobot, self).__init__(obj_id, pose, collision_model)
        self.robot_api = robot_api

    def get_end_effectors_ids(self) -> Set[str]:
        return self.robot_api.get_end_effectors_ids(self.id)

    def get_end_effector_pose(self, end_effector_id: str) -> Pose:  # global pose
        return self.robot_api.get_end_effector_pose(self.id, end_effector_id)

    @staticmethod
    def from_services(robot_api: RestRobotService) -> Iterator["RestRobot"]:

        # TODO what if robot does not support get_robot_pose?
        for robot_id in robot_api.get_robot_ids():
            try:
                yield RestRobot(robot_api, robot_id, robot_api.get_robot_pose(robot_id))
            except Arcor2Exception as e:
                print(e)

    def stop(self) -> None:
        self.robot_api.stop(self.id)

    def robot_joints(self) -> List[Joint]:
        return self.robot_api.robot_joints(self.id)

    @action
    def end_effector_move(self, end_effector_id: str, pose: Pose, move_type: MoveTypeEnum, speed: float) -> None:
        """
        Moves the robot's end-effector to a specific pose.
        :param end_effector_id: Unique end-effector id.
        :param pose: Target pose.
        :param move_type: Type of move.
        :param speed: Speed of move.
        :return:
        """

        self.robot_api.end_effector_move(self.id, end_effector_id, pose, move_type, speed)

    @action
    def end_effector_move_relative(self, end_effector_id: str, pose: Pose, rel_pose: RelativePose,
                                   move_type: MoveTypeEnum, speed: float) -> None:
        """
        Moves the robot's end-effector to a specific pose.
        :param end_effector_id: Unique end-effector id.
        :param pose: Target pose.
        :param rel_pose: Relative pose.
        :param move_type: Type of move.
        :param speed: Speed of move.
        :return:
        """

        pass

    @action
    def set_joints(self, joints: RobotJoints, move_type: MoveTypeEnum, speed: float) -> None:

        assert self.id == joints.robot_id
        self.robot_api.set_joints(self.id, joints, move_type, speed)

    def inputs(self) -> Set[str]:
        return self.robot_api.inputs(self.id)

    def outputs(self, robot_id: str) -> Set[str]:
        return self.robot_api.outputs(self.id)

    @action
    def get_input(self, input_id: str) -> float:
        return self.robot_api.get_input(input_id)

    @action
    def set_output(self, output_id: str, value: float) -> None:
        self.robot_api.set_output(output_id)

    def focus(self, mfa: MeshFocusAction) -> Pose:
        return self.robot_api.focus(mfa)

    def grippers(self) -> Set[str]:
        return self.robot_api.grippers(self.id)

    @action
    def gripper_grip(self, gripper_id: str, position: float, speed: float, force: float) -> None:
        return self.robot_api.gripper_grip(self.id, gripper_id, position, speed, force)

    @action
    def gripper_opening(self, gripper_id: str, position: float, speed: float) -> None:
        self.robot_api.gripper_opening(self.id, gripper_id, position, speed)

    @action
    def gripper_gripped(self, gripper_id: str) -> bool:
        return self.robot_api.gripper_gripped(self.id, gripper_id)

    def suctions(self) -> Set[str]:
        return self.robot_api.suctions(self.id)

    @action
    def suctions_suck(self, suction_id: str) -> None:
        self.robot_api.suctions_suck(self.id, suction_id)

    @action
    def suctions_release(self, suction_id: str) -> None:
        self.robot_api.suctions_release(self.id, suction_id)

    @action
    def suctions_attached(self, suction_id: str) -> bool:
        return self.robot_api.suctions_attached(self.id, suction_id)

    end_effector_move.__action__ = ActionMetadata(free=True, blocking=True, composite=True, blackbox=True)
    end_effector_move_relative.__action__ = ActionMetadata(free=True, blocking=True, composite=True, blackbox=True)
    set_joints.__action__ = ActionMetadata(free=True, blocking=True, composite=True, blackbox=True)
    get_input.__action__ = ActionMetadata(free=True, blocking=True, composite=True, blackbox=True)
    set_output.__action__ = ActionMetadata(free=True, blocking=True, composite=True, blackbox=True)
    gripper_grip.__action__ = ActionMetadata(free=True, blocking=True, composite=True, blackbox=True)
    gripper_opening.__action__ = ActionMetadata(free=True, blocking=True, composite=True, blackbox=True)
    gripper_gripped.__action__ = ActionMetadata(free=True, blocking=True, composite=True, blackbox=True)
    suctions_suck.__action__ = ActionMetadata(free=True, blocking=True, composite=True, blackbox=True)
    suctions_release.__action__ = ActionMetadata(free=True, blocking=True, composite=True, blackbox=True)
    suctions_attached.__action__ = ActionMetadata(free=True, blocking=True, composite=True, blackbox=True)


RestRobot.DYNAMIC_PARAMS = {
    "end_effector_id": (RestRobot.get_end_effectors_ids.__name__, set()),
    "gripper_id": (RestRobot.grippers.__name__, {"robot_id"}),
    "suction_id": (RestRobot.suctions.__name__, {"robot_id"}),
    "input_id": (RestRobot.inputs.__name__, {"robot_id"}),
    "output_id": (RestRobot.outputs.__name__, {"robot_id"})
}
from typing import Iterator, Set, Optional

from arcor2.object_types import Robot
from arcor2.data.common import Pose, ActionMetadata
from arcor2.data.object_type import MeshFocusAction, Models
# TODO relative import (to make it work in execution package)
from arcor2_kinali.services.rest_robot_service import RestRobotService, MoveTypeEnum
from arcor2.action import action
from arcor2.exceptions import Arcor2Exception

# TODO focus


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

    def get_end_effector_pose(self, end_effector: str) -> Pose:  # global pose
        return self.robot_api.get_end_effector_pose(self.id, end_effector)

    @staticmethod
    def from_services(robot_api: RestRobotService) -> Iterator["RestRobot"]:

        # TODO what if robot does not support get_robot_pose?
        for robot_id in robot_api.get_robot_ids():
            try:
                yield RestRobot(robot_api, robot_id, robot_api.get_robot_pose(robot_id))
            except Arcor2Exception as e:
                print(e)

    @action
    def end_effector_move(self, end_effector_id: str, pose: Pose, speed: float) -> None:

        move_type = MoveTypeEnum.AVOID_COLLISIONS
        self.robot_api.end_effector_move(self.id, end_effector_id, pose, move_type, speed)

    def focus(self, mfa: MeshFocusAction) -> Pose:
        return self.robot_api.focus(mfa)

    end_effector_move.__action__ = ActionMetadata(free=True, blocking=True, composite=True, blackbox=True)

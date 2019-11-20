from typing import Iterator, Optional, Set

from arcor2.object_types import Robot
from arcor2.data.common import Pose, ActionPoint, ActionMetadata
from arcor2_kinali.services.rest_robot_service import RestRobotService
from arcor2.action import action

from arcor2_kinali.data.common import MoveTypeEnum
# TODO focus


class RestRobot(Robot):

    def __init__(self,
                 robot_api: RestRobotService,
                 name: Optional[str] = None,
                 pose: Optional[Pose] = None) -> None:

        super(RestRobot, self).__init__(name, pose)  # TODO distinguish id and (human-readable) name?
        self.robot_api = robot_api

    def get_end_effectors_ids(self) -> Set[str]:
        return self.robot_api.get_end_effectors_ids(self.id)

    def get_end_effector_pose(self, end_effector: str) -> Pose:  # global pose
        return self.robot_api.get_end_effector_pose(self.id, end_effector)

    @staticmethod
    def from_services(robot_api: RestRobotService) -> Iterator["RestRobot"]:

        for robot_id in robot_api.get_robot_ids():
            yield RestRobot(robot_api, robot_id, robot_api.get_robot_pose(robot_id))

    @action
    def end_effector_move(self, end_effector_id: str, ap: ActionPoint, speed: float) -> None:

        move_type = MoveTypeEnum.AVOID_COLLISIONS
        self.robot_api.end_effector_move(self.id, end_effector_id, ap, move_type, speed)

    end_effector_move.__action__ = ActionMetadata(free=True, blocking=True, composite=True, blackbox=True)

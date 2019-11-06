from typing import Iterator, Optional

from arcor2.object_types import Robot
from arcor2.data.common import Pose, ActionPoint
from arcor2_kinali.services.rest_robot_service import RestRobotService


class RestRobot(Robot):

    def __init__(self,
                 robot_api: RestRobotService,
                 name: Optional[str] = None,
                 pose: Optional[Pose] = None) -> None:

        super(RestRobot, self).__init__(name, pose)  # TODO distinguish id and (human-readable) name?
        self.robot_api = robot_api

    def get_pose(self, end_effector: str) -> Pose:
        return self.robot_api.get_robot_pose(self.name)

    @staticmethod
    def from_services(robot_api: RestRobotService) -> Iterator["RestRobot"]:

        for robot_id in robot_api.get_robot_ids():
            yield RestRobot(robot_api, robot_id, robot_api.get_robot_pose(robot_id))

    def end_effector_move(self, end_effector_id: str, ap: ActionPoint):
        self.robot_api.end_effector_move(self.name, end_effector_id, ap)

from typing import Set

from arcor2.services import RobotService
from arcor2.data.common import Pose, ActionMetadata, ActionPoint, Position, Orientation
from arcor2.action import action
from arcor2 import rest

from arcor2_kinali.data.common import MoveTypeEnum

# TODO mixin for kinali services?
# TODO handle rest exceptions


class RestRobotService(RobotService):

    def __init__(self, configuration_id: str):

        super(RestRobotService, self).__init__(configuration_id)
        rest.put(f"/systems/{self.configuration_id}/create")  # TODO make this shared for all REST services (mixin?)

    @staticmethod
    def get_configuration_ids() -> Set[str]:
        return set(rest.get_data("/systems"))

    def get_robot_ids(self) -> Set[str]:
        return set(rest.get_data("/robots"))

    def get_robot_pose(self, robot_id: str) -> Pose:
        return rest.get(f"/robots/{robot_id}/pose", Pose)

    def stop(self, robot_id: str) -> None:
        rest.put(f"/robots/{robot_id}/stop")

    def get_end_effectors_ids(self, robot_id: str) -> Set[str]:
        return set(rest.get_data(f"/robots/{robot_id}/endeffectors"))

    def get_end_effector_pose(self, robot_id: str, end_effector_id: str) -> Pose:
        return rest.get(f"/robots/{robot_id}/{end_effector_id}/pose", Pose)

    @action
    def end_effector_move(self, robot_id: str, end_effector_id: str, ap: ActionPoint, speed: float) -> None:

        move_type = MoveTypeEnum.AVOID_COLLISIONS
        rest.put(f"/robots/{robot_id}/{end_effector_id}/move?moveType={move_type.value}&speed={speed}", ap.pose)

    end_effector_move.__action__ = ActionMetadata(free=True, blocking=True)

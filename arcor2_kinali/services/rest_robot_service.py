from typing import Set

from arcor2.services import RobotService
from arcor2.data.common import Pose, ActionMetadata, ActionPoint, Position, Orientation
from arcor2.action import action
from arcor2 import rest

# TODO handle rest exceptions


class RestRobotService(RobotService):

    def __init__(self, configuration_id: str):

        # TODO call create
        pass

    @staticmethod
    def get_configuration_ids() -> Set[str]:
        return {"conf1", "conf2"}

    def get_robot_ids(self) -> Set[str]:
        # return set(rest.get_list("/robots", str))  # get_list pracuje s JsonSchemaMixin...
        return {"robot1", "robot2"}

    def get_robot_pose(self, robot_id: str) -> Pose:
        # return rest.get(f"/robots/{robot_id}/pose", Pose)
        return Pose(Position(0, 0, 0), Orientation(0, 0, 0, 1))

    def stop(self, robot_id: str) -> None:

        rest.put(f"/robots/{robot_id}/stop")

    def get_end_effectors_ids(self, robot_id: str) -> Set[str]:
        return set("eeBig")

    def get_end_effector_pose(self, robot_id: str, end_effector_id: str) -> Pose:
        return rest.get(f"/robots/{robot_id}/{end_effector_id}/pose", Pose)

    @action
    def end_effector_move(self, robot_id: str, end_effector_id: str, ap: ActionPoint):
        # TODO transform AP using resources class
        rest.put(f"/robots/{robot_id}/{end_effector_id}/move", ap.pose)  # pose: Pose, moveType: MoveType, speed: float

    end_effector_move.__action__ = ActionMetadata(free=True, blocking=True)

from typing import Set
import os
import copy

from arcor2.services import RobotService
from arcor2.data.common import Pose, ActionMetadata, ActionPoint
from arcor2.action import action
from arcor2 import rest
from arcor2.object_types import Generic
from arcor2.data.object_type import ModelTypeEnum

from arcor2_kinali.data.common import MoveTypeEnum

# TODO mixin for kinali services?
# TODO handle rest exceptions

URL = os.getenv("REST_ROBOT_SERVICE_URL", "http://127.0.0.1:10000")

def collision_id(obj: Generic) -> str:
    return obj.collision_model.type().value + "-" + obj.id


class RestRobotService(RobotService):

    def __init__(self, configuration_id: str):

        super(RestRobotService, self).__init__(configuration_id)
        # rest.put(f"{URL}/systems/{self.configuration_id}/create")  # TODO make this shared for all REST services (mixin?)

    @staticmethod
    def get_configuration_ids() -> Set[str]:
        # return set(rest.get_data(f"{URL}/systems"))
        return {"conf1", "conf2"}

    def add_collision(self, obj: Generic) -> None:
        assert obj.collision_model and obj.collision_model.type() != ModelTypeEnum.NONE
        params = copy.deepcopy(obj.collision_model.__dict__)
        params["id"] = collision_id(obj)
        # rest.put(f"{URL}/collisions/{obj.collision_model.type()}", obj.pose, params)

    def remove_collision(self, obj: Generic) -> None:
        assert obj.collision_model and obj.collision_model.type() != ModelTypeEnum.NONE
        # rest.delete(f"{URL}/collisions/{collision_id(obj)}")

    def get_robot_ids(self) -> Set[str]:
        # return set(rest.get_data(f"{URL}/robots"))
        return {"r1", "r2"}

    def get_robot_pose(self, robot_id: str) -> Pose:
        # return rest.get(f"{URL}/robots/{robot_id}/pose", Pose)
        return Pose()

    def stop(self, robot_id: str) -> None:
        rest.put(f"{URL}/robots/{robot_id}/stop")

    def get_end_effectors_ids(self, robot_id: str) -> Set[str]:
        # return set(rest.get_data(f"{URL}/robots/{robot_id}/endeffectors"))
        return {"ee"}

    def get_end_effector_pose(self, robot_id: str, end_effector_id: str) -> Pose:
        # return rest.get(f"{URL}/robots/{robot_id}/{end_effector_id}/pose", Pose)
        return Pose()

    @action
    def end_effector_move(self, robot_id: str, end_effector_id: str, ap: ActionPoint, speed: float) -> None:

        move_type = MoveTypeEnum.AVOID_COLLISIONS
        # rest.put(f"{URL}/robots/{robot_id}/{end_effector_id}/move?moveType={move_type.value}&speed={speed}", ap.pose)

    end_effector_move.__action__ = ActionMetadata(free=True, blocking=True)

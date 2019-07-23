from arcor2.object_types import Robot
from arcor2.object_types.utils import action
from arcor2.data import ActionMetadata, ActionPoint
from arcor2.exceptions import RobotException
from swagger_client import ApirobotMoveApi, ApiClient
from swagger_client import Move, Pose6d, Vec3
from arcor2_kinali.conf import API_CLIENT_CONF
from swagger_client.rest import ApiException
import time

"""
This file is going to be auto-generated based on API specification. So far, it's handwritten.
"""


class KinaliRobot(Robot):

    def __init__(self, *args, **kwargs):

        super(KinaliRobot, self).__init__(*args, **kwargs)

        self.api = ApirobotMoveApi(ApiClient(API_CLIENT_CONF))

    @action
    def move_to(self, target: ActionPoint, end_effector: str, speed: int) -> None:

        # TODO action point pose should be relative to its parent object pose - how and where to get the absolute pose?

        ts_start = time.monotonic()

        # TODO convert orientation from quaternion to rpy (which convention?)
        try:
            self.api.put(move=Move(pose=Pose6d(position=Vec3(*target.pose.position.to_list()), rotation=Vec3(0, 0, 0))))
        except ApiException as e:
            print(e)
            raise RobotException()

        ts_end = time.monotonic()
        dur = ts_end - ts_start

        # this is just for testing purposes...
        if dur < 1.0:
            time.sleep(1.0 - dur)

    move_to.__action__ = ActionMetadata(free=True, blocking=True)

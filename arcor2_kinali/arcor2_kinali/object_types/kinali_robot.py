from arcor2.object_types import Robot
from arcor2.action import action
from arcor2.data import ActionMetadata, ActionPoint
from arcor2.exceptions import RobotException
from swagger_client import RobotApi, ApiClient
from swagger_client import Move, Pose6d, Vector3
from arcor2_kinali.conf import API_CLIENT_CONF
from swagger_client.rest import ApiException
import time

"""
This file is going to be auto-generated based on API specification. So far, it's handwritten.
"""


class KinaliRobot(Robot):

    def __init__(self, *args, **kwargs):

        super(KinaliRobot, self).__init__(*args, **kwargs)

        self.api = RobotApi(ApiClient(API_CLIENT_CONF))

    @action
    def move_to(self, target: ActionPoint, end_effector: str, speed: int) -> None:

        # TODO action point pose should be relative to its parent object pose - how and where to get the absolute pose?

        ts_start = time.monotonic()

        # TODO convert orientation from quaternion to rpy (which convention?)
        try:
            self.api.pose_put(move=Move(position=Vector3(*target.pose.position),
                                        rotation=Vector3(0, 0, 0),
                                        end_effector=end_effector))
        except ApiException as e:
            print(e)
            raise RobotException()

        ts_end = time.monotonic()
        dur = ts_end - ts_start

        # this is just for testing purposes...
        if dur < 1.0:
            time.sleep(1.0 - dur)

    move_to.__action__ = ActionMetadata(free=True, blocking=True)

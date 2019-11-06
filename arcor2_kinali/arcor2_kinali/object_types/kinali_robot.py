import json
import time

from arcor2.object_types import Robot
from arcor2.action import action
from arcor2.data.common import ActionMetadata, ActionPoint, Pose, Position, Orientation
from arcor2.data.object_type import MeshFocusAction
from arcor2.exceptions import RobotException
from swagger_client import RobotApi, ApiClient
from swagger_client import Move, Vector3, Quaternion, Pose6d, MeshFocusAction as MeshFocusActionSw, OpenProject
from arcor2_kinali.conf import API_CLIENT_CONF
from swagger_client.rest import ApiException
from urllib3.exceptions import MaxRetryError

"""
This file is going to be auto-generated based on API specification. So far, it's handwritten.
"""


class KinaliRobot(Robot):

    def __init__(self, *args, **kwargs):

        super(KinaliRobot, self).__init__(*args, **kwargs)

        self.api = RobotApi(ApiClient(API_CLIENT_CONF))
        # self.api.put_open_project(open_project=OpenProject(project_name=kwargs["id"]))

    def get_pose(self, end_effector: str) -> Pose:

        try:
            ret: Pose6d = self.api.get_pose(end_effector=end_effector)
        except ApiException as e:
            # TODO how to get PickMasterError here?
            err = json.loads(e.body)
            raise RobotException(err["message"])
        except MaxRetryError:
            raise RobotException("API not available.")

        return Pose(Position(ret.position.x, ret.position.y, ret.position.z),
                    Orientation(ret.rotation.x, ret.rotation.y, ret.rotation.z, ret.rotation.w))

    def focus(self, mfa: MeshFocusAction) -> Pose:

        sw_mfa = MeshFocusActionSw([Vector3(pt.x, pt.y, pt.z) for pt in mfa.mesh_focus_points],
                                   [Vector3(pt.x, pt.y, pt.z) for pt in mfa.robot_space_points])

        try:
            ret: Pose6d = self.api.robot_get_mesh_focus(focus=sw_mfa)
        except ApiException as e:
            # TODO how to get PickMasterError here?
            err = json.loads(e.body)
            raise RobotException(err["message"])
        except MaxRetryError:
            raise RobotException("API not available.")

        return Pose(Position(ret.position.x, ret.position.y, ret.position.z),
                    Orientation(ret.rotation.x, ret.rotation.y, ret.rotation.z, ret.rotation.w))

    @action
    def move_to(self, target: ActionPoint, end_effector: str, speed: int) -> None:

        # TODO action point pose should be relative to its parent object pose - how and where to get the absolute pose?

        ts_start = time.monotonic()

        try:
            self.api.put_move(move=Move(position=Vector3(*target.pose.position),
                                        rotation=Quaternion(*target.pose.orientation),
                                        end_effector=end_effector))
        except ApiException as e:
            # TODO how to get PickMasterError here?
            err = json.loads(e.body)
            raise RobotException(err["message"])
        except MaxRetryError:
            raise RobotException("API not available.")

        ts_end = time.monotonic()
        dur = ts_end - ts_start

        # this is just for testing purposes...
        if dur < 1.0:
            time.sleep(1.0 - dur)

    move_to.__action__ = ActionMetadata(free=True, blocking=True)

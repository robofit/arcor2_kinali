from typing import List

from PIL.Image import Image  # type: ignore

from arcor2 import rest
from arcor2.data.common import ActionMetadata, Pose

from arcor2_kinali.data.search import GripperSetup, SearchEngineParameters, SearchOutput
from arcor2_kinali.object_types.kinali_object import KinaliObject


class Search(KinaliObject):
    """
    REST interface to the search service.
    """

    def grab_image(self) -> None:
        """
        Grabs image and stores to internal cache.
        :return:
        """
        rest.put(f"{self.settings.url}/capture/grab")

    def get_image(self) -> Image:
        """
        Gets RGB image from internal cache, if there is any.
        :return:
        """

        return rest.get_image(f"{self.settings.url}/capture/image")

    def get_pose(self) -> Pose:
        """
        Gets capture device pose in actual initialized spatial system space.
        :return:
        """
        return rest.get(f"{self.settings.url}/capture/pose", Pose)

    def put_suction_configuration(self, item_id: str, tool_id: str, poses: List[Pose]) -> None:
        """
        Adds or updates suction pick configuration.
        :param item_id:
        :param tool_id:
        :param poses:
        :return:
        """
        rest.put(f"{self.settings.url}/pick/suctions", poses, {"item_id": item_id, "tool_id": tool_id})

    def get_pick_poses_for_suction(self, item_id: str, tool_id: str, pose: Pose) -> List[Pose]:
        """
        Gets pick poses for specific suction and item.
        :param item_id:
        :param tool_id:
        :param pose:
        :return:
        """

        return rest.get_list(f"{self.settings.url}/pick/suctions/poses", Pose, pose,
                             params={"item_id": item_id, "tool_id": tool_id})

    def put_gripper_configuration(self, item_id: str, tool_id: str, gripper_setup: List[GripperSetup]) -> None:
        """
        Adds or updates gripper definitions for tool and item.
        :param item_id:
        :param tool_id:
        :param gripper_setup:
        :return:
        """

        rest.put(f"{self.settings.url}/pick/grippers", gripper_setup, {"item_id": item_id, "tool_id": tool_id})

    def get_pick_poses_for_gripper(self, item_id: str, tool_id: str, pose: Pose) -> List[GripperSetup]:
        """
        Gets pick poses for specific tool and item.
        :param item_id:
        :param tool_id:
        :param pose:
        :return:
        """

        return rest.get_list(f"{self.settings.url}/pick/grippers/setup", GripperSetup, pose,
                             {"item_id": item_id, "tool_id": tool_id})

    def search(self) -> SearchOutput:
        """
        Searches items based on search engine configuration and images stored in internal cache.
        :return:
        """
        return rest.get(f"{self.settings.url}/search", SearchOutput)

    def set_search_parameters(self, parameters: SearchEngineParameters) -> None:
        """
        Sets the search parameters.
        :param parameters:
        :return:
        """

        rest.put(f"{self.settings.url}/search", parameters)

    def visualization(self) -> Image:
        """
        Gets RGB visualization from last search run, if there is any.
        :return:
        """

        return rest.get_image(f"{self.settings.url}/search/visualization")

    grab_image.__action__ = ActionMetadata(blocking=True)  # type: ignore
    get_image.__action__ = ActionMetadata(blocking=True)  # type: ignore
    get_pose.__action__ = ActionMetadata(blocking=True)  # type: ignore
    get_pick_poses_for_suction.__action__ = ActionMetadata(blocking=True)  # type: ignore
    search.__action__ = ActionMetadata(blocking=True)  # type: ignore
    visualization.__action__ = ActionMetadata(blocking=True)  # type: ignore

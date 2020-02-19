from typing import Set, List
import os

from PIL.Image import Image  # type: ignore

from arcor2.services import Service
from arcor2.data.common import Pose, ActionMetadata
from arcor2.action import action
from arcor2 import rest

from arcor2_kinali.services import systems
from arcor2_kinali.data.search import SearchOutput

# TODO handle rest exceptions

URL = os.getenv("SEARCH_SERVICE_URL", "http://127.0.0.1:12000")


class SearchService(Service):
    """
    REST interface to the search service.
    """

    def __init__(self, configuration_id: str):

        super(SearchService, self).__init__(configuration_id)
        systems.create(URL, self)

    @staticmethod
    def get_configuration_ids() -> Set[str]:
        return systems.systems(URL)

    @action
    def grab_image(self) -> None:
        """
        Grabs image and stores to internal cache.
        :return:
        """
        rest.put(f"{URL}/capture/grab")

    @action
    def get_image(self) -> Image:
        """
        Gets RGB image from internal cache, if there is any.
        :return:
        """

        return rest.get_image(f"{URL}/capture/image")

    @action
    def get_pose(self) -> Pose:
        """
        Gets capture device pose in actual initialized spatial system space.
        :return:
        """
        return rest.get(f"{URL}/capture/pose", Pose)

    def put_suction_configuration(self, item_id: str, tool_id: str, poses: List[Pose]) -> None:
        """
        Adds or updates suction pick configuration.
        :param item_id:
        :param tool_id:
        :param poses:
        :return:
        """
        rest.put(f"{URL}/pick/suctions", poses, {"item_id": item_id, "tool_id": tool_id})

    @action
    def get_pick_poses_for_suction(self, item_id: str, tool_id: str, pose: Pose) -> List[Pose]:
        """
        Gets pick poses for specific suction and item.
        :param item_id:
        :param tool_id:
        :param pose:
        :return:
        """

        return rest.put_returning_list(f"{URL}/pick/suctions/poses", pose, {"item_id": item_id, "tool_id": tool_id},
                                       data_cls=Pose)

    @action
    def search(self) -> SearchOutput:
        """
        Searches items based on search engine configuration and images stored in internal cache.
        :return:
        """
        return rest.get(f"{URL}/search", SearchOutput)

    @action
    def visualization(self) -> Image:
        """
        Gets RGB visualization from last search run, if there is any.
        :return:
        """

        return rest.get_image(f"{URL}/search/visualization")

    grab_image.__action__ = ActionMetadata(free=True, blocking=True)
    get_image.__action__ = ActionMetadata(free=True, blocking=True)
    get_pose.__action__ = ActionMetadata(free=True, blocking=True)
    get_pick_poses_for_suction.__action__ = ActionMetadata(free=True, blocking=True)
    search.__action__ = ActionMetadata(free=True, blocking=True)
    visualization.__action__ = ActionMetadata(free=True, blocking=True)

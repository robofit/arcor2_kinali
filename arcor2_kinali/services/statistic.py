from typing import FrozenSet, List
import os

from arcor2.services import Service
from arcor2.data.common import ActionMetadata
from arcor2.action import action
from arcor2 import rest

# from arcor2_kinali.services import systems

URL = os.getenv("STATISTIC_SERVICE_URL", "http://127.0.0.1:16000")


class StatisticService(Service):
    """
    Statistic Web API Reference.
    """

    def __init__(self, configuration_id: str):

        super(StatisticService, self).__init__(configuration_id)

    @staticmethod
    def get_configuration_ids() -> FrozenSet[str]:
        return frozenset({"default"})

    @action
    def get_names(self) -> List[str]:
        """
        Gets names of all tracked values.
        :return:
        """
        return rest.get_list_primitive(f"{URL}/values", str)

    @action
    def add_value(self, name: str, value: float) -> None:
        """
        Logs value with the specified name.
        :param name:
        :param value:
        :return:
        """

        rest.put(f"{URL}/values/{name}", params={"value": value})

    @action
    def get_values(self, name: str) -> List[float]:
        """
        Gets tracked values with the specified name. Values are sorted as were added to service.
        :param name:
        :return:
        """

        return rest.get_list_primitive(f"{URL}/values/{name}", float)

    @action
    def clear(self) -> None:
        """
        Deletes all tracked values.
        :return:
        """

        rest.put(f"{URL}/values/clear")

    get_names.__action__ = ActionMetadata(free=True, blocking=True)
    add_value.__action__ = ActionMetadata(free=True, blocking=True)
    get_values.__action__ = ActionMetadata(free=True, blocking=True)
    clear.__action__ = ActionMetadata(free=True, blocking=True)

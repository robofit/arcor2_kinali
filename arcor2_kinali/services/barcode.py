from typing import Set
import os

from arcor2.services import Service
from arcor2.data.common import ActionMetadata
from arcor2.action import action
from arcor2 import rest

from arcor2_kinali.services import systems

# TODO handle rest exceptions

URL = os.getenv("BARCODE_SERVICE_URL", "http://127.0.0.1:12000")


class BarcodeService(Service):
    """
    REST interface to the barcode service.
    """

    def __init__(self, configuration_id: str):

        super(BarcodeService, self).__init__(configuration_id)
        systems.create(URL, self)

    @staticmethod
    def get_configuration_ids() -> Set[str]:
        return systems.systems(URL)

    @action
    def active_scanners(self) -> Set[str]:
        """
        Gets scanners ids.
        :return:
        """
        return set(rest.get_list_primitive(f"{URL}/scanner/ids", str))

    @action
    def scan(self) -> str:
        """
        Gets scan.
        :return:
        """

        return rest.put_returning_primitive(f"{URL}/scanner/scan", str)

    active_scanners.__action__ = ActionMetadata(free=True, blocking=True)
    scan.__action__ = ActionMetadata(free=True, blocking=True)

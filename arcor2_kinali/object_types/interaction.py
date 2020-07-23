from typing import List

from arcor2 import rest
from arcor2.action import action
from arcor2.data.common import ActionMetadata

from arcor2_kinali.data.interaction import DialogValue, NotificationLevelEnum, NotificationValue
from arcor2_kinali.object_types.kinali_object import KinaliObject


class Interaction(KinaliObject):
    """
    REST interface to the barcode service.
    """

    @action
    def add_dialog(self, title: str, content: str, options: List[str]) -> None:
        """
        Logs value with the specified group and name.
        :param title:
        :param content:
        :param options:
        :return:
        """

        rest.put(f"{self.settings.url}/dialog", params={"title": title, "content": content}, data=options)

    @action
    def get_dialog(self) -> DialogValue:
        """
        Gets names of all tracked values stored in given group.
        :return:
        """

        return rest.get(f"{self.settings.url}/dialog", DialogValue)

    @action
    def add_dialog_resolve(self, option: str) -> None:
        """
        Logs value with the specified group and name.
        :param option:
        :return:
        """

        rest.put(f"{self.settings.url}/dialog/resolve", params={"option": option})

    @action
    def add_notification(self, message: str, level: NotificationLevelEnum) -> None:
        """
        Logs value with the specified group and name.
        :param message:
        :param level:
        :return:
        """

        rest.put(f"{self.settings.url}/notification", params={"message": message, "level": level})

    @action
    def delete_notifications(self) -> None:
        """
        Deletes all tracked values stored in given group.
        :return:
        """

        rest.delete(f"{self.settings.url}/notifications")

    @action
    def get_notifications(self, since_imestamp: int) -> List[NotificationValue]:
        """
        Gets names of all tracked values stored in given group.
        :param since_imestamp:
        :return:
        """
        return rest.get_list(f"{self.settings.url}/notifications",
                             NotificationValue, params={"since_imestamp": since_imestamp})

    add_dialog.__action__ = ActionMetadata(blocking=True)  # type: ignore
    get_dialog.__action__ = ActionMetadata(blocking=True)  # type: ignore
    add_dialog_resolve.__action__ = ActionMetadata(blocking=True)  # type: ignore
    add_notification.__action__ = ActionMetadata(blocking=True)  # type: ignore
    delete_notifications.__action__ = ActionMetadata(blocking=True)  # type: ignore
    get_notifications.__action__ = ActionMetadata(blocking=True)  # type: ignore

from typing import Optional, Set

from arcor2 import rest
from arcor2.services import Service


def systems(url: str) -> Set[str]:
    return set(rest.get_data(f"{url}/systems"))


def create(url: str, srv: Service) -> None:
    rest.put(f"{url}/systems/{srv.configuration_id}/create")


def destroy(url: str) -> None:
    rest.put(f"{url}/systems/destroy")


def active(url: str) -> Optional[str]:
    return rest.get_primitive(f"{url}/systems/active", str)

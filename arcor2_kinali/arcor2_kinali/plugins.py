from arcor2.helpers import RpcPlugin
from typing import Dict
from swagger_client import ProjectApi, ApiClient
from arcor2_kinali.conf import API_CLIENT_CONF
from swagger_client.rest import ApiException
from swagger_client import OpenProject


class KinaliRpcPlugin(RpcPlugin):

    def __init__(self):

        self.api = ProjectApi(ApiClient(API_CLIENT_CONF))

    def post_hook(self, req: str, args: Dict, resp: Dict):

        if not resp["result"]:
            return

        if req == "loadProject" and "id" in args:
            print("Opening project {}.".format(args["id"]))
            try:
                self.api.put_open_project(open_project=OpenProject(project_name=args["id"]))
            except ApiException as e:
                print(e)

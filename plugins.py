from arcor2.helpers import RpcPlugin
from typing import Dict
from arcor2_kinali.swagger_client import ApiprojectOpenProjectApi, ApiClient
from arcor2_kinali.conf import API_CLIENT_CONF
from arcor2_kinali.swagger_client.rest import ApiException


class KinaliRpcPlugin(RpcPlugin):

    def __init__(self):

        self.api = ApiprojectOpenProjectApi(ApiClient(API_CLIENT_CONF))

    def post_hook(self, req: str, args: Dict, resp: Dict):

        if not resp["result"]:
            return

        if req == "loadProject" and "_id" in args:
            print("Opening project {}.".format(args["_id"]))
            try:
                self.api.open(project_id=args["_id"])
            except ApiException as e:
                print(e)

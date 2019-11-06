import os
import sys

try:
    KINALI_RESTAPI_ADDRESS = os.environ["ARCOR2_KINALI_RESTAPI_ADDRESS"]
except KeyError:
    sys.exit("'ARCOR2_KINALI_RESTAPI_ADDRESS' env. variable not set.")
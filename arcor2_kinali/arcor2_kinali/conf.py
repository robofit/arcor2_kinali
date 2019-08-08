import swagger_client

try:
    KINALI_RESTAPI_ADDRESS = os.environ["ARCOR2_KINALI_RESTAPI_ADDRESS"]
except KeyError:
    sys.exit("'ARCOR2_KINALI_RESTAPI_ADDRESS' env. variable not set.")

API_CLIENT_CONF = swagger_client.Configuration()
API_CLIENT_CONF.host = KINALI_RESTAPI_ADDRESS

import swagger_client

try:
    KINALI_RESTAPI_ADRESS = os.environ["ARCOR2_KINALI_RESTAPI_ADRESS"]
except KeyError:
    sys.exit("'ARCOR2_KINALI_RESTAPI_ADRESS' env. variable not set.")

API_CLIENT_CONF = swagger_client.Configuration()
API_CLIENT_CONF.host = KINALI_RESTAPI_ADRESS

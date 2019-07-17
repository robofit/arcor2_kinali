from arcor2_kinali import swagger_client

CONF = swagger_client.Configuration()
CONF.host = "http://localhost:5000"

API_CLIENT = swagger_client.ApiClient(CONF)

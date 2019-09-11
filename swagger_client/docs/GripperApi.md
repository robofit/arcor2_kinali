# swagger_client.GripperApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gripper_put_activation**](GripperApi.md#gripper_put_activation) | **PUT** /api/gripper/activate | Activate gripper, need after start gripper.
[**gripper_put_close**](GripperApi.md#gripper_put_close) | **PUT** /api/gripper/close | Close gripper, move to 20 position with 100 force and 30 speed.
[**gripper_put_move**](GripperApi.md#gripper_put_move) | **PUT** /api/gripper/move | Move gripper to position with specific speed and force.
[**gripper_put_open**](GripperApi.md#gripper_put_open) | **PUT** /api/gripper/open | Opens gripper, move to 0 position with 200 force and 200 speed.


# **gripper_put_activation**
> gripper_put_activation()

Activate gripper, need after start gripper.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GripperApi()

try:
    # Activate gripper, need after start gripper.
    api_instance.gripper_put_activation()
except ApiException as e:
    print("Exception when calling GripperApi->gripper_put_activation: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gripper_put_close**
> gripper_put_close()

Close gripper, move to 20 position with 100 force and 30 speed.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GripperApi()

try:
    # Close gripper, move to 20 position with 100 force and 30 speed.
    api_instance.gripper_put_close()
except ApiException as e:
    print("Exception when calling GripperApi->gripper_put_close: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gripper_put_move**
> gripper_put_move(position=position, force=force, speed=speed)

Move gripper to position with specific speed and force.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GripperApi()
position = 56 # int | Position to move gripper 0-255 (optional)
force = 56 # int | Force - allow value 0-255 (optional)
speed = 56 # int | Speed - allow value 0-255 (optional)

try:
    # Move gripper to position with specific speed and force.
    api_instance.gripper_put_move(position=position, force=force, speed=speed)
except ApiException as e:
    print("Exception when calling GripperApi->gripper_put_move: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position** | **int**| Position to move gripper 0-255 | [optional] 
 **force** | **int**| Force - allow value 0-255 | [optional] 
 **speed** | **int**| Speed - allow value 0-255 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gripper_put_open**
> gripper_put_open()

Opens gripper, move to 0 position with 200 force and 200 speed.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GripperApi()

try:
    # Opens gripper, move to 0 position with 200 force and 200 speed.
    api_instance.gripper_put_open()
except ApiException as e:
    print("Exception when calling GripperApi->gripper_put_open: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


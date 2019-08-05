# swagger_client.RobotApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](RobotApi.md#get) | **GET** /api/robot/pose | Gets pose of robot&#39;s end-effector.
[**pose_put**](RobotApi.md#pose_put) | **PUT** /api/robot/pose | Moves robot&#39;s end-effector to specific pose.


# **get**
> Pose6d get(end_effector=end_effector)

Gets pose of robot's end-effector.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()
end_effector = 'end_effector_example' # str | The name of the end-effector. (optional)

try:
    # Gets pose of robot's end-effector.
    api_response = api_instance.get(end_effector=end_effector)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_effector** | **str**| The name of the end-effector. | [optional] 

### Return type

[**Pose6d**](Pose6d.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pose_put**
> pose_put(move=move)

Moves robot's end-effector to specific pose.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()
move = swagger_client.Move() # Move | Move action to process. (optional)

try:
    # Moves robot's end-effector to specific pose.
    api_instance.pose_put(move=move)
except ApiException as e:
    print("Exception when calling RobotApi->pose_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move** | [**Move**](Move.md)| Move action to process. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


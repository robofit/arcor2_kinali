# swagger_client.RobotApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_joints**](RobotApi.md#get_joints) | **GET** /api/robot/joints | Gets actual joints with names to rotation of robot.
[**get_pose**](RobotApi.md#get_pose) | **GET** /api/robot/pose | Gets pose of robot&#39;s end-effector.
[**put_joints**](RobotApi.md#put_joints) | **PUT** /api/robot/joints | Moves robot to specific joints rotation.
[**put_move**](RobotApi.md#put_move) | **PUT** /api/robot/pose | Moves robot&#39;s end-effector to specific pose.


# **get_joints**
> RobotJoints get_joints()

Gets actual joints with names to rotation of robot.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()

try:
    # Gets actual joints with names to rotation of robot.
    api_response = api_instance.get_joints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->get_joints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RobotJoints**](RobotJoints.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pose**
> Pose6d get_pose(end_effector=end_effector)

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
    api_response = api_instance.get_pose(end_effector=end_effector)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->get_pose: %s\n" % e)
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

# **put_joints**
> put_joints(move_joint=move_joint)

Moves robot to specific joints rotation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()
move_joint = swagger_client.RobotJoints() # RobotJoints | Target joints. (optional)

try:
    # Moves robot to specific joints rotation.
    api_instance.put_joints(move_joint=move_joint)
except ApiException as e:
    print("Exception when calling RobotApi->put_joints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_joint** | [**RobotJoints**](RobotJoints.md)| Target joints. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_move**
> put_move(move=move)

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
    api_instance.put_move(move=move)
except ApiException as e:
    print("Exception when calling RobotApi->put_move: %s\n" % e)
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


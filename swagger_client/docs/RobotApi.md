# swagger_client.RobotApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_end_effector_names**](RobotApi.md#get_end_effector_names) | **GET** /api/robot/end-effector | Gets names of end-effectors.
[**get_io**](RobotApi.md#get_io) | **GET** /api/robot/io | Gets robot io pin value.
[**get_joints**](RobotApi.md#get_joints) | **GET** /api/robot/joints | Gets actual joints with names to rotation of robot.
[**get_pose**](RobotApi.md#get_pose) | **GET** /api/robot/pose | Gets pose of robot&#39;s end-effector.
[**put_init_robot**](RobotApi.md#put_init_robot) | **PUT** /api/robot/init | Initialize a robot system.
[**put_joints**](RobotApi.md#put_joints) | **PUT** /api/robot/joints | Moves robot to specific joints rotation.
[**put_move**](RobotApi.md#put_move) | **PUT** /api/robot/pose | Moves robot&#39;s end-effector to specific pose.
[**robot_get_mesh_focus**](RobotApi.md#robot_get_mesh_focus) | **PUT** /api/robot/focus | Focuses mesh pivot to robot space
[**set_io**](RobotApi.md#set_io) | **PUT** /api/robot/io | Sets robot io pin value.


# **get_end_effector_names**
> list[str] get_end_effector_names()

Gets names of end-effectors.

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
    # Gets names of end-effectors.
    api_response = api_instance.get_end_effector_names()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->get_end_effector_names: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_io**
> float get_io(io_pin=io_pin)

Gets robot io pin value.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()
io_pin = 'io_pin_example' # str | Pin of robot to read. (optional)

try:
    # Gets robot io pin value.
    api_response = api_instance.get_io(io_pin=io_pin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->get_io: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **io_pin** | **str**| Pin of robot to read. | [optional] 

### Return type

**float**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **put_init_robot**
> put_init_robot(init_robot=init_robot)

Initialize a robot system.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()
init_robot = swagger_client.InitRobot() # InitRobot | InitRobot action to process. (optional)

try:
    # Initialize a robot system.
    api_instance.put_init_robot(init_robot=init_robot)
except ApiException as e:
    print("Exception when calling RobotApi->put_init_robot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **init_robot** | [**InitRobot**](InitRobot.md)| InitRobot action to process. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_joints**
> put_joints(robot_joints=robot_joints)

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
robot_joints = swagger_client.RobotJoints() # RobotJoints | Target joints. (optional)

try:
    # Moves robot to specific joints rotation.
    api_instance.put_joints(robot_joints=robot_joints)
except ApiException as e:
    print("Exception when calling RobotApi->put_joints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **robot_joints** | [**RobotJoints**](RobotJoints.md)| Target joints. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

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
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **robot_get_mesh_focus**
> Pose6d robot_get_mesh_focus(focus=focus)

Focuses mesh pivot to robot space

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()
focus = swagger_client.MeshFocusAction() # MeshFocusAction | Point clouds for focusing mesh position in robot space (optional)

try:
    # Focuses mesh pivot to robot space
    api_response = api_instance.robot_get_mesh_focus(focus=focus)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->robot_get_mesh_focus: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **focus** | [**MeshFocusAction**](MeshFocusAction.md)| Point clouds for focusing mesh position in robot space | [optional] 

### Return type

[**Pose6d**](Pose6d.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_io**
> set_io(io=io)

Sets robot io pin value.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()
io = swagger_client.IoAction() # IoAction | Io parameters to set. (optional)

try:
    # Sets robot io pin value.
    api_instance.set_io(io=io)
except ApiException as e:
    print("Exception when calling RobotApi->set_io: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **io** | [**IoAction**](IoAction.md)| Io parameters to set. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


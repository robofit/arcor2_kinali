# swagger_client.SimaticApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_actual_position**](SimaticApi.md#get_actual_position) | **GET** /api/simatic/position | Gets actual position of simatic engine.
[**get_io**](SimaticApi.md#get_io) | **GET** /api/simatic/io | Gets analog/digital input/output value.
[**move_home**](SimaticApi.md#move_home) | **PUT** /api/simatic/move_home | Move engine to home position, need after start simatic.
[**move_to_position**](SimaticApi.md#move_to_position) | **PUT** /api/simatic/position | Move engine to absolute or relative position with specific speed.
[**set_io**](SimaticApi.md#set_io) | **PUT** /api/simatic/io | Sets analog/digital output value.
[**stop_machine**](SimaticApi.md#stop_machine) | **PUT** /api/simatic/stop_machine | Stop engine.


# **get_actual_position**
> int get_actual_position(engine_number)

Gets actual position of simatic engine.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SimaticApi()
engine_number = 56 # int | Number of simatic engine

try:
    # Gets actual position of simatic engine.
    api_response = api_instance.get_actual_position(engine_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimaticApi->get_actual_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_number** | **int**| Number of simatic engine | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_io**
> float get_io(name)

Gets analog/digital input/output value.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SimaticApi()
name = 'name_example' # str | Name of IO with format {A/D}{I/O}_{byte number}

try:
    # Gets analog/digital input/output value.
    api_response = api_instance.get_io(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimaticApi->get_io: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of IO with format {A/D}{I/O}_{byte number} | 

### Return type

**float**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_home**
> move_home(engine)

Move engine to home position, need after start simatic.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SimaticApi()
engine = 56 # int | Number of engine

try:
    # Move engine to home position, need after start simatic.
    api_instance.move_home(engine)
except ApiException as e:
    print("Exception when calling SimaticApi->move_home: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine** | **int**| Number of engine | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_to_position**
> move_to_position(engine, position, speed, position_type)

Move engine to absolute or relative position with specific speed.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SimaticApi()
engine = 56 # int | Number of engine
position = 56 # int | Position in micrometre
speed = 56 # int | Speed in mm/s
position_type = 'position_type_example' # str | Absolute or relative

try:
    # Move engine to absolute or relative position with specific speed.
    api_instance.move_to_position(engine, position, speed, position_type)
except ApiException as e:
    print("Exception when calling SimaticApi->move_to_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine** | **int**| Number of engine | 
 **position** | **int**| Position in micrometre | 
 **speed** | **int**| Speed in mm/s | 
 **position_type** | **str**| Absolute or relative | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_io**
> set_io(name, output=output)

Sets analog/digital output value.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SimaticApi()
name = 'name_example' # str | Name of IO with format {A/D}{I/O}_{byte number}
output = 1.2 # float | Value set to IO (optional)

try:
    # Sets analog/digital output value.
    api_instance.set_io(name, output=output)
except ApiException as e:
    print("Exception when calling SimaticApi->set_io: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of IO with format {A/D}{I/O}_{byte number} | 
 **output** | **float**| Value set to IO | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_machine**
> stop_machine(number)

Stop engine.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SimaticApi()
number = 56 # int | Number of engine

try:
    # Stop engine.
    api_instance.stop_machine(number)
except ApiException as e:
    print("Exception when calling SimaticApi->stop_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **int**| Number of engine | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


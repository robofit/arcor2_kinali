# swagger_client.ScriptingApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scripting_run_script_from_file**](ScriptingApi.md#scripting_run_script_from_file) | **PUT** /api/scripting/run | Posts file script and execute.
[**scripting_stop**](ScriptingApi.md#scripting_stop) | **PUT** /api/scripting/stop | Stop running script.


# **scripting_run_script_from_file**
> scripting_run_script_from_file(file)

Posts file script and execute.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScriptingApi()
file = '/path/to/file.txt' # file | File with script.

try:
    # Posts file script and execute.
    api_instance.scripting_run_script_from_file(file)
except ApiException as e:
    print("Exception when calling ScriptingApi->scripting_run_script_from_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| File with script. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scripting_stop**
> scripting_stop()

Stop running script.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScriptingApi()

try:
    # Stop running script.
    api_instance.scripting_stop()
except ApiException as e:
    print("Exception when calling ScriptingApi->scripting_stop: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


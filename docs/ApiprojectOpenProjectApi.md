# swagger_client.ApiprojectOpenProjectApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**open**](ApiprojectOpenProjectApi.md#open) | **PUT** /api/project/OpenProject | Opens project in Pick Master.


# **open**
> open(project_id=project_id)

Opens project in Pick Master.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiprojectOpenProjectApi()
project_id = 'project_id_example' # str | The unique identification of the project. (optional)

try:
    # Opens project in Pick Master.
    api_instance.open(project_id=project_id)
except ApiException as e:
    print("Exception when calling ApiprojectOpenProjectApi->open: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identification of the project. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


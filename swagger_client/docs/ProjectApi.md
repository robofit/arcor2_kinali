# swagger_client.ProjectApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**put**](ProjectApi.md#put) | **PUT** /api/project/open | Opens the project in Pick Master.


# **put**
> put(open_project=open_project)

Opens the project in Pick Master.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
open_project = swagger_client.OpenProject() # OpenProject | The project to open. (optional)

try:
    # Opens the project in Pick Master.
    api_instance.put(open_project=open_project)
except ApiException as e:
    print("Exception when calling ProjectApi->put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_project** | [**OpenProject**](OpenProject.md)| The project to open. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


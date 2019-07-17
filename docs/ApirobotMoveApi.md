# swagger_client.ApirobotMoveApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**put**](ApirobotMoveApi.md#put) | **PUT** /api/robot/Move | Moves robot endpoint to specific point with specific orientation.


# **put**
> put(move=move)

Moves robot endpoint to specific point with specific orientation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApirobotMoveApi()
move = swagger_client.Move() # Move | Move action to process. (optional)

try:
    # Moves robot endpoint to specific point with specific orientation.
    api_instance.put(move=move)
except ApiException as e:
    print("Exception when calling ApirobotMoveApi->put: %s\n" % e)
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


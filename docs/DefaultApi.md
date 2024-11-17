# pyticktick.openapi_client.DefaultApi

All URIs are relative to *https://api.ticktick.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_token_post**](DefaultApi.md#oauth_token_post) | **POST** /oauth/token | Get token
[**open_v1_project_get**](DefaultApi.md#open_v1_project_get) | **GET** /open/v1/project | Get User Project.
[**open_v1_project_post**](DefaultApi.md#open_v1_project_post) | **POST** /open/v1/project | Create Project
[**open_v1_project_project_id_data_get**](DefaultApi.md#open_v1_project_project_id_data_get) | **GET** /open/v1/project/{projectId}/data | 
[**open_v1_project_project_id_delete**](DefaultApi.md#open_v1_project_project_id_delete) | **DELETE** /open/v1/project/{projectId} | 
[**open_v1_project_project_id_get**](DefaultApi.md#open_v1_project_project_id_get) | **GET** /open/v1/project/{projectId} | 
[**open_v1_project_project_id_post**](DefaultApi.md#open_v1_project_project_id_post) | **POST** /open/v1/project/{projectId} | Update Project
[**open_v1_project_project_id_task_task_id_complete_post**](DefaultApi.md#open_v1_project_project_id_task_task_id_complete_post) | **POST** /open/v1/project/{projectId}/task/{taskId}/complete | Update Task
[**open_v1_project_project_id_task_task_id_delete**](DefaultApi.md#open_v1_project_project_id_task_task_id_delete) | **DELETE** /open/v1/project/{projectId}/task/{taskId} | Delete task.
[**open_v1_project_project_id_task_task_id_get**](DefaultApi.md#open_v1_project_project_id_task_task_id_get) | **GET** /open/v1/project/{projectId}/task/{taskId} | Get Task By Project ID And Task ID.
[**open_v1_task_post**](DefaultApi.md#open_v1_task_post) | **POST** /open/v1/task | Create Task
[**open_v1_task_task_id_post**](DefaultApi.md#open_v1_task_task_id_post) | **POST** /open/v1/task/{taskId} | Update Task


# **oauth_token_post**
> OauthTokenPost200Response oauth_token_post(oauth_token_post_request=oauth_token_post_request)

Get token

client_id and :client_secret are passes to basic auth as username and password

### Example

* Basic Authentication (BasicAuth):
```python
import time
import os
import pyticktick.openapi_client
from pyticktick.openapi_client.models.oauth_token_post200_response import OauthTokenPost200Response
from pyticktick.openapi_client.models.oauth_token_post_request import OauthTokenPostRequest
from pyticktick.openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ticktick.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pyticktick.openapi_client.Configuration(
    host = "https://api.ticktick.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pyticktick.openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
async with pyticktick.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyticktick.openapi_client.DefaultApi(api_client)
    oauth_token_post_request = pyticktick.openapi_client.OauthTokenPostRequest() # OauthTokenPostRequest |  (optional)

    try:
        # Get token
        api_response = await api_instance.oauth_token_post(oauth_token_post_request=oauth_token_post_request)
        print("The response of DefaultApi->oauth_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->oauth_token_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oauth_token_post_request** | [**OauthTokenPostRequest**](OauthTokenPostRequest.md)|  | [optional] 

### Return type

[**OauthTokenPost200Response**](OauthTokenPost200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_v1_project_get**
> List[Project] open_v1_project_get()

Get User Project.

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import pyticktick.openapi_client
from pyticktick.openapi_client.models.project import Project
from pyticktick.openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ticktick.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pyticktick.openapi_client.Configuration(
    host = "https://api.ticktick.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: BearerAuth
configuration = pyticktick.openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with pyticktick.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyticktick.openapi_client.DefaultApi(api_client)

    try:
        # Get User Project.
        api_response = await api_instance.open_v1_project_get()
        print("The response of DefaultApi->open_v1_project_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->open_v1_project_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[Project]**](Project.md)

### Authorization

[OAuth2](../README.md#OAuth2), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_v1_project_post**
> Project open_v1_project_post(project)

Create Project

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import pyticktick.openapi_client
from pyticktick.openapi_client.models.project import Project
from pyticktick.openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ticktick.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pyticktick.openapi_client.Configuration(
    host = "https://api.ticktick.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: BearerAuth
configuration = pyticktick.openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with pyticktick.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyticktick.openapi_client.DefaultApi(api_client)
    project = pyticktick.openapi_client.Project() # Project | 

    try:
        # Create Project
        api_response = await api_instance.open_v1_project_post(project)
        print("The response of DefaultApi->open_v1_project_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->open_v1_project_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**Project**](Project.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

[OAuth2](../README.md#OAuth2), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_v1_project_project_id_data_get**
> ProjectData open_v1_project_project_id_data_get(project_id)



### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import pyticktick.openapi_client
from pyticktick.openapi_client.models.project_data import ProjectData
from pyticktick.openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ticktick.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pyticktick.openapi_client.Configuration(
    host = "https://api.ticktick.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: BearerAuth
configuration = pyticktick.openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with pyticktick.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyticktick.openapi_client.DefaultApi(api_client)
    project_id = 'project_id_example' # str | Project identifier

    try:
        api_response = await api_instance.open_v1_project_project_id_data_get(project_id)
        print("The response of DefaultApi->open_v1_project_project_id_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->open_v1_project_project_id_data_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project identifier | 

### Return type

[**ProjectData**](ProjectData.md)

### Authorization

[OAuth2](../README.md#OAuth2), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_v1_project_project_id_delete**
> open_v1_project_project_id_delete(project_id)



### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import pyticktick.openapi_client
from pyticktick.openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ticktick.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pyticktick.openapi_client.Configuration(
    host = "https://api.ticktick.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: BearerAuth
configuration = pyticktick.openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with pyticktick.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyticktick.openapi_client.DefaultApi(api_client)
    project_id = 'project_id_example' # str | Project identifier

    try:
        await api_instance.open_v1_project_project_id_delete(project_id)
    except Exception as e:
        print("Exception when calling DefaultApi->open_v1_project_project_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project identifier | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_v1_project_project_id_get**
> Project open_v1_project_project_id_get(project_id)



### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import pyticktick.openapi_client
from pyticktick.openapi_client.models.project import Project
from pyticktick.openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ticktick.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pyticktick.openapi_client.Configuration(
    host = "https://api.ticktick.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: BearerAuth
configuration = pyticktick.openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with pyticktick.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyticktick.openapi_client.DefaultApi(api_client)
    project_id = 'project_id_example' # str | Project identifier

    try:
        api_response = await api_instance.open_v1_project_project_id_get(project_id)
        print("The response of DefaultApi->open_v1_project_project_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->open_v1_project_project_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project identifier | 

### Return type

[**Project**](Project.md)

### Authorization

[OAuth2](../README.md#OAuth2), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_v1_project_project_id_post**
> Project open_v1_project_project_id_post(project_id, open_v1_project_project_id_post_request)

Update Project

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import pyticktick.openapi_client
from pyticktick.openapi_client.models.open_v1_project_project_id_post_request import OpenV1ProjectProjectIdPostRequest
from pyticktick.openapi_client.models.project import Project
from pyticktick.openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ticktick.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pyticktick.openapi_client.Configuration(
    host = "https://api.ticktick.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: BearerAuth
configuration = pyticktick.openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with pyticktick.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyticktick.openapi_client.DefaultApi(api_client)
    project_id = 'project_id_example' # str | Project identifier
    open_v1_project_project_id_post_request = pyticktick.openapi_client.OpenV1ProjectProjectIdPostRequest() # OpenV1ProjectProjectIdPostRequest | 

    try:
        # Update Project
        api_response = await api_instance.open_v1_project_project_id_post(project_id, open_v1_project_project_id_post_request)
        print("The response of DefaultApi->open_v1_project_project_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->open_v1_project_project_id_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project identifier | 
 **open_v1_project_project_id_post_request** | [**OpenV1ProjectProjectIdPostRequest**](OpenV1ProjectProjectIdPostRequest.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

[OAuth2](../README.md#OAuth2), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_v1_project_project_id_task_task_id_complete_post**
> open_v1_project_project_id_task_task_id_complete_post(project_id, task_id, open_v1_project_project_id_task_task_id_complete_post_request)

Update Task

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import pyticktick.openapi_client
from pyticktick.openapi_client.models.open_v1_project_project_id_task_task_id_complete_post_request import OpenV1ProjectProjectIdTaskTaskIdCompletePostRequest
from pyticktick.openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ticktick.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pyticktick.openapi_client.Configuration(
    host = "https://api.ticktick.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: BearerAuth
configuration = pyticktick.openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with pyticktick.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyticktick.openapi_client.DefaultApi(api_client)
    project_id = 'project_id_example' # str | Project identifier
    task_id = 'task_id_example' # str | Task identifier
    open_v1_project_project_id_task_task_id_complete_post_request = pyticktick.openapi_client.OpenV1ProjectProjectIdTaskTaskIdCompletePostRequest() # OpenV1ProjectProjectIdTaskTaskIdCompletePostRequest | 

    try:
        # Update Task
        await api_instance.open_v1_project_project_id_task_task_id_complete_post(project_id, task_id, open_v1_project_project_id_task_task_id_complete_post_request)
    except Exception as e:
        print("Exception when calling DefaultApi->open_v1_project_project_id_task_task_id_complete_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project identifier | 
 **task_id** | **str**| Task identifier | 
 **open_v1_project_project_id_task_task_id_complete_post_request** | [**OpenV1ProjectProjectIdTaskTaskIdCompletePostRequest**](OpenV1ProjectProjectIdTaskTaskIdCompletePostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_v1_project_project_id_task_task_id_delete**
> open_v1_project_project_id_task_task_id_delete(project_id, task_id)

Delete task.

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import pyticktick.openapi_client
from pyticktick.openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ticktick.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pyticktick.openapi_client.Configuration(
    host = "https://api.ticktick.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: BearerAuth
configuration = pyticktick.openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with pyticktick.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyticktick.openapi_client.DefaultApi(api_client)
    project_id = 'project_id_example' # str | Project identifier
    task_id = 'task_id_example' # str | Task identifier

    try:
        # Delete task.
        await api_instance.open_v1_project_project_id_task_task_id_delete(project_id, task_id)
    except Exception as e:
        print("Exception when calling DefaultApi->open_v1_project_project_id_task_task_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project identifier | 
 **task_id** | **str**| Task identifier | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_v1_project_project_id_task_task_id_get**
> Task open_v1_project_project_id_task_task_id_get(project_id, task_id)

Get Task By Project ID And Task ID.

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import pyticktick.openapi_client
from pyticktick.openapi_client.models.task import Task
from pyticktick.openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ticktick.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pyticktick.openapi_client.Configuration(
    host = "https://api.ticktick.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: BearerAuth
configuration = pyticktick.openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with pyticktick.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyticktick.openapi_client.DefaultApi(api_client)
    project_id = 'project_id_example' # str | Project identifier
    task_id = 'task_id_example' # str | Task identifier

    try:
        # Get Task By Project ID And Task ID.
        api_response = await api_instance.open_v1_project_project_id_task_task_id_get(project_id, task_id)
        print("The response of DefaultApi->open_v1_project_project_id_task_task_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->open_v1_project_project_id_task_task_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project identifier | 
 **task_id** | **str**| Task identifier | 

### Return type

[**Task**](Task.md)

### Authorization

[OAuth2](../README.md#OAuth2), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_v1_task_post**
> Task open_v1_task_post(task)

Create Task

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import pyticktick.openapi_client
from pyticktick.openapi_client.models.task import Task
from pyticktick.openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ticktick.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pyticktick.openapi_client.Configuration(
    host = "https://api.ticktick.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: BearerAuth
configuration = pyticktick.openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with pyticktick.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyticktick.openapi_client.DefaultApi(api_client)
    task = pyticktick.openapi_client.Task() # Task | 

    try:
        # Create Task
        api_response = await api_instance.open_v1_task_post(task)
        print("The response of DefaultApi->open_v1_task_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->open_v1_task_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task** | [**Task**](Task.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[OAuth2](../README.md#OAuth2), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_v1_task_task_id_post**
> Task open_v1_task_task_id_post(task_id, open_v1_task_task_id_post_request)

Update Task

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import pyticktick.openapi_client
from pyticktick.openapi_client.models.open_v1_task_task_id_post_request import OpenV1TaskTaskIdPostRequest
from pyticktick.openapi_client.models.task import Task
from pyticktick.openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ticktick.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pyticktick.openapi_client.Configuration(
    host = "https://api.ticktick.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: BearerAuth
configuration = pyticktick.openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with pyticktick.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyticktick.openapi_client.DefaultApi(api_client)
    task_id = 'task_id_example' # str | Task identifier
    open_v1_task_task_id_post_request = pyticktick.openapi_client.OpenV1TaskTaskIdPostRequest() # OpenV1TaskTaskIdPostRequest | 

    try:
        # Update Task
        api_response = await api_instance.open_v1_task_task_id_post(task_id, open_v1_task_task_id_post_request)
        print("The response of DefaultApi->open_v1_task_task_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->open_v1_task_task_id_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Task identifier | 
 **open_v1_task_task_id_post_request** | [**OpenV1TaskTaskIdPostRequest**](OpenV1TaskTaskIdPostRequest.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[OAuth2](../README.md#OAuth2), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


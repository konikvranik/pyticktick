# OpenV1TaskTaskIdPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Task identifier | [optional] 
**task_id** | **str** | Task identifier | [optional] 
**project_id** | **str** | Task project id | [optional] 
**title** | **str** | Task title | [optional] 
**completed_time** | **datetime** | Task completed time in \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ssZ\&quot; | [optional] 
**status** | [**Status**](Status.md) |  | [optional] 
**is_all_day** | **bool** | All day | [optional] 
**content** | **str** | Task content | [optional] 
**desc** | **str** | Task description of checklist | [optional] 
**due_date** | **datetime** | Task due date time in \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ssZ\&quot; | [optional] 
**items** | [**List[ChecklistItem]**](ChecklistItem.md) | Subtasks of Task | [optional] 
**priority** | **int** | Task priority | [optional] 
**reminders** | **List[str]** | List of reminder triggers | [optional] 
**repeat_flag** | **str** | Recurring rules of task | [optional] 
**sort_order** | **int** | Task sort order | [optional] 
**start_date** | **datetime** | Start date time in \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ssZ\&quot; | [optional] 
**time_zone** | **object** |  | [optional] 

## Example

```python
from pyticktick.openapi_client.models.open_v1_task_task_id_post_request import OpenV1TaskTaskIdPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OpenV1TaskTaskIdPostRequest from a JSON string
open_v1_task_task_id_post_request_instance = OpenV1TaskTaskIdPostRequest.from_json(json)
# print the JSON string representation of the object
print OpenV1TaskTaskIdPostRequest.to_json()

# convert the object into a dict
open_v1_task_task_id_post_request_dict = open_v1_task_task_id_post_request_instance.to_dict()
# create an instance of OpenV1TaskTaskIdPostRequest from a dict
open_v1_task_task_id_post_request_from_dict = OpenV1TaskTaskIdPostRequest.from_dict(open_v1_task_task_id_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



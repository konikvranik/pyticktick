# ProjectData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | [**Project**](Project.md) |  | [optional] 
**tasks** | [**List[Task]**](Task.md) |  | [optional] 
**columns** | [**List[Column]**](Column.md) |  | [optional] 

## Example

```python
from pyticktick.openapi_client.models.project_data import ProjectData

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectData from a JSON string
project_data_instance = ProjectData.from_json(json)
# print the JSON string representation of the object
print ProjectData.to_json()

# convert the object into a dict
project_data_dict = project_data_instance.to_dict()
# create an instance of ProjectData from a dict
project_data_from_dict = ProjectData.from_dict(project_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


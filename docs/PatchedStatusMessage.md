# PatchedStatusMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**title** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**state** | [**StateA07Enum**](StateA07Enum.md) |  | [optional] 
**categories** | **List[int]** |  | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from signals_api_client.models.patched_status_message import PatchedStatusMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedStatusMessage from a JSON string
patched_status_message_instance = PatchedStatusMessage.from_json(json)
# print the JSON string representation of the object
print(PatchedStatusMessage.to_json())

# convert the object into a dict
patched_status_message_dict = patched_status_message_instance.to_dict()
# create an instance of PatchedStatusMessage from a dict
patched_status_message_from_dict = PatchedStatusMessage.from_dict(patched_status_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



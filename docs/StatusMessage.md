# StatusMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**title** | **str** |  | 
**text** | **str** |  | 
**active** | **bool** |  | [optional] 
**state** | [**StateA07Enum**](StateA07Enum.md) |  | 
**categories** | **List[int]** |  | [optional] 
**updated_at** | **datetime** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 

## Example

```python
from signals_api_client.models.status_message import StatusMessage

# TODO update the JSON string below
json = "{}"
# create an instance of StatusMessage from a JSON string
status_message_instance = StatusMessage.from_json(json)
# print the JSON string representation of the object
print(StatusMessage.to_json())

# convert the object into a dict
status_message_dict = status_message_instance.to_dict()
# create an instance of StatusMessage from a dict
status_message_from_dict = StatusMessage.from_dict(status_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SignalList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links9**](Links9.md) |  | 
**display** | **str** |  | [readonly] 
**uuid** | **str** |  | [readonly] 
**id_display** | **str** |  | [readonly] 
**text** | **str** |  | [readonly] 
**status** | [**NestedMySignalStatus**](NestedMySignalStatus.md) |  | 
**created_at** | **datetime** |  | [readonly] 

## Example

```python
from signals_api_client.models.signal_list import SignalList

# TODO update the JSON string below
json = "{}"
# create an instance of SignalList from a JSON string
signal_list_instance = SignalList.from_json(json)
# print the JSON string representation of the object
print(SignalList.to_json())

# convert the object into a dict
signal_list_dict = signal_list_instance.to_dict()
# create an instance of SignalList from a dict
signal_list_from_dict = SignalList.from_dict(signal_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



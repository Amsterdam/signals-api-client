# NestedMySignalStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | [readonly] 
**state_display** | **str** |  | [readonly] 

## Example

```python
from signals_api_client.models.nested_my_signal_status import NestedMySignalStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NestedMySignalStatus from a JSON string
nested_my_signal_status_instance = NestedMySignalStatus.from_json(json)
# print the JSON string representation of the object
print(NestedMySignalStatus.to_json())

# convert the object into a dict
nested_my_signal_status_dict = nested_my_signal_status_instance.to_dict()
# create an instance of NestedMySignalStatus from a dict
nested_my_signal_status_from_dict = NestedMySignalStatus.from_dict(nested_my_signal_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



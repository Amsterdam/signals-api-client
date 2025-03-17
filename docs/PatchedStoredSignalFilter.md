# PatchedStoredSignalFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **str** |  | [optional] [readonly] 
**display** | **str** |  | [optional] [readonly] 
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**options** | **object** |  | [optional] 
**refresh** | **bool** |  | [optional] 
**show_on_overview** | **bool** |  | [optional] 

## Example

```python
from signals_api_client.models.patched_stored_signal_filter import PatchedStoredSignalFilter

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedStoredSignalFilter from a JSON string
patched_stored_signal_filter_instance = PatchedStoredSignalFilter.from_json(json)
# print the JSON string representation of the object
print(PatchedStoredSignalFilter.to_json())

# convert the object into a dict
patched_stored_signal_filter_dict = patched_stored_signal_filter_instance.to_dict()
# create an instance of PatchedStoredSignalFilter from a dict
patched_stored_signal_filter_from_dict = PatchedStoredSignalFilter.from_dict(patched_stored_signal_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



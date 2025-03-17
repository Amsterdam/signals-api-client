# StoredSignalFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **str** |  | [readonly] 
**display** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**created_at** | **datetime** |  | [readonly] 
**options** | **object** |  | [optional] 
**refresh** | **bool** |  | [optional] 
**show_on_overview** | **bool** |  | [optional] 

## Example

```python
from signals_api_client.models.stored_signal_filter import StoredSignalFilter

# TODO update the JSON string below
json = "{}"
# create an instance of StoredSignalFilter from a JSON string
stored_signal_filter_instance = StoredSignalFilter.from_json(json)
# print the JSON string representation of the object
print(StoredSignalFilter.to_json())

# convert the object into a dict
stored_signal_filter_dict = stored_signal_filter_instance.to_dict()
# create an instance of StoredSignalFilter from a dict
stored_signal_filter_from_dict = StoredSignalFilter.from_dict(stored_signal_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



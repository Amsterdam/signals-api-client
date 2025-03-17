# PaginatedAbridgedChildSignalList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedAbridgedChildSignalListLinks**](PaginatedAbridgedChildSignalListLinks.md) |  | [optional] 
**count** | **int** |  | [optional] 
**results** | [**List[AbridgedChildSignal]**](AbridgedChildSignal.md) |  | [optional] 

## Example

```python
from signals_api_client.models.paginated_abridged_child_signal_list import PaginatedAbridgedChildSignalList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAbridgedChildSignalList from a JSON string
paginated_abridged_child_signal_list_instance = PaginatedAbridgedChildSignalList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAbridgedChildSignalList.to_json())

# convert the object into a dict
paginated_abridged_child_signal_list_dict = paginated_abridged_child_signal_list_instance.to_dict()
# create an instance of PaginatedAbridgedChildSignalList from a dict
paginated_abridged_child_signal_list_from_dict = PaginatedAbridgedChildSignalList.from_dict(paginated_abridged_child_signal_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



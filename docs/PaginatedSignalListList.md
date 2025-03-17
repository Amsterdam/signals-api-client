# PaginatedSignalListList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedAbridgedChildSignalListLinks**](PaginatedAbridgedChildSignalListLinks.md) |  | [optional] 
**count** | **int** |  | [optional] 
**results** | [**List[SignalList]**](SignalList.md) |  | [optional] 

## Example

```python
from signals_api_client.models.paginated_signal_list_list import PaginatedSignalListList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSignalListList from a JSON string
paginated_signal_list_list_instance = PaginatedSignalListList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSignalListList.to_json())

# convert the object into a dict
paginated_signal_list_list_dict = paginated_signal_list_list_instance.to_dict()
# create an instance of PaginatedSignalListList from a dict
paginated_signal_list_list_from_dict = PaginatedSignalListList.from_dict(paginated_signal_list_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



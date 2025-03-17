# PaginatedStoredSignalFilterList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[StoredSignalFilter]**](StoredSignalFilter.md) |  | 

## Example

```python
from signals_api_client.models.paginated_stored_signal_filter_list import PaginatedStoredSignalFilterList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedStoredSignalFilterList from a JSON string
paginated_stored_signal_filter_list_instance = PaginatedStoredSignalFilterList.from_json(json)
# print the JSON string representation of the object
print(PaginatedStoredSignalFilterList.to_json())

# convert the object into a dict
paginated_stored_signal_filter_list_dict = paginated_stored_signal_filter_list_instance.to_dict()
# create an instance of PaginatedStoredSignalFilterList from a dict
paginated_stored_signal_filter_list_from_dict = PaginatedStoredSignalFilterList.from_dict(paginated_stored_signal_filter_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PaginatedSignalIdListList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedAbridgedChildSignalListLinks**](PaginatedAbridgedChildSignalListLinks.md) |  | [optional] 
**count** | **int** |  | [optional] 
**results** | [**List[SignalIdList]**](SignalIdList.md) |  | [optional] 

## Example

```python
from signals_api_client.models.paginated_signal_id_list_list import PaginatedSignalIdListList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSignalIdListList from a JSON string
paginated_signal_id_list_list_instance = PaginatedSignalIdListList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSignalIdListList.to_json())

# convert the object into a dict
paginated_signal_id_list_list_dict = paginated_signal_id_list_list_instance.to_dict()
# create an instance of PaginatedSignalIdListList from a dict
paginated_signal_id_list_list_from_dict = PaginatedSignalIdListList.from_dict(paginated_signal_id_list_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



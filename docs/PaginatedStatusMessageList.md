# PaginatedStatusMessageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedAbridgedChildSignalListLinks**](PaginatedAbridgedChildSignalListLinks.md) |  | [optional] 
**count** | **int** |  | [optional] 
**results** | [**List[StatusMessage]**](StatusMessage.md) |  | [optional] 

## Example

```python
from signals_api_client.models.paginated_status_message_list import PaginatedStatusMessageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedStatusMessageList from a JSON string
paginated_status_message_list_instance = PaginatedStatusMessageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedStatusMessageList.to_json())

# convert the object into a dict
paginated_status_message_list_dict = paginated_status_message_list_instance.to_dict()
# create an instance of PaginatedStatusMessageList from a dict
paginated_status_message_list_from_dict = PaginatedStatusMessageList.from_dict(paginated_status_message_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



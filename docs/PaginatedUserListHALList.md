# PaginatedUserListHALList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedAbridgedChildSignalListLinks**](PaginatedAbridgedChildSignalListLinks.md) |  | [optional] 
**count** | **int** |  | [optional] 
**results** | [**List[UserListHAL]**](UserListHAL.md) |  | [optional] 

## Example

```python
from signals_api_client.models.paginated_user_list_hal_list import PaginatedUserListHALList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUserListHALList from a JSON string
paginated_user_list_hal_list_instance = PaginatedUserListHALList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUserListHALList.to_json())

# convert the object into a dict
paginated_user_list_hal_list_dict = paginated_user_list_hal_list_instance.to_dict()
# create an instance of PaginatedUserListHALList from a dict
paginated_user_list_hal_list_from_dict = PaginatedUserListHALList.from_dict(paginated_user_list_hal_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



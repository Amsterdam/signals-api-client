# PaginatedUserNameListList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedAbridgedChildSignalListLinks**](PaginatedAbridgedChildSignalListLinks.md) |  | [optional] 
**count** | **int** |  | [optional] 
**results** | [**List[UserNameList]**](UserNameList.md) |  | [optional] 

## Example

```python
from signals_api_client.models.paginated_user_name_list_list import PaginatedUserNameListList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUserNameListList from a JSON string
paginated_user_name_list_list_instance = PaginatedUserNameListList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUserNameListList.to_json())

# convert the object into a dict
paginated_user_name_list_list_dict = paginated_user_name_list_list_instance.to_dict()
# create an instance of PaginatedUserNameListList from a dict
paginated_user_name_list_list_from_dict = PaginatedUserNameListList.from_dict(paginated_user_name_list_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



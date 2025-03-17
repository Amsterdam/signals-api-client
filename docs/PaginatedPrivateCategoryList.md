# PaginatedPrivateCategoryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedAbridgedChildSignalListLinks**](PaginatedAbridgedChildSignalListLinks.md) |  | [optional] 
**count** | **int** |  | [optional] 
**results** | [**List[PrivateCategory]**](PrivateCategory.md) |  | [optional] 

## Example

```python
from signals_api_client.models.paginated_private_category_list import PaginatedPrivateCategoryList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPrivateCategoryList from a JSON string
paginated_private_category_list_instance = PaginatedPrivateCategoryList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPrivateCategoryList.to_json())

# convert the object into a dict
paginated_private_category_list_dict = paginated_private_category_list_instance.to_dict()
# create an instance of PaginatedPrivateCategoryList from a dict
paginated_private_category_list_from_dict = PaginatedPrivateCategoryList.from_dict(paginated_private_category_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



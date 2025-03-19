# PaginatedAreaTypeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedAbridgedChildSignalListLinks**](PaginatedAbridgedChildSignalListLinks.md) |  | [optional] 
**count** | **int** |  | [optional] 
**results** | [**List[AreaType]**](AreaType.md) |  | [optional] 

## Example

```python
from signals_api_client.models.paginated_area_type_list import PaginatedAreaTypeList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAreaTypeList from a JSON string
paginated_area_type_list_instance = PaginatedAreaTypeList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAreaTypeList.to_json())

# convert the object into a dict
paginated_area_type_list_dict = paginated_area_type_list_instance.to_dict()
# create an instance of PaginatedAreaTypeList from a dict
paginated_area_type_list_from_dict = PaginatedAreaTypeList.from_dict(paginated_area_type_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



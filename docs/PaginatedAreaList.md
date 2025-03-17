# PaginatedAreaList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedAbridgedChildSignalListLinks**](PaginatedAbridgedChildSignalListLinks.md) |  | [optional] 
**count** | **int** |  | [optional] 
**results** | [**List[Area]**](Area.md) |  | [optional] 

## Example

```python
from signals_api_client.models.paginated_area_list import PaginatedAreaList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAreaList from a JSON string
paginated_area_list_instance = PaginatedAreaList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAreaList.to_json())

# convert the object into a dict
paginated_area_list_dict = paginated_area_list_instance.to_dict()
# create an instance of PaginatedAreaList from a dict
paginated_area_list_from_dict = PaginatedAreaList.from_dict(paginated_area_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



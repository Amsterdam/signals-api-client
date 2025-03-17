# CategoryDepartment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**category** | [**TmpCategory**](TmpCategory.md) |  | [readonly] 
**category_id** | **int** |  | 
**is_responsible** | **bool** |  | [optional] 
**can_view** | **bool** |  | [optional] 

## Example

```python
from signals_api_client.models.category_department import CategoryDepartment

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryDepartment from a JSON string
category_department_instance = CategoryDepartment.from_json(json)
# print the JSON string representation of the object
print(CategoryDepartment.to_json())

# convert the object into a dict
category_department_dict = category_department_instance.to_dict()
# create an instance of CategoryDepartment from a dict
category_department_from_dict = CategoryDepartment.from_dict(category_department_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



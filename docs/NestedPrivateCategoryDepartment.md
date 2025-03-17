# NestedPrivateCategoryDepartment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**code** | **str** |  | 
**name** | **str** |  | 
**is_intern** | **bool** |  | 
**is_responsible** | **bool** |  | [readonly] 
**can_view** | **bool** |  | [readonly] 

## Example

```python
from signals_api_client.models.nested_private_category_department import NestedPrivateCategoryDepartment

# TODO update the JSON string below
json = "{}"
# create an instance of NestedPrivateCategoryDepartment from a JSON string
nested_private_category_department_instance = NestedPrivateCategoryDepartment.from_json(json)
# print the JSON string representation of the object
print(NestedPrivateCategoryDepartment.to_json())

# convert the object into a dict
nested_private_category_department_dict = nested_private_category_department_instance.to_dict()
# create an instance of NestedPrivateCategoryDepartment from a dict
nested_private_category_department_from_dict = NestedPrivateCategoryDepartment.from_dict(nested_private_category_department_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



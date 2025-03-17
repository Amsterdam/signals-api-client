# NestedDepartmentModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**code** | **str** |  | [readonly] 
**name** | **str** |  | [readonly] 
**is_intern** | **bool** |  | [readonly] 

## Example

```python
from signals_api_client.models.nested_department_model import NestedDepartmentModel

# TODO update the JSON string below
json = "{}"
# create an instance of NestedDepartmentModel from a JSON string
nested_department_model_instance = NestedDepartmentModel.from_json(json)
# print the JSON string representation of the object
print(NestedDepartmentModel.to_json())

# convert the object into a dict
nested_department_model_dict = nested_department_model_instance.to_dict()
# create an instance of NestedDepartmentModel from a dict
nested_department_model_from_dict = NestedDepartmentModel.from_dict(nested_department_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



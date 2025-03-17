# NestedPublicDepartment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [readonly] 
**name** | **str** |  | [readonly] 
**is_intern** | **bool** |  | [readonly] 

## Example

```python
from signals_api_client.models.nested_public_department import NestedPublicDepartment

# TODO update the JSON string below
json = "{}"
# create an instance of NestedPublicDepartment from a JSON string
nested_public_department_instance = NestedPublicDepartment.from_json(json)
# print the JSON string representation of the object
print(NestedPublicDepartment.to_json())

# convert the object into a dict
nested_public_department_dict = nested_public_department_instance.to_dict()
# create an instance of NestedPublicDepartment from a dict
nested_public_department_from_dict = NestedPublicDepartment.from_dict(nested_public_department_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



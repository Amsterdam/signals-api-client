# NestedTypeModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**created_at** | **datetime** |  | [readonly] 
**created_by** | **str** |  | [optional] 

## Example

```python
from signals_api_client.models.nested_type_model import NestedTypeModel

# TODO update the JSON string below
json = "{}"
# create an instance of NestedTypeModel from a JSON string
nested_type_model_instance = NestedTypeModel.from_json(json)
# print the JSON string representation of the object
print(NestedTypeModel.to_json())

# convert the object into a dict
nested_type_model_dict = nested_type_model_instance.to_dict()
# create an instance of NestedTypeModel from a dict
nested_type_model_from_dict = NestedTypeModel.from_dict(nested_type_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



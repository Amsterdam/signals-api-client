# NestedPriorityModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | [**PriorityEnum**](PriorityEnum.md) |  | [optional] 
**created_by** | **str** |  | [readonly] 

## Example

```python
from signals_api_client.models.nested_priority_model import NestedPriorityModel

# TODO update the JSON string below
json = "{}"
# create an instance of NestedPriorityModel from a JSON string
nested_priority_model_instance = NestedPriorityModel.from_json(json)
# print the JSON string representation of the object
print(NestedPriorityModel.to_json())

# convert the object into a dict
nested_priority_model_dict = nested_priority_model_instance.to_dict()
# create an instance of NestedPriorityModel from a dict
nested_priority_model_from_dict = NestedPriorityModel.from_dict(nested_priority_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



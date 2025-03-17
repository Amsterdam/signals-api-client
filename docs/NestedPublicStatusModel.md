# NestedPublicStatusModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | [readonly] 
**state_display** | **str** |  | [readonly] 

## Example

```python
from signals_api_client.models.nested_public_status_model import NestedPublicStatusModel

# TODO update the JSON string below
json = "{}"
# create an instance of NestedPublicStatusModel from a JSON string
nested_public_status_model_instance = NestedPublicStatusModel.from_json(json)
# print the JSON string representation of the object
print(NestedPublicStatusModel.to_json())

# convert the object into a dict
nested_public_status_model_dict = nested_public_status_model_instance.to_dict()
# create an instance of NestedPublicStatusModel from a dict
nested_public_status_model_from_dict = NestedPublicStatusModel.from_dict(nested_public_status_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



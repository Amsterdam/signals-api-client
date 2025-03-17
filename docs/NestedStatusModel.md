# NestedStatusModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**user** | **str** |  | [readonly] 
**state** | [**NestedStatusModelState**](NestedStatusModelState.md) |  | [optional] 
**state_display** | **str** |  | [readonly] 
**target_api** | [**NestedStatusModelTargetApi**](NestedStatusModelTargetApi.md) |  | [optional] 
**extra_properties** | **object** |  | [optional] 
**send_email** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**email_override** | **str** |  | [optional] 

## Example

```python
from signals_api_client.models.nested_status_model import NestedStatusModel

# TODO update the JSON string below
json = "{}"
# create an instance of NestedStatusModel from a JSON string
nested_status_model_instance = NestedStatusModel.from_json(json)
# print the JSON string representation of the object
print(NestedStatusModel.to_json())

# convert the object into a dict
nested_status_model_dict = nested_status_model_instance.to_dict()
# create an instance of NestedStatusModel from a dict
nested_status_model_from_dict = NestedStatusModel.from_dict(nested_status_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



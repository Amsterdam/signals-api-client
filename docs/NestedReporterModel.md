# NestedReporterModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**sharing_allowed** | **bool** |  | [optional] 
**allows_contact** | **bool** |  | [readonly] 

## Example

```python
from signals_api_client.models.nested_reporter_model import NestedReporterModel

# TODO update the JSON string below
json = "{}"
# create an instance of NestedReporterModel from a JSON string
nested_reporter_model_instance = NestedReporterModel.from_json(json)
# print the JSON string representation of the object
print(NestedReporterModel.to_json())

# convert the object into a dict
nested_reporter_model_dict = nested_reporter_model_instance.to_dict()
# create an instance of NestedReporterModel from a dict
nested_reporter_model_from_dict = NestedReporterModel.from_dict(nested_reporter_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



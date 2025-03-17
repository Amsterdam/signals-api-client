# SignalContextReporterCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub** | **str** |  | [optional] 
**sub_slug** | **str** |  | [optional] 
**departments** | **str** |  | [optional] 
**main** | **str** |  | [optional] 
**main_slug** | **str** |  | [optional] 

## Example

```python
from signals_api_client.models.signal_context_reporter_category import SignalContextReporterCategory

# TODO update the JSON string below
json = "{}"
# create an instance of SignalContextReporterCategory from a JSON string
signal_context_reporter_category_instance = SignalContextReporterCategory.from_json(json)
# print the JSON string representation of the object
print(SignalContextReporterCategory.to_json())

# convert the object into a dict
signal_context_reporter_category_dict = signal_context_reporter_category_instance.to_dict()
# create an instance of SignalContextReporterCategory from a dict
signal_context_reporter_category_from_dict = SignalContextReporterCategory.from_dict(signal_context_reporter_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



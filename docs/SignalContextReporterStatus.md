# SignalContextReporterStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | [optional] 
**state_display** | **str** |  | [optional] 

## Example

```python
from signals_api_client.models.signal_context_reporter_status import SignalContextReporterStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SignalContextReporterStatus from a JSON string
signal_context_reporter_status_instance = SignalContextReporterStatus.from_json(json)
# print the JSON string representation of the object
print(SignalContextReporterStatus.to_json())

# convert the object into a dict
signal_context_reporter_status_dict = signal_context_reporter_status_instance.to_dict()
# create an instance of SignalContextReporterStatus from a dict
signal_context_reporter_status_from_dict = SignalContextReporterStatus.from_dict(signal_context_reporter_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



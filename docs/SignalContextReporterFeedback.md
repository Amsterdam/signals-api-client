# SignalContextReporterFeedback


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_satisfied** | **bool** |  | [optional] 
**submitted_at** | **datetime** |  | [optional] 

## Example

```python
from signals_api_client.models.signal_context_reporter_feedback import SignalContextReporterFeedback

# TODO update the JSON string below
json = "{}"
# create an instance of SignalContextReporterFeedback from a JSON string
signal_context_reporter_feedback_instance = SignalContextReporterFeedback.from_json(json)
# print the JSON string representation of the object
print(SignalContextReporterFeedback.to_json())

# convert the object into a dict
signal_context_reporter_feedback_dict = signal_context_reporter_feedback_instance.to_dict()
# create an instance of SignalContextReporterFeedback from a dict
signal_context_reporter_feedback_from_dict = SignalContextReporterFeedback.from_dict(signal_context_reporter_feedback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



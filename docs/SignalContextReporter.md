# SignalContextReporter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signal_count** | **int** | The number of signals created by the same reporter as the current signal. | [optional] 
**open_count** | **int** | The number of open signals created by the same reporter as the current signal. | [optional] 
**positive_count** | **int** | The number of signals created by the same reporter as the current signal, that have been marked as positive feedback. | [optional] 
**negative_count** | **int** | The number of signals created by the same reporter as the current signal, that have been marked as negative feedback. | [optional] 

## Example

```python
from signals_api_client.models.signal_context_reporter import SignalContextReporter

# TODO update the JSON string below
json = "{}"
# create an instance of SignalContextReporter from a JSON string
signal_context_reporter_instance = SignalContextReporter.from_json(json)
# print the JSON string representation of the object
print(SignalContextReporter.to_json())

# convert the object into a dict
signal_context_reporter_dict = signal_context_reporter_instance.to_dict()
# create an instance of SignalContextReporter from a dict
signal_context_reporter_from_dict = SignalContextReporter.from_dict(signal_context_reporter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



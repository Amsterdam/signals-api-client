# CancelSignalReporter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 

## Example

```python
from signals_api_client.models.cancel_signal_reporter import CancelSignalReporter

# TODO update the JSON string below
json = "{}"
# create an instance of CancelSignalReporter from a JSON string
cancel_signal_reporter_instance = CancelSignalReporter.from_json(json)
# print the JSON string representation of the object
print(CancelSignalReporter.to_json())

# convert the object into a dict
cancel_signal_reporter_dict = cancel_signal_reporter_instance.to_dict()
# create an instance of CancelSignalReporter from a dict
cancel_signal_reporter_from_dict = CancelSignalReporter.from_dict(cancel_signal_reporter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SignalReporter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**allows_contact** | **bool** |  | [readonly] 
**sharing_allowed** | **bool** |  | 
**state** | **str** |  | [readonly] 
**email_verification_token_expires** | **datetime** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from signals_api_client.models.signal_reporter import SignalReporter

# TODO update the JSON string below
json = "{}"
# create an instance of SignalReporter from a JSON string
signal_reporter_instance = SignalReporter.from_json(json)
# print the JSON string representation of the object
print(SignalReporter.to_json())

# convert the object into a dict
signal_reporter_dict = signal_reporter_instance.to_dict()
# create an instance of SignalReporter from a dict
signal_reporter_from_dict = SignalReporter.from_dict(signal_reporter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



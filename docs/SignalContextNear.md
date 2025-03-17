# SignalContextNear


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signal_count** | **int** | The number of signals in the same category as the current signal, within a radius of 500 meters, created in the last 4 weeks. | [optional] 

## Example

```python
from signals_api_client.models.signal_context_near import SignalContextNear

# TODO update the JSON string below
json = "{}"
# create an instance of SignalContextNear from a JSON string
signal_context_near_instance = SignalContextNear.from_json(json)
# print the JSON string representation of the object
print(SignalContextNear.to_json())

# convert the object into a dict
signal_context_near_dict = signal_context_near_instance.to_dict()
# create an instance of SignalContextNear from a dict
signal_context_near_from_dict = SignalContextNear.from_dict(signal_context_near_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



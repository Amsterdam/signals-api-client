# SignalContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links7**](Links7.md) |  | 
**near** | [**SignalContextNear**](SignalContextNear.md) |  | 
**reporter** | [**SignalContextReporter**](SignalContextReporter.md) |  | 

## Example

```python
from signals_api_client.models.signal_context import SignalContext

# TODO update the JSON string below
json = "{}"
# create an instance of SignalContext from a JSON string
signal_context_instance = SignalContext.from_json(json)
# print the JSON string representation of the object
print(SignalContext.to_json())

# convert the object into a dict
signal_context_dict = signal_context_instance.to_dict()
# create an instance of SignalContext from a dict
signal_context_from_dict = SignalContext.from_dict(signal_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



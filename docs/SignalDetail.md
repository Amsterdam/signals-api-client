# SignalDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links8**](Links8.md) |  | 
**display** | **str** |  | [readonly] 
**uuid** | **str** |  | [readonly] 
**id_display** | **str** |  | [readonly] 
**text** | **str** |  | [readonly] 
**status** | [**NestedMySignalStatus**](NestedMySignalStatus.md) |  | 
**location** | [**NestedMySignalLocation**](NestedMySignalLocation.md) |  | 
**extra_properties** | **object** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 

## Example

```python
from signals_api_client.models.signal_detail import SignalDetail

# TODO update the JSON string below
json = "{}"
# create an instance of SignalDetail from a JSON string
signal_detail_instance = SignalDetail.from_json(json)
# print the JSON string representation of the object
print(SignalDetail.to_json())

# convert the object into a dict
signal_detail_dict = signal_detail_instance.to_dict()
# create an instance of SignalDetail from a dict
signal_detail_from_dict = SignalDetail.from_dict(signal_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



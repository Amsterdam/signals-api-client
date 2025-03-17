# AbridgedChildSignal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links**](Links.md) |  | 
**id** | **int** |  | [readonly] 
**status** | **str** |  | [readonly] 
**category** | **str** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**can_view_signal** | **str** |  | [readonly] 

## Example

```python
from signals_api_client.models.abridged_child_signal import AbridgedChildSignal

# TODO update the JSON string below
json = "{}"
# create an instance of AbridgedChildSignal from a JSON string
abridged_child_signal_instance = AbridgedChildSignal.from_json(json)
# print the JSON string representation of the object
print(AbridgedChildSignal.to_json())

# convert the object into a dict
abridged_child_signal_dict = abridged_child_signal_instance.to_dict()
# create an instance of AbridgedChildSignal from a dict
abridged_child_signal_from_dict = AbridgedChildSignal.from_dict(abridged_child_signal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



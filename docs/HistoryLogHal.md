# HistoryLogHal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**when** | **datetime** |  | 
**what** | **str** | \&quot;what\&quot; in the style of the signals_history_view Present for backwards compatibility | [readonly] 
**action** | **str** |  | [readonly] 
**description** | **str** |  | 
**signal** | **str** |  | 

## Example

```python
from signals_api_client.models.history_log_hal import HistoryLogHal

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryLogHal from a JSON string
history_log_hal_instance = HistoryLogHal.from_json(json)
# print the JSON string representation of the object
print(HistoryLogHal.to_json())

# convert the object into a dict
history_log_hal_dict = history_log_hal_instance.to_dict()
# create an instance of HistoryLogHal from a dict
history_log_hal_from_dict = HistoryLogHal.from_dict(history_log_hal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



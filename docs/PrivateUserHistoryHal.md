# PrivateUserHistoryHal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | [readonly] 
**when** | **datetime** |  | [readonly] 
**what** | **str** |  | [readonly] 
**action** | **str** |  | [readonly] 
**description** | **str** |  | [readonly] 
**who** | **str** | \&quot;who\&quot; in the style of the signals_history_view Present for backwards compatibility | [readonly] 
**user** | **int** |  | [readonly] 

## Example

```python
from signals_api_client.models.private_user_history_hal import PrivateUserHistoryHal

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateUserHistoryHal from a JSON string
private_user_history_hal_instance = PrivateUserHistoryHal.from_json(json)
# print the JSON string representation of the object
print(PrivateUserHistoryHal.to_json())

# convert the object into a dict
private_user_history_hal_dict = private_user_history_hal_instance.to_dict()
# create an instance of PrivateUserHistoryHal from a dict
private_user_history_hal_from_dict = PrivateUserHistoryHal.from_dict(private_user_history_hal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



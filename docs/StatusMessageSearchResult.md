# StatusMessageSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**title** | **str** |  | 
**text** | **str** |  | 
**active** | **bool** |  | 
**state** | **str** |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from signals_api_client.models.status_message_search_result import StatusMessageSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of StatusMessageSearchResult from a JSON string
status_message_search_result_instance = StatusMessageSearchResult.from_json(json)
# print the JSON string representation of the object
print(StatusMessageSearchResult.to_json())

# convert the object into a dict
status_message_search_result_dict = status_message_search_result_instance.to_dict()
# create an instance of StatusMessageSearchResult from a dict
status_message_search_result_from_dict = StatusMessageSearchResult.from_dict(status_message_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



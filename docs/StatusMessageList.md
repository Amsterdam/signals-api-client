# StatusMessageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [readonly] 
**results** | [**List[StatusMessageSearchResult]**](StatusMessageSearchResult.md) |  | 
**facets** | [**StatusMessageFacet**](StatusMessageFacet.md) |  | 

## Example

```python
from signals_api_client.models.status_message_list import StatusMessageList

# TODO update the JSON string below
json = "{}"
# create an instance of StatusMessageList from a JSON string
status_message_list_instance = StatusMessageList.from_json(json)
# print the JSON string representation of the object
print(StatusMessageList.to_json())

# convert the object into a dict
status_message_list_dict = status_message_list_instance.to_dict()
# create an instance of StatusMessageList from a dict
status_message_list_from_dict = StatusMessageList.from_dict(status_message_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



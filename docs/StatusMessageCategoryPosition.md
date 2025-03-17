# StatusMessageCategoryPosition

Serializer for the StatusMessageCategory model used for ordering status messages.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_message** | **int** |  | 
**position** | **int** |  | 

## Example

```python
from signals_api_client.models.status_message_category_position import StatusMessageCategoryPosition

# TODO update the JSON string below
json = "{}"
# create an instance of StatusMessageCategoryPosition from a JSON string
status_message_category_position_instance = StatusMessageCategoryPosition.from_json(json)
# print the JSON string representation of the object
print(StatusMessageCategoryPosition.to_json())

# convert the object into a dict
status_message_category_position_dict = status_message_category_position_instance.to_dict()
# create an instance of StatusMessageCategoryPosition from a dict
status_message_category_position_from_dict = StatusMessageCategoryPosition.from_dict(status_message_category_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



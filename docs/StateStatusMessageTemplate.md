# StateStatusMessageTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**StateStatusMessageTemplateStateEnum**](StateStatusMessageTemplateStateEnum.md) |  | 
**templates** | **str** |  | [readonly] 

## Example

```python
from signals_api_client.models.state_status_message_template import StateStatusMessageTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of StateStatusMessageTemplate from a JSON string
state_status_message_template_instance = StateStatusMessageTemplate.from_json(json)
# print the JSON string representation of the object
print(StateStatusMessageTemplate.to_json())

# convert the object into a dict
state_status_message_template_dict = state_status_message_template_instance.to_dict()
# create an instance of StateStatusMessageTemplate from a dict
state_status_message_template_from_dict = StateStatusMessageTemplate.from_dict(state_status_message_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



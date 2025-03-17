# Feedback


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_satisfied** | **bool** |  | 
**allows_contact** | **bool** |  | [optional] 
**text** | **str** |  | [optional] 
**text_list** | **List[str]** |  | [optional] 
**text_extra** | **str** |  | [optional] 
**signal_id** | **str** |  | [readonly] 

## Example

```python
from signals_api_client.models.feedback import Feedback

# TODO update the JSON string below
json = "{}"
# create an instance of Feedback from a JSON string
feedback_instance = Feedback.from_json(json)
# print the JSON string representation of the object
print(Feedback.to_json())

# convert the object into a dict
feedback_dict = feedback_instance.to_dict()
# create an instance of Feedback from a dict
feedback_from_dict = Feedback.from_dict(feedback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



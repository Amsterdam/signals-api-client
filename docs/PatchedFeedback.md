# PatchedFeedback


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_satisfied** | **bool** |  | [optional] 
**allows_contact** | **bool** |  | [optional] 
**text** | **str** |  | [optional] 
**text_list** | **List[str]** |  | [optional] 
**text_extra** | **str** |  | [optional] 
**signal_id** | **str** |  | [optional] [readonly] 

## Example

```python
from signals_api_client.models.patched_feedback import PatchedFeedback

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedFeedback from a JSON string
patched_feedback_instance = PatchedFeedback.from_json(json)
# print the JSON string representation of the object
print(PatchedFeedback.to_json())

# convert the object into a dict
patched_feedback_dict = patched_feedback_instance.to_dict()
# create an instance of PatchedFeedback from a dict
patched_feedback_from_dict = PatchedFeedback.from_dict(patched_feedback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



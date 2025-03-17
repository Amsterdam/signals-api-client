# NestedNoteModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**created_by** | **str** |  | [readonly] 

## Example

```python
from signals_api_client.models.nested_note_model import NestedNoteModel

# TODO update the JSON string below
json = "{}"
# create an instance of NestedNoteModel from a JSON string
nested_note_model_instance = NestedNoteModel.from_json(json)
# print the JSON string representation of the object
print(NestedNoteModel.to_json())

# convert the object into a dict
nested_note_model_dict = nested_note_model_instance.to_dict()
# create an instance of NestedNoteModel from a dict
nested_note_model_from_dict = NestedNoteModel.from_dict(nested_note_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



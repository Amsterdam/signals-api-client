# Highlight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **List[str]** |  | [optional] 
**text** | **List[str]** |  | [optional] 

## Example

```python
from signals_api_client.models.highlight import Highlight

# TODO update the JSON string below
json = "{}"
# create an instance of Highlight from a JSON string
highlight_instance = Highlight.from_json(json)
# print the JSON string representation of the object
print(Highlight.to_json())

# convert the object into a dict
highlight_dict = highlight_instance.to_dict()
# create an instance of Highlight from a dict
highlight_from_dict = Highlight.from_dict(highlight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



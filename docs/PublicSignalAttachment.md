# PublicSignalAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display** | **str** |  | [readonly] 
**links** | **str** |  | [readonly] 
**location** | **str** |  | [readonly] 
**is_image** | **bool** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**file** | **str** |  | 

## Example

```python
from signals_api_client.models.public_signal_attachment import PublicSignalAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of PublicSignalAttachment from a JSON string
public_signal_attachment_instance = PublicSignalAttachment.from_json(json)
# print the JSON string representation of the object
print(PublicSignalAttachment.to_json())

# convert the object into a dict
public_signal_attachment_dict = public_signal_attachment_instance.to_dict()
# create an instance of PublicSignalAttachment from a dict
public_signal_attachment_from_dict = PublicSignalAttachment.from_dict(public_signal_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PrivateSignalAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display** | **str** |  | [readonly] 
**links** | [**Links5**](Links5.md) |  | 
**location** | **str** |  | [readonly] 
**is_image** | **bool** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**file** | **str** |  | 
**created_by** | **str** |  | [readonly] 
**public** | **bool** |  | [optional] 
**caption** | **str** |  | [optional] 

## Example

```python
from signals_api_client.models.private_signal_attachment import PrivateSignalAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateSignalAttachment from a JSON string
private_signal_attachment_instance = PrivateSignalAttachment.from_json(json)
# print the JSON string representation of the object
print(PrivateSignalAttachment.to_json())

# convert the object into a dict
private_signal_attachment_dict = private_signal_attachment_instance.to_dict()
# create an instance of PrivateSignalAttachment from a dict
private_signal_attachment_from_dict = PrivateSignalAttachment.from_dict(private_signal_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



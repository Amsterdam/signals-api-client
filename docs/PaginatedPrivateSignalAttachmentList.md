# PaginatedPrivateSignalAttachmentList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedAbridgedChildSignalListLinks**](PaginatedAbridgedChildSignalListLinks.md) |  | [optional] 
**count** | **int** |  | [optional] 
**results** | [**List[PrivateSignalAttachment]**](PrivateSignalAttachment.md) |  | [optional] 

## Example

```python
from signals_api_client.models.paginated_private_signal_attachment_list import PaginatedPrivateSignalAttachmentList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPrivateSignalAttachmentList from a JSON string
paginated_private_signal_attachment_list_instance = PaginatedPrivateSignalAttachmentList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPrivateSignalAttachmentList.to_json())

# convert the object into a dict
paginated_private_signal_attachment_list_dict = paginated_private_signal_attachment_list_instance.to_dict()
# create an instance of PaginatedPrivateSignalAttachmentList from a dict
paginated_private_signal_attachment_list_from_dict = PaginatedPrivateSignalAttachmentList.from_dict(paginated_private_signal_attachment_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



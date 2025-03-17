# EmailPreviewPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**StatusEnum**](StatusEnum.md) |  | 
**text** | **str** |  | [optional] 
**email_override** | **str** |  | [optional] 

## Example

```python
from signals_api_client.models.email_preview_post import EmailPreviewPost

# TODO update the JSON string below
json = "{}"
# create an instance of EmailPreviewPost from a JSON string
email_preview_post_instance = EmailPreviewPost.from_json(json)
# print the JSON string representation of the object
print(EmailPreviewPost.to_json())

# convert the object into a dict
email_preview_post_dict = email_preview_post_instance.to_dict()
# create an instance of EmailPreviewPost from a dict
email_preview_post_from_dict = EmailPreviewPost.from_dict(email_preview_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



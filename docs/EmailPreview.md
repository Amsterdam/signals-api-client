# EmailPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** |  | [readonly] 
**html** | **str** |  | [readonly] 

## Example

```python
from signals_api_client.models.email_preview import EmailPreview

# TODO update the JSON string below
json = "{}"
# create an instance of EmailPreview from a JSON string
email_preview_instance = EmailPreview.from_json(json)
# print the JSON string representation of the object
print(EmailPreview.to_json())

# convert the object into a dict
email_preview_dict = email_preview_instance.to_dict()
# create an instance of EmailPreview from a dict
email_preview_from_dict = EmailPreview.from_dict(email_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



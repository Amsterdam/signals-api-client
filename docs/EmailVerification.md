# EmailVerification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 

## Example

```python
from signals_api_client.models.email_verification import EmailVerification

# TODO update the JSON string below
json = "{}"
# create an instance of EmailVerification from a JSON string
email_verification_instance = EmailVerification.from_json(json)
# print the JSON string representation of the object
print(EmailVerification.to_json())

# convert the object into a dict
email_verification_dict = email_verification_instance.to_dict()
# create an instance of EmailVerification from a dict
email_verification_from_dict = EmailVerification.from_dict(email_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



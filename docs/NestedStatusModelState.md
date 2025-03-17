# NestedStatusModelState

Melding status  * `m` - Gemeld * `i` - In afwachting van behandeling * `b` - In behandeling * `h` - On hold * `ingepland` - Ingepland * `ready to send` - Extern: te verzenden * `o` - Afgehandeld * `a` - Geannuleerd * `reopened` - Heropend * `s` - Gesplitst * `closure requested` - Extern: verzoek tot afhandeling * `reaction requested` - Reactie gevraagd * `reaction received` - Reactie ontvangen * `forward to external` - Doorgezet naar extern * `sent` - Extern: verzonden * `send failed` - Extern: mislukt * `done external` - Extern: afgehandeld * `reopen requested` - Verzoek tot heropenen

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from signals_api_client.models.nested_status_model_state import NestedStatusModelState

# TODO update the JSON string below
json = "{}"
# create an instance of NestedStatusModelState from a JSON string
nested_status_model_state_instance = NestedStatusModelState.from_json(json)
# print the JSON string representation of the object
print(NestedStatusModelState.to_json())

# convert the object into a dict
nested_status_model_state_dict = nested_status_model_state_instance.to_dict()
# create an instance of NestedStatusModelState from a dict
nested_status_model_state_from_dict = NestedStatusModelState.from_dict(nested_status_model_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



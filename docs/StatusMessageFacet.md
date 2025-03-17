# StatusMessageFacet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**List[StateTermsFacet]**](StateTermsFacet.md) |  | 
**active** | [**List[ActiveTermsFacet]**](ActiveTermsFacet.md) |  | 

## Example

```python
from signals_api_client.models.status_message_facet import StatusMessageFacet

# TODO update the JSON string below
json = "{}"
# create an instance of StatusMessageFacet from a JSON string
status_message_facet_instance = StatusMessageFacet.from_json(json)
# print the JSON string representation of the object
print(StatusMessageFacet.to_json())

# convert the object into a dict
status_message_facet_dict = status_message_facet_instance.to_dict()
# create an instance of StatusMessageFacet from a dict
status_message_facet_from_dict = StatusMessageFacet.from_dict(status_message_facet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



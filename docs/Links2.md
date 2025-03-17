# Links2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**curies** | [**Links1Curies**](Links1Curies.md) |  | [optional] 
**var_self** | [**Links1Self**](Links1Self.md) |  | [optional] 
**archives** | [**Links1Archives**](Links1Archives.md) |  | [optional] 
**sia_status_message_templates** | [**Links2SiaStatusMessageTemplates**](Links2SiaStatusMessageTemplates.md) |  | [optional] 

## Example

```python
from signals_api_client.models.links2 import Links2

# TODO update the JSON string below
json = "{}"
# create an instance of Links2 from a JSON string
links2_instance = Links2.from_json(json)
# print the JSON string representation of the object
print(Links2.to_json())

# convert the object into a dict
links2_dict = links2_instance.to_dict()
# create an instance of Links2 from a dict
links2_from_dict = Links2.from_dict(links2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



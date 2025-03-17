# Links8


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**curies** | [**Links1Curies**](Links1Curies.md) |  | [optional] 
**var_self** | [**Links8Self**](Links8Self.md) |  | [optional] 
**archives** | [**Links8Archives**](Links8Archives.md) |  | [optional] 
**sia_attachments** | [**List[Links8SiaAttachmentsInner]**](Links8SiaAttachmentsInner.md) |  | [optional] 

## Example

```python
from signals_api_client.models.links8 import Links8

# TODO update the JSON string below
json = "{}"
# create an instance of Links8 from a JSON string
links8_instance = Links8.from_json(json)
# print the JSON string representation of the object
print(Links8.to_json())

# convert the object into a dict
links8_dict = links8_instance.to_dict()
# create an instance of Links8 from a dict
links8_from_dict = Links8.from_dict(links8_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



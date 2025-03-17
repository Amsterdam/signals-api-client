# Links6


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**curies** | [**Links1Curies**](Links1Curies.md) |  | [optional] 
**var_self** | [**Links6Self**](Links6Self.md) |  | [optional] 
**archives** | [**Links6Archives**](Links6Archives.md) |  | [optional] 
**sia_attachments** | [**Links6SiaAttachments**](Links6SiaAttachments.md) |  | [optional] 
**sia_pdf** | [**Links6SiaPdf**](Links6SiaPdf.md) |  | [optional] 
**sia_context** | [**Links6SiaContext**](Links6SiaContext.md) |  | [optional] 
**sia_parent** | [**LinksSelf**](LinksSelf.md) |  | [optional] 
**sia_children** | [**List[Links6SiaChildrenInner]**](Links6SiaChildrenInner.md) |  | [optional] 

## Example

```python
from signals_api_client.models.links6 import Links6

# TODO update the JSON string below
json = "{}"
# create an instance of Links6 from a JSON string
links6_instance = Links6.from_json(json)
# print the JSON string representation of the object
print(Links6.to_json())

# convert the object into a dict
links6_dict = links6_instance.to_dict()
# create an instance of Links6 from a dict
links6_from_dict = Links6.from_dict(links6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



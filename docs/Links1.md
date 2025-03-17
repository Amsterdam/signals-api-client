# Links1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**curies** | [**Links1Curies**](Links1Curies.md) |  | [optional] 
**var_self** | [**Links1Self**](Links1Self.md) |  | [optional] 
**archives** | [**Links1Archives**](Links1Archives.md) |  | [optional] 
**sia_questionnaire** | [**Links1SiaQuestionnaire**](Links1SiaQuestionnaire.md) |  | [optional] 
**sia_icon** | [**Links1SiaIcon**](Links1SiaIcon.md) |  | [optional] 

## Example

```python
from signals_api_client.models.links1 import Links1

# TODO update the JSON string below
json = "{}"
# create an instance of Links1 from a JSON string
links1_instance = Links1.from_json(json)
# print the JSON string representation of the object
print(Links1.to_json())

# convert the object into a dict
links1_dict = links1_instance.to_dict()
# create an instance of Links1 from a dict
links1_from_dict = Links1.from_dict(links1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Links7


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**curies** | [**Links1Curies**](Links1Curies.md) |  | [optional] 
**var_self** | [**LinksSelf**](LinksSelf.md) |  | [optional] 
**sia_context_reporter_detail** | [**Links7SiaContextReporterDetail**](Links7SiaContextReporterDetail.md) |  | [optional] 
**sia_context_geography_detail** | [**Links7SiaContextGeographyDetail**](Links7SiaContextGeographyDetail.md) |  | [optional] 

## Example

```python
from signals_api_client.models.links7 import Links7

# TODO update the JSON string below
json = "{}"
# create an instance of Links7 from a JSON string
links7_instance = Links7.from_json(json)
# print the JSON string representation of the object
print(Links7.to_json())

# convert the object into a dict
links7_dict = links7_instance.to_dict()
# create an instance of Links7 from a dict
links7_from_dict = Links7.from_dict(links7_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



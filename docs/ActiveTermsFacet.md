# ActiveTermsFacet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [readonly] 
**active** | **bool** |  | [readonly] 
**term** | **bool** |  | [readonly] 

## Example

```python
from signals_api_client.models.active_terms_facet import ActiveTermsFacet

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveTermsFacet from a JSON string
active_terms_facet_instance = ActiveTermsFacet.from_json(json)
# print the JSON string representation of the object
print(ActiveTermsFacet.to_json())

# convert the object into a dict
active_terms_facet_dict = active_terms_facet_instance.to_dict()
# create an instance of ActiveTermsFacet from a dict
active_terms_facet_from_dict = ActiveTermsFacet.from_dict(active_terms_facet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



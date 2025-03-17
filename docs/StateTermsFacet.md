# StateTermsFacet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [readonly] 
**active** | **bool** |  | [readonly] 
**term** | **str** |  | [readonly] 

## Example

```python
from signals_api_client.models.state_terms_facet import StateTermsFacet

# TODO update the JSON string below
json = "{}"
# create an instance of StateTermsFacet from a JSON string
state_terms_facet_instance = StateTermsFacet.from_json(json)
# print the JSON string representation of the object
print(StateTermsFacet.to_json())

# convert the object into a dict
state_terms_facet_dict = state_terms_facet_instance.to_dict()
# create an instance of StateTermsFacet from a dict
state_terms_facet_from_dict = StateTermsFacet.from_dict(state_terms_facet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# V1PublicSignalsGeographyRetrieve200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**features** | [**List[V1PublicSignalsGeographyRetrieve200ResponseFeaturesInner]**](V1PublicSignalsGeographyRetrieve200ResponseFeaturesInner.md) |  | [optional] 

## Example

```python
from signals_api_client.models.v1_public_signals_geography_retrieve200_response import V1PublicSignalsGeographyRetrieve200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1PublicSignalsGeographyRetrieve200Response from a JSON string
v1_public_signals_geography_retrieve200_response_instance = V1PublicSignalsGeographyRetrieve200Response.from_json(json)
# print the JSON string representation of the object
print(V1PublicSignalsGeographyRetrieve200Response.to_json())

# convert the object into a dict
v1_public_signals_geography_retrieve200_response_dict = v1_public_signals_geography_retrieve200_response_instance.to_dict()
# create an instance of V1PublicSignalsGeographyRetrieve200Response from a dict
v1_public_signals_geography_retrieve200_response_from_dict = V1PublicSignalsGeographyRetrieve200Response.from_dict(v1_public_signals_geography_retrieve200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



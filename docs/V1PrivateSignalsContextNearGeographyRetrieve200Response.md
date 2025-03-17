# V1PrivateSignalsContextNearGeographyRetrieve200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**features** | [**List[V1PrivateSignalsContextNearGeographyRetrieve200ResponseFeaturesInner]**](V1PrivateSignalsContextNearGeographyRetrieve200ResponseFeaturesInner.md) |  | [optional] 

## Example

```python
from signals_api_client.models.v1_private_signals_context_near_geography_retrieve200_response import V1PrivateSignalsContextNearGeographyRetrieve200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1PrivateSignalsContextNearGeographyRetrieve200Response from a JSON string
v1_private_signals_context_near_geography_retrieve200_response_instance = V1PrivateSignalsContextNearGeographyRetrieve200Response.from_json(json)
# print the JSON string representation of the object
print(V1PrivateSignalsContextNearGeographyRetrieve200Response.to_json())

# convert the object into a dict
v1_private_signals_context_near_geography_retrieve200_response_dict = v1_private_signals_context_near_geography_retrieve200_response_instance.to_dict()
# create an instance of V1PrivateSignalsContextNearGeographyRetrieve200Response from a dict
v1_private_signals_context_near_geography_retrieve200_response_from_dict = V1PrivateSignalsContextNearGeographyRetrieve200Response.from_dict(v1_private_signals_context_near_geography_retrieve200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



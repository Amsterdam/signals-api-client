# V1PrivateSignalsGeographyRetrieve200ResponseFeaturesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**geometry** | [**V1PrivateSignalsContextNearGeographyRetrieve200ResponseFeaturesInnerGeometry**](V1PrivateSignalsContextNearGeographyRetrieve200ResponseFeaturesInnerGeometry.md) |  | [optional] 
**properties** | [**V1PrivateSignalsGeographyRetrieve200ResponseFeaturesInnerProperties**](V1PrivateSignalsGeographyRetrieve200ResponseFeaturesInnerProperties.md) |  | [optional] 

## Example

```python
from signals_api_client.models.v1_private_signals_geography_retrieve200_response_features_inner import V1PrivateSignalsGeographyRetrieve200ResponseFeaturesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1PrivateSignalsGeographyRetrieve200ResponseFeaturesInner from a JSON string
v1_private_signals_geography_retrieve200_response_features_inner_instance = V1PrivateSignalsGeographyRetrieve200ResponseFeaturesInner.from_json(json)
# print the JSON string representation of the object
print(V1PrivateSignalsGeographyRetrieve200ResponseFeaturesInner.to_json())

# convert the object into a dict
v1_private_signals_geography_retrieve200_response_features_inner_dict = v1_private_signals_geography_retrieve200_response_features_inner_instance.to_dict()
# create an instance of V1PrivateSignalsGeographyRetrieve200ResponseFeaturesInner from a dict
v1_private_signals_geography_retrieve200_response_features_inner_from_dict = V1PrivateSignalsGeographyRetrieve200ResponseFeaturesInner.from_dict(v1_private_signals_geography_retrieve200_response_features_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



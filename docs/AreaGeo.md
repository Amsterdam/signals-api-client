# AreaGeo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**GisFeatureEnum**](GisFeatureEnum.md) |  | [optional] 
**geometry** | [**AreaCreateGeometry**](AreaCreateGeometry.md) |  | [optional] 
**properties** | [**AreaGeoProperties**](AreaGeoProperties.md) |  | [optional] 

## Example

```python
from signals_api_client.models.area_geo import AreaGeo

# TODO update the JSON string below
json = "{}"
# create an instance of AreaGeo from a JSON string
area_geo_instance = AreaGeo.from_json(json)
# print the JSON string representation of the object
print(AreaGeo.to_json())

# convert the object into a dict
area_geo_dict = area_geo_instance.to_dict()
# create an instance of AreaGeo from a dict
area_geo_from_dict = AreaGeo.from_dict(area_geo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



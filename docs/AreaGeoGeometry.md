# AreaGeoGeometry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**coordinates** | **List[List[List[List[float]]]]** |  | [optional] 

## Example

```python
from signals_api_client.models.area_geo_geometry import AreaGeoGeometry

# TODO update the JSON string below
json = "{}"
# create an instance of AreaGeoGeometry from a JSON string
area_geo_geometry_instance = AreaGeoGeometry.from_json(json)
# print the JSON string representation of the object
print(AreaGeoGeometry.to_json())

# convert the object into a dict
area_geo_geometry_dict = area_geo_geometry_instance.to_dict()
# create an instance of AreaGeoGeometry from a dict
area_geo_geometry_from_dict = AreaGeoGeometry.from_dict(area_geo_geometry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



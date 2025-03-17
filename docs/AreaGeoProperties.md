# AreaGeoProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**type** | [**AreaType**](AreaType.md) |  | [optional] 

## Example

```python
from signals_api_client.models.area_geo_properties import AreaGeoProperties

# TODO update the JSON string below
json = "{}"
# create an instance of AreaGeoProperties from a JSON string
area_geo_properties_instance = AreaGeoProperties.from_json(json)
# print the JSON string representation of the object
print(AreaGeoProperties.to_json())

# convert the object into a dict
area_geo_properties_dict = area_geo_properties_instance.to_dict()
# create an instance of AreaGeoProperties from a dict
area_geo_properties_from_dict = AreaGeoProperties.from_dict(area_geo_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AreaCreateGeometry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**coordinates** | **List[List[List[List[float]]]]** |  | [optional] 

## Example

```python
from signals_api_client.models.area_create_geometry import AreaCreateGeometry

# TODO update the JSON string below
json = "{}"
# create an instance of AreaCreateGeometry from a JSON string
area_create_geometry_instance = AreaCreateGeometry.from_json(json)
# print the JSON string representation of the object
print(AreaCreateGeometry.to_json())

# convert the object into a dict
area_create_geometry_dict = area_create_geometry_instance.to_dict()
# create an instance of AreaCreateGeometry from a dict
area_create_geometry_from_dict = AreaCreateGeometry.from_dict(area_create_geometry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



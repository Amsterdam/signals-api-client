# AreaCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**code** | **str** |  | 
**type** | **int** |  | 
**geometry** | [**AreaCreateGeometry**](AreaCreateGeometry.md) |  | 

## Example

```python
from signals_api_client.models.area_create import AreaCreate

# TODO update the JSON string below
json = "{}"
# create an instance of AreaCreate from a JSON string
area_create_instance = AreaCreate.from_json(json)
# print the JSON string representation of the object
print(AreaCreate.to_json())

# convert the object into a dict
area_create_dict = area_create_instance.to_dict()
# create an instance of AreaCreate from a dict
area_create_from_dict = AreaCreate.from_dict(area_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



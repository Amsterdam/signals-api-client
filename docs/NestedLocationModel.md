# NestedLocationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**stadsdeel** | [**StadsdeelEnum**](StadsdeelEnum.md) |  | [optional] 
**buurt_code** | **str** |  | [optional] 
**area_type_code** | **str** |  | [optional] 
**area_code** | **str** |  | [optional] 
**area_name** | **str** |  | [optional] 
**address** | **object** |  | [optional] 
**address_text** | **str** |  | [readonly] 
**postcode** | **str** |  | [readonly] 
**geometrie** | [**NestedLocationModelGeometrie**](NestedLocationModelGeometrie.md) |  | 
**extra_properties** | **object** |  | [optional] 
**created_by** | **str** |  | [readonly] 
**bag_validated** | **bool** |  | [readonly] 

## Example

```python
from signals_api_client.models.nested_location_model import NestedLocationModel

# TODO update the JSON string below
json = "{}"
# create an instance of NestedLocationModel from a JSON string
nested_location_model_instance = NestedLocationModel.from_json(json)
# print the JSON string representation of the object
print(NestedLocationModel.to_json())

# convert the object into a dict
nested_location_model_dict = nested_location_model_instance.to_dict()
# create an instance of NestedLocationModel from a dict
nested_location_model_from_dict = NestedLocationModel.from_dict(nested_location_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CategoryHAL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links1**](Links1.md) |  | 
**display** | **str** |  | [readonly] 
**name** | **str** |  | 
**slug** | **str** |  | [readonly] 
**handling** | [**HandlingEnum**](HandlingEnum.md) |  | [optional] 
**departments** | **str** |  | [readonly] 
**is_active** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**handling_message** | **str** |  | [optional] 
**questionnaire** | **str** |  | [readonly] 
**public_name** | **str** |  | [optional] 
**is_public_accessible** | **bool** |  | [optional] 

## Example

```python
from signals_api_client.models.category_hal import CategoryHAL

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryHAL from a JSON string
category_hal_instance = CategoryHAL.from_json(json)
# print the JSON string representation of the object
print(CategoryHAL.to_json())

# convert the object into a dict
category_hal_dict = category_hal_instance.to_dict()
# create an instance of CategoryHAL from a dict
category_hal_from_dict = CategoryHAL.from_dict(category_hal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



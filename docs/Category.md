# Category


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links1**](Links1.md) |  | 
**display** | **str** |  | [readonly] 
**name** | **str** |  | 
**slug** | **str** |  | [readonly] 
**public_name** | **str** |  | [optional] 
**is_public_accessible** | **bool** |  | 
**sub_categories** | [**List[CategoryHAL]**](CategoryHAL.md) |  | 
**configuration** | **object** |  | [optional] 
**handling** | [**HandlingEnum**](HandlingEnum.md) |  | [optional] 
**departments** | **str** |  | [readonly] 
**is_active** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**handling_message** | **str** |  | [optional] 
**questionnaire** | **str** |  | [readonly] 

## Example

```python
from signals_api_client.models.category import Category

# TODO update the JSON string below
json = "{}"
# create an instance of Category from a JSON string
category_instance = Category.from_json(json)
# print the JSON string representation of the object
print(Category.to_json())

# convert the object into a dict
category_dict = category_instance.to_dict()
# create an instance of Category from a dict
category_from_dict = Category.from_dict(category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



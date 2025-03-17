# ParentCategoryHAL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links1**](Links1.md) |  | 
**display** | **str** |  | [readonly] 
**name** | **str** |  | 
**slug** | **str** |  | [readonly] 
**public_name** | **str** |  | [optional] 
**is_public_accessible** | **str** |  | [readonly] 
**sub_categories** | [**List[CategoryHAL]**](CategoryHAL.md) |  | 
**configuration** | **object** |  | [optional] 

## Example

```python
from signals_api_client.models.parent_category_hal import ParentCategoryHAL

# TODO update the JSON string below
json = "{}"
# create an instance of ParentCategoryHAL from a JSON string
parent_category_hal_instance = ParentCategoryHAL.from_json(json)
# print the JSON string representation of the object
print(ParentCategoryHAL.to_json())

# convert the object into a dict
parent_category_hal_dict = parent_category_hal_instance.to_dict()
# create an instance of ParentCategoryHAL from a dict
parent_category_hal_from_dict = ParentCategoryHAL.from_dict(parent_category_hal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



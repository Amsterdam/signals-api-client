# NestedCategoryModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_category** | **str** |  | [optional] 
**sub** | **str** |  | [readonly] 
**sub_slug** | **str** |  | [readonly] 
**main** | **str** |  | [readonly] 
**main_slug** | **str** |  | [readonly] 
**category_url** | **str** |  | [optional] 
**departments** | **str** |  | [readonly] 
**created_by** | **str** |  | [readonly] 
**text** | **str** |  | [optional] 
**deadline** | **datetime** |  | [readonly] 
**deadline_factor_3** | **datetime** |  | [readonly] 

## Example

```python
from signals_api_client.models.nested_category_model import NestedCategoryModel

# TODO update the JSON string below
json = "{}"
# create an instance of NestedCategoryModel from a JSON string
nested_category_model_instance = NestedCategoryModel.from_json(json)
# print the JSON string representation of the object
print(NestedCategoryModel.to_json())

# convert the object into a dict
nested_category_model_dict = nested_category_model_instance.to_dict()
# create an instance of NestedCategoryModel from a dict
nested_category_model_from_dict = NestedCategoryModel.from_dict(nested_category_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



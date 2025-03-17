# PatchedPrivateCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links2**](Links2.md) |  | [optional] 
**display** | **str** |  | [optional] [readonly] 
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**slug** | **str** |  | [optional] [readonly] 
**is_active** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**handling_message** | **str** |  | [optional] 
**sla** | **Dict[str, object]** |  | [optional] [readonly] 
**new_sla** | [**PrivateCategorySLA**](PrivateCategorySLA.md) |  | [optional] 
**departments** | [**List[NestedPrivateCategoryDepartment]**](NestedPrivateCategoryDepartment.md) |  | [optional] [readonly] 
**note** | **str** |  | [optional] 
**public_name** | **str** |  | [optional] 
**is_public_accessible** | **bool** |  | [optional] 
**configuration** | **object** |  | [optional] 
**icon** | **str** |  | [optional] 

## Example

```python
from signals_api_client.models.patched_private_category import PatchedPrivateCategory

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPrivateCategory from a JSON string
patched_private_category_instance = PatchedPrivateCategory.from_json(json)
# print the JSON string representation of the object
print(PatchedPrivateCategory.to_json())

# convert the object into a dict
patched_private_category_dict = patched_private_category_instance.to_dict()
# create an instance of PatchedPrivateCategory from a dict
patched_private_category_from_dict = PatchedPrivateCategory.from_dict(patched_private_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PrivateCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links2**](Links2.md) |  | 
**display** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**slug** | **str** |  | [readonly] 
**is_active** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**handling_message** | **str** |  | [optional] 
**sla** | **Dict[str, object]** |  | [readonly] 
**new_sla** | [**PrivateCategorySLA**](PrivateCategorySLA.md) |  | 
**departments** | [**List[NestedPrivateCategoryDepartment]**](NestedPrivateCategoryDepartment.md) |  | [readonly] 
**note** | **str** |  | [optional] 
**public_name** | **str** |  | [optional] 
**is_public_accessible** | **bool** |  | [optional] 
**configuration** | **object** |  | [optional] 
**icon** | **str** |  | [optional] 

## Example

```python
from signals_api_client.models.private_category import PrivateCategory

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateCategory from a JSON string
private_category_instance = PrivateCategory.from_json(json)
# print the JSON string representation of the object
print(PrivateCategory.to_json())

# convert the object into a dict
private_category_dict = private_category_instance.to_dict()
# create an instance of PrivateCategory from a dict
private_category_from_dict = PrivateCategory.from_dict(private_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TemporaryCategoryHAL

TODO: Refactor the TemporaryCategoryHALSerializer and TemporaryParentCategoryHALSerializer serializers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links1**](Links1.md) |  | 
**display** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**slug** | **str** |  | [readonly] 
**handling** | [**HandlingEnum**](HandlingEnum.md) |  | [optional] 
**departments** | [**List[NestedPublicDepartment]**](NestedPublicDepartment.md) |  | [readonly] 
**is_active** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**handling_message** | **str** |  | [optional] 

## Example

```python
from signals_api_client.models.temporary_category_hal import TemporaryCategoryHAL

# TODO update the JSON string below
json = "{}"
# create an instance of TemporaryCategoryHAL from a JSON string
temporary_category_hal_instance = TemporaryCategoryHAL.from_json(json)
# print the JSON string representation of the object
print(TemporaryCategoryHAL.to_json())

# convert the object into a dict
temporary_category_hal_dict = temporary_category_hal_instance.to_dict()
# create an instance of TemporaryCategoryHAL from a dict
temporary_category_hal_from_dict = TemporaryCategoryHAL.from_dict(temporary_category_hal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



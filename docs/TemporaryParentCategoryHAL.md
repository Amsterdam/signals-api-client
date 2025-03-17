# TemporaryParentCategoryHAL

SIG-2287 [BE] Afdeling geeft categorie zonder main slug terug  Added a TemporaryParentCategoryHALSerializer so that we can override the serializer_url_field to render the correct url for a parent category  TODO: Refactor the TemporaryCategoryHALSerializer and TemporaryParentCategoryHALSerializer serializers

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
from signals_api_client.models.temporary_parent_category_hal import TemporaryParentCategoryHAL

# TODO update the JSON string below
json = "{}"
# create an instance of TemporaryParentCategoryHAL from a JSON string
temporary_parent_category_hal_instance = TemporaryParentCategoryHAL.from_json(json)
# print the JSON string representation of the object
print(TemporaryParentCategoryHAL.to_json())

# convert the object into a dict
temporary_parent_category_hal_dict = temporary_parent_category_hal_instance.to_dict()
# create an instance of TemporaryParentCategoryHAL from a dict
temporary_parent_category_hal_from_dict = TemporaryParentCategoryHAL.from_dict(temporary_parent_category_hal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



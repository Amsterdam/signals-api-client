# PatchedUserDetailHAL

Serializer mixin to make fields only writeable at creation. When updating the field is set to read-only.  In the Meta data of the serializer just add tupple:  write_once_fields = (     '...',  # The name of the field you want to be write once )  or list:  write_once_fields = [     '...',  # The name of the field you want to be write once ]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links4**](Links4.md) |  | [optional] 
**display** | **str** |  | [optional] [readonly] 
**id** | **int** |  | [optional] [readonly] 
**username** | **str** | Vereist. 150 tekens of minder. Alleen letters, cijfers en de tekens @/,/+/-/_ zijn toegestaan. | [optional] [readonly] 
**email** | **str** |  | [optional] [readonly] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**is_active** | **bool** | Bepaalt of deze gebruiker als actief dient te worden behandeld. U kunt dit uitvinken in plaats van een gebruiker te verwijderen. | [optional] 
**is_staff** | **bool** | Bepaalt of de gebruiker zich op deze beheerwebsite kan aanmelden. | [optional] [readonly] 
**is_superuser** | **bool** | Bepaalt dat deze gebruiker alle rechten heeft, zonder deze expliciet toe te wijzen. | [optional] [readonly] 
**roles** | [**List[Role]**](Role.md) |  | [optional] [readonly] 
**role_ids** | **List[int]** |  | [optional] 
**permissions** | [**List[Permission]**](Permission.md) |  | [optional] [readonly] 
**profile** | [**ProfileDetail**](ProfileDetail.md) |  | [optional] 

## Example

```python
from signals_api_client.models.patched_user_detail_hal import PatchedUserDetailHAL

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedUserDetailHAL from a JSON string
patched_user_detail_hal_instance = PatchedUserDetailHAL.from_json(json)
# print the JSON string representation of the object
print(PatchedUserDetailHAL.to_json())

# convert the object into a dict
patched_user_detail_hal_dict = patched_user_detail_hal_instance.to_dict()
# create an instance of PatchedUserDetailHAL from a dict
patched_user_detail_hal_from_dict = PatchedUserDetailHAL.from_dict(patched_user_detail_hal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



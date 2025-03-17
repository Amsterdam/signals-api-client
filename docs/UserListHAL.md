# UserListHAL

Serializer mixin to make fields only writeable at creation. When updating the field is set to read-only.  In the Meta data of the serializer just add tupple:  write_once_fields = (     '...',  # The name of the field you want to be write once )  or list:  write_once_fields = [     '...',  # The name of the field you want to be write once ]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links3**](Links3.md) |  | 
**display** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**username** | **str** | Vereist. 150 tekens of minder. Alleen letters, cijfers en de tekens @/,/+/-/_ zijn toegestaan. | 
**is_active** | **bool** | Bepaalt of deze gebruiker als actief dient te worden behandeld. U kunt dit uitvinken in plaats van een gebruiker te verwijderen. | [optional] 
**roles** | **List[str]** |  | [readonly] 
**role_ids** | **List[int]** |  | [optional] 
**profile** | [**ProfileList**](ProfileList.md) |  | [optional] 

## Example

```python
from signals_api_client.models.user_list_hal import UserListHAL

# TODO update the JSON string below
json = "{}"
# create an instance of UserListHAL from a JSON string
user_list_hal_instance = UserListHAL.from_json(json)
# print the JSON string representation of the object
print(UserListHAL.to_json())

# convert the object into a dict
user_list_hal_dict = user_list_hal_instance.to_dict()
# create an instance of UserListHAL from a dict
user_list_hal_from_dict = UserListHAL.from_dict(user_list_hal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



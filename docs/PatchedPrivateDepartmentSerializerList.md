# PatchedPrivateDepartmentSerializerList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links3**](Links3.md) |  | [optional] 
**display** | **str** |  | [optional] [readonly] 
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**is_intern** | **bool** |  | [optional] 
**category_names** | **List[str]** |  | [optional] [readonly] 
**can_direct** | **bool** |  | [optional] 

## Example

```python
from signals_api_client.models.patched_private_department_serializer_list import PatchedPrivateDepartmentSerializerList

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPrivateDepartmentSerializerList from a JSON string
patched_private_department_serializer_list_instance = PatchedPrivateDepartmentSerializerList.from_json(json)
# print the JSON string representation of the object
print(PatchedPrivateDepartmentSerializerList.to_json())

# convert the object into a dict
patched_private_department_serializer_list_dict = patched_private_department_serializer_list_instance.to_dict()
# create an instance of PatchedPrivateDepartmentSerializerList from a dict
patched_private_department_serializer_list_from_dict = PatchedPrivateDepartmentSerializerList.from_dict(patched_private_department_serializer_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



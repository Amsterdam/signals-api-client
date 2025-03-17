# PatchedRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links3**](Links3.md) |  | [optional] 
**display** | **str** |  | [optional] [readonly] 
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**permissions** | [**List[Permission]**](Permission.md) |  | [optional] [readonly] 
**permission_ids** | **List[int]** |  | [optional] 

## Example

```python
from signals_api_client.models.patched_role import PatchedRole

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedRole from a JSON string
patched_role_instance = PatchedRole.from_json(json)
# print the JSON string representation of the object
print(PatchedRole.to_json())

# convert the object into a dict
patched_role_dict = patched_role_instance.to_dict()
# create an instance of PatchedRole from a dict
patched_role_from_dict = PatchedRole.from_dict(patched_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



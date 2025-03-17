# Role


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links3**](Links3.md) |  | 
**display** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**permissions** | [**List[Permission]**](Permission.md) |  | [readonly] 
**permission_ids** | **List[int]** |  | [optional] 

## Example

```python
from signals_api_client.models.role import Role

# TODO update the JSON string below
json = "{}"
# create an instance of Role from a JSON string
role_instance = Role.from_json(json)
# print the JSON string representation of the object
print(Role.to_json())

# convert the object into a dict
role_dict = role_instance.to_dict()
# create an instance of Role from a dict
role_from_dict = Role.from_dict(role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



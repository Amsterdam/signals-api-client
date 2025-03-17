# PrivateDepartmentSerializerList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links3**](Links3.md) |  | 
**display** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**code** | **str** |  | 
**is_intern** | **bool** |  | [optional] 
**category_names** | **List[str]** |  | [readonly] 
**can_direct** | **bool** |  | [optional] 

## Example

```python
from signals_api_client.models.private_department_serializer_list import PrivateDepartmentSerializerList

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateDepartmentSerializerList from a JSON string
private_department_serializer_list_instance = PrivateDepartmentSerializerList.from_json(json)
# print the JSON string representation of the object
print(PrivateDepartmentSerializerList.to_json())

# convert the object into a dict
private_department_serializer_list_dict = private_department_serializer_list_instance.to_dict()
# create an instance of PrivateDepartmentSerializerList from a dict
private_department_serializer_list_from_dict = PrivateDepartmentSerializerList.from_dict(private_department_serializer_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



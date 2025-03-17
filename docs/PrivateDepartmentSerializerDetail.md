# PrivateDepartmentSerializerDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links3**](Links3.md) |  | 
**display** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**code** | **str** |  | 
**is_intern** | **bool** |  | [optional] 
**categories** | [**List[CategoryDepartment]**](CategoryDepartment.md) |  | [optional] 
**can_direct** | **bool** |  | [optional] 

## Example

```python
from signals_api_client.models.private_department_serializer_detail import PrivateDepartmentSerializerDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateDepartmentSerializerDetail from a JSON string
private_department_serializer_detail_instance = PrivateDepartmentSerializerDetail.from_json(json)
# print the JSON string representation of the object
print(PrivateDepartmentSerializerDetail.to_json())

# convert the object into a dict
private_department_serializer_detail_dict = private_department_serializer_detail_instance.to_dict()
# create an instance of PrivateDepartmentSerializerDetail from a dict
private_department_serializer_detail_from_dict = PrivateDepartmentSerializerDetail.from_dict(private_department_serializer_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



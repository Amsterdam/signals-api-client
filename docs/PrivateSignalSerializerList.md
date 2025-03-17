# PrivateSignalSerializerList

This serializer is used for the list endpoint and when creating a new instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links**](Links.md) |  | 
**display** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**id_display** | **str** |  | [readonly] 
**signal_id** | **str** |  | [readonly] 
**source** | **str** |  | [optional] 
**text** | **str** |  | 
**text_extra** | **str** |  | [optional] 
**status** | [**NestedStatusModel**](NestedStatusModel.md) |  | [optional] 
**location** | [**NestedLocationModel**](NestedLocationModel.md) |  | 
**category** | [**NestedCategoryModel**](NestedCategoryModel.md) |  | 
**reporter** | [**NestedReporterModel**](NestedReporterModel.md) |  | 
**priority** | [**NestedPriorityModel**](NestedPriorityModel.md) |  | [optional] 
**type** | [**NestedTypeModel**](NestedTypeModel.md) |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**incident_date_start** | **datetime** |  | 
**incident_date_end** | **datetime** |  | [optional] 
**operational_date** | **datetime** |  | [optional] 
**has_attachments** | **str** |  | [readonly] 
**extra_properties** | **object** |  | [optional] 
**notes** | [**List[NestedNoteModel]**](NestedNoteModel.md) |  | [optional] 
**directing_departments** | [**List[NestedDepartmentModel]**](NestedDepartmentModel.md) |  | [optional] 
**routing_departments** | [**List[NestedDepartmentModel]**](NestedDepartmentModel.md) |  | [optional] 
**attachments** | **List[str]** |  | [optional] 
**parent** | **int** |  | [optional] 
**has_parent** | **str** |  | [readonly] 
**has_children** | **str** |  | [readonly] 
**assigned_user_email** | **str** |  | [optional] 
**session** | **str** |  | [optional] 

## Example

```python
from signals_api_client.models.private_signal_serializer_list import PrivateSignalSerializerList

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateSignalSerializerList from a JSON string
private_signal_serializer_list_instance = PrivateSignalSerializerList.from_json(json)
# print the JSON string representation of the object
print(PrivateSignalSerializerList.to_json())

# convert the object into a dict
private_signal_serializer_list_dict = private_signal_serializer_list_instance.to_dict()
# create an instance of PrivateSignalSerializerList from a dict
private_signal_serializer_list_from_dict = PrivateSignalSerializerList.from_dict(private_signal_serializer_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PatchedPrivateSignalSerializerList

This serializer is used for the list endpoint and when creating a new instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links**](Links.md) |  | [optional] 
**display** | **str** |  | [optional] [readonly] 
**id** | **int** |  | [optional] [readonly] 
**id_display** | **str** |  | [optional] [readonly] 
**signal_id** | **str** |  | [optional] [readonly] 
**source** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**text_extra** | **str** |  | [optional] 
**status** | [**NestedStatusModel**](NestedStatusModel.md) |  | [optional] 
**location** | [**NestedLocationModel**](NestedLocationModel.md) |  | [optional] 
**category** | [**NestedCategoryModel**](NestedCategoryModel.md) |  | [optional] 
**reporter** | [**NestedReporterModel**](NestedReporterModel.md) |  | [optional] 
**priority** | [**NestedPriorityModel**](NestedPriorityModel.md) |  | [optional] 
**type** | [**NestedTypeModel**](NestedTypeModel.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**incident_date_start** | **datetime** |  | [optional] 
**incident_date_end** | **datetime** |  | [optional] 
**operational_date** | **datetime** |  | [optional] 
**has_attachments** | **str** |  | [optional] [readonly] 
**extra_properties** | **object** |  | [optional] 
**notes** | [**List[NestedNoteModel]**](NestedNoteModel.md) |  | [optional] 
**directing_departments** | [**List[NestedDepartmentModel]**](NestedDepartmentModel.md) |  | [optional] 
**routing_departments** | [**List[NestedDepartmentModel]**](NestedDepartmentModel.md) |  | [optional] 
**attachments** | **List[str]** |  | [optional] 
**parent** | **int** |  | [optional] 
**has_parent** | **str** |  | [optional] [readonly] 
**has_children** | **str** |  | [optional] [readonly] 
**assigned_user_email** | **str** |  | [optional] 
**session** | **str** |  | [optional] 

## Example

```python
from signals_api_client.models.patched_private_signal_serializer_list import PatchedPrivateSignalSerializerList

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPrivateSignalSerializerList from a JSON string
patched_private_signal_serializer_list_instance = PatchedPrivateSignalSerializerList.from_json(json)
# print the JSON string representation of the object
print(PatchedPrivateSignalSerializerList.to_json())

# convert the object into a dict
patched_private_signal_serializer_list_dict = patched_private_signal_serializer_list_instance.to_dict()
# create an instance of PatchedPrivateSignalSerializerList from a dict
patched_private_signal_serializer_list_from_dict = PatchedPrivateSignalSerializerList.from_dict(patched_private_signal_serializer_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



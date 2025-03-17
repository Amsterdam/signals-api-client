# PrivateSignalSerializerDetail

This serializer is used for the detail endpoint and when updating the instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links6**](Links6.md) |  | 
**display** | **str** |  | [readonly] 
**category** | [**NestedCategoryModel**](NestedCategoryModel.md) |  | [optional] 
**id** | **int** |  | [readonly] 
**id_display** | **str** |  | [readonly] 
**has_attachments** | **str** |  | [readonly] 
**location** | [**NestedLocationModel**](NestedLocationModel.md) |  | [optional] 
**status** | [**NestedStatusModel**](NestedStatusModel.md) |  | [optional] 
**reporter** | [**NestedReporterModel**](NestedReporterModel.md) |  | [optional] 
**priority** | [**NestedPriorityModel**](NestedPriorityModel.md) |  | [optional] 
**notes** | [**List[NestedNoteModel]**](NestedNoteModel.md) |  | [optional] 
**type** | [**NestedTypeModel**](NestedTypeModel.md) |  | [optional] 
**source** | **str** |  | [optional] 
**text** | **str** |  | 
**text_extra** | **str** |  | [optional] 
**extra_properties** | **object** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**incident_date_start** | **datetime** |  | 
**incident_date_end** | **datetime** |  | [optional] 
**directing_departments** | [**List[NestedDepartmentModel]**](NestedDepartmentModel.md) |  | [optional] 
**routing_departments** | [**List[NestedDepartmentModel]**](NestedDepartmentModel.md) |  | [optional] 
**attachments** | **List[str]** |  | [readonly] 
**assigned_user_email** | **str** |  | [optional] 

## Example

```python
from signals_api_client.models.private_signal_serializer_detail import PrivateSignalSerializerDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateSignalSerializerDetail from a JSON string
private_signal_serializer_detail_instance = PrivateSignalSerializerDetail.from_json(json)
# print the JSON string representation of the object
print(PrivateSignalSerializerDetail.to_json())

# convert the object into a dict
private_signal_serializer_detail_dict = private_signal_serializer_detail_instance.to_dict()
# create an instance of PrivateSignalSerializerDetail from a dict
private_signal_serializer_detail_from_dict = PrivateSignalSerializerDetail.from_dict(private_signal_serializer_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



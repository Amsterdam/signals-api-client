# PublicQuestionSerializerDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**field_type** | [**FieldTypeEnum**](FieldTypeEnum.md) |  | 
**meta** | **object** |  | 
**required** | **bool** |  | 

## Example

```python
from signals_api_client.models.public_question_serializer_detail import PublicQuestionSerializerDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PublicQuestionSerializerDetail from a JSON string
public_question_serializer_detail_instance = PublicQuestionSerializerDetail.from_json(json)
# print the JSON string representation of the object
print(PublicQuestionSerializerDetail.to_json())

# convert the object into a dict
public_question_serializer_detail_dict = public_question_serializer_detail_instance.to_dict()
# create an instance of PublicQuestionSerializerDetail from a dict
public_question_serializer_detail_from_dict = PublicQuestionSerializerDetail.from_dict(public_question_serializer_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



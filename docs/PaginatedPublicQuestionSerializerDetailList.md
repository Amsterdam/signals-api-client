# PaginatedPublicQuestionSerializerDetailList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedAbridgedChildSignalListLinks**](PaginatedAbridgedChildSignalListLinks.md) |  | [optional] 
**count** | **int** |  | [optional] 
**results** | [**List[PublicQuestionSerializerDetail]**](PublicQuestionSerializerDetail.md) |  | [optional] 

## Example

```python
from signals_api_client.models.paginated_public_question_serializer_detail_list import PaginatedPublicQuestionSerializerDetailList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPublicQuestionSerializerDetailList from a JSON string
paginated_public_question_serializer_detail_list_instance = PaginatedPublicQuestionSerializerDetailList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPublicQuestionSerializerDetailList.to_json())

# convert the object into a dict
paginated_public_question_serializer_detail_list_dict = paginated_public_question_serializer_detail_list_instance.to_dict()
# create an instance of PaginatedPublicQuestionSerializerDetailList from a dict
paginated_public_question_serializer_detail_list_from_dict = PaginatedPublicQuestionSerializerDetailList.from_dict(paginated_public_question_serializer_detail_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



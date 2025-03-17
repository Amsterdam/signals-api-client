# PaginatedStandardAnswerList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedAbridgedChildSignalListLinks**](PaginatedAbridgedChildSignalListLinks.md) |  | [optional] 
**count** | **int** |  | [optional] 
**results** | [**List[StandardAnswer]**](StandardAnswer.md) |  | [optional] 

## Example

```python
from signals_api_client.models.paginated_standard_answer_list import PaginatedStandardAnswerList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedStandardAnswerList from a JSON string
paginated_standard_answer_list_instance = PaginatedStandardAnswerList.from_json(json)
# print the JSON string representation of the object
print(PaginatedStandardAnswerList.to_json())

# convert the object into a dict
paginated_standard_answer_list_dict = paginated_standard_answer_list_instance.to_dict()
# create an instance of PaginatedStandardAnswerList from a dict
paginated_standard_answer_list_from_dict = PaginatedStandardAnswerList.from_dict(paginated_standard_answer_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



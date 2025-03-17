# PaginatedExpressionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedAbridgedChildSignalListLinks**](PaginatedAbridgedChildSignalListLinks.md) |  | [optional] 
**count** | **int** |  | [optional] 
**results** | [**List[Expression]**](Expression.md) |  | [optional] 

## Example

```python
from signals_api_client.models.paginated_expression_list import PaginatedExpressionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedExpressionList from a JSON string
paginated_expression_list_instance = PaginatedExpressionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedExpressionList.to_json())

# convert the object into a dict
paginated_expression_list_dict = paginated_expression_list_instance.to_dict()
# create an instance of PaginatedExpressionList from a dict
paginated_expression_list_from_dict = PaginatedExpressionList.from_dict(paginated_expression_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



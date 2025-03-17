# PatchedExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**type** | **str** |  | [optional] [readonly] 
**routing_department** | [**RoutingExpression**](RoutingExpression.md) |  | [optional] 

## Example

```python
from signals_api_client.models.patched_expression import PatchedExpression

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedExpression from a JSON string
patched_expression_instance = PatchedExpression.from_json(json)
# print the JSON string representation of the object
print(PatchedExpression.to_json())

# convert the object into a dict
patched_expression_dict = patched_expression_instance.to_dict()
# create an instance of PatchedExpression from a dict
patched_expression_from_dict = PatchedExpression.from_dict(patched_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



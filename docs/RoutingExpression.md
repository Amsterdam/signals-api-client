# RoutingExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**department** | [**NestedDepartmentModel**](NestedDepartmentModel.md) |  | [optional] 
**order** | **int** |  | [optional] 

## Example

```python
from signals_api_client.models.routing_expression import RoutingExpression

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingExpression from a JSON string
routing_expression_instance = RoutingExpression.from_json(json)
# print the JSON string representation of the object
print(RoutingExpression.to_json())

# convert the object into a dict
routing_expression_dict = routing_expression_instance.to_dict()
# create an instance of RoutingExpression from a dict
routing_expression_from_dict = RoutingExpression.from_dict(routing_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



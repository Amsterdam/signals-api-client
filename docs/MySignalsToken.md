# MySignalsToken

Based on the AuthToken implementation of rest-framework

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 

## Example

```python
from signals_api_client.models.my_signals_token import MySignalsToken

# TODO update the JSON string below
json = "{}"
# create an instance of MySignalsToken from a JSON string
my_signals_token_instance = MySignalsToken.from_json(json)
# print the JSON string representation of the object
print(MySignalsToken.to_json())

# convert the object into a dict
my_signals_token_dict = my_signals_token_instance.to_dict()
# create an instance of MySignalsToken from a dict
my_signals_token_from_dict = MySignalsToken.from_dict(my_signals_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



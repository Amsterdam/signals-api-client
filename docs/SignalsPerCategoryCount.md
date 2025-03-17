# SignalsPerCategoryCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**SimpleCategory**](SimpleCategory.md) |  | [readonly] 
**signal_count** | **int** |  | 

## Example

```python
from signals_api_client.models.signals_per_category_count import SignalsPerCategoryCount

# TODO update the JSON string below
json = "{}"
# create an instance of SignalsPerCategoryCount from a JSON string
signals_per_category_count_instance = SignalsPerCategoryCount.from_json(json)
# print the JSON string representation of the object
print(SignalsPerCategoryCount.to_json())

# convert the object into a dict
signals_per_category_count_dict = signals_per_category_count_instance.to_dict()
# create an instance of SignalsPerCategoryCount from a dict
signals_per_category_count_from_dict = SignalsPerCategoryCount.from_dict(signals_per_category_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



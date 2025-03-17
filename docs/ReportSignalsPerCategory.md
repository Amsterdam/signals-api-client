# ReportSignalsPerCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_signal_count** | **int** |  | [readonly] 
**results** | [**SignalsPerCategoryCount**](SignalsPerCategoryCount.md) |  | [readonly] 

## Example

```python
from signals_api_client.models.report_signals_per_category import ReportSignalsPerCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ReportSignalsPerCategory from a JSON string
report_signals_per_category_instance = ReportSignalsPerCategory.from_json(json)
# print the JSON string representation of the object
print(ReportSignalsPerCategory.to_json())

# convert the object into a dict
report_signals_per_category_dict = report_signals_per_category_instance.to_dict()
# create an instance of ReportSignalsPerCategory from a dict
report_signals_per_category_from_dict = ReportSignalsPerCategory.from_dict(report_signals_per_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



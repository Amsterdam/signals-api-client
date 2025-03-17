# PaginatedSignalReporterList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedAbridgedChildSignalListLinks**](PaginatedAbridgedChildSignalListLinks.md) |  | [optional] 
**count** | **int** |  | [optional] 
**results** | [**List[SignalReporter]**](SignalReporter.md) |  | [optional] 

## Example

```python
from signals_api_client.models.paginated_signal_reporter_list import PaginatedSignalReporterList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSignalReporterList from a JSON string
paginated_signal_reporter_list_instance = PaginatedSignalReporterList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSignalReporterList.to_json())

# convert the object into a dict
paginated_signal_reporter_list_dict = paginated_signal_reporter_list_instance.to_dict()
# create an instance of PaginatedSignalReporterList from a dict
paginated_signal_reporter_list_from_dict = PaginatedSignalReporterList.from_dict(paginated_signal_reporter_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



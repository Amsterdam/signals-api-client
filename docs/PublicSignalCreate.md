# PublicSignalCreate

This serializer allows anonymous users to report `signals.Signals`.  Note: this is only used in the creation of new Signal instances, not to create the response body after a succesfull POST.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] [default to 'online']
**text** | **str** |  | 
**text_extra** | **str** |  | [optional] 
**location** | [**NestedLocationModel**](NestedLocationModel.md) |  | 
**category** | [**NestedCategoryModel**](NestedCategoryModel.md) |  | 
**reporter** | [**NestedReporterModel**](NestedReporterModel.md) |  | 
**incident_date_start** | **datetime** |  | 
**incident_date_end** | **datetime** |  | [optional] 
**extra_properties** | **object** |  | [optional] 
**session** | **str** |  | [optional] 

## Example

```python
from signals_api_client.models.public_signal_create import PublicSignalCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PublicSignalCreate from a JSON string
public_signal_create_instance = PublicSignalCreate.from_json(json)
# print the JSON string representation of the object
print(PublicSignalCreate.to_json())

# convert the object into a dict
public_signal_create_dict = public_signal_create_instance.to_dict()
# create an instance of PublicSignalCreate from a dict
public_signal_create_from_dict = PublicSignalCreate.from_dict(public_signal_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



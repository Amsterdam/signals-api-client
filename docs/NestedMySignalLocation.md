# NestedMySignalLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **object** |  | [readonly] 
**address_text** | **str** |  | [readonly] 
**geometrie** | [**NestedMySignalLocationGeometrie**](NestedMySignalLocationGeometrie.md) |  | 

## Example

```python
from signals_api_client.models.nested_my_signal_location import NestedMySignalLocation

# TODO update the JSON string below
json = "{}"
# create an instance of NestedMySignalLocation from a JSON string
nested_my_signal_location_instance = NestedMySignalLocation.from_json(json)
# print the JSON string representation of the object
print(NestedMySignalLocation.to_json())

# convert the object into a dict
nested_my_signal_location_dict = nested_my_signal_location_instance.to_dict()
# create an instance of NestedMySignalLocation from a dict
nested_my_signal_location_from_dict = NestedMySignalLocation.from_dict(nested_my_signal_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



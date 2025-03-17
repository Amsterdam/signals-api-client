# PublicSignalSerializerDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**id_display** | **str** |  | [readonly] 
**signal_id** | **str** |  | 
**status** | [**NestedPublicStatusModel**](NestedPublicStatusModel.md) |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**incident_date_start** | **datetime** |  | 
**incident_date_end** | **datetime** |  | [optional] 

## Example

```python
from signals_api_client.models.public_signal_serializer_detail import PublicSignalSerializerDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PublicSignalSerializerDetail from a JSON string
public_signal_serializer_detail_instance = PublicSignalSerializerDetail.from_json(json)
# print the JSON string representation of the object
print(PublicSignalSerializerDetail.to_json())

# convert the object into a dict
public_signal_serializer_detail_dict = public_signal_serializer_detail_instance.to_dict()
# create an instance of PublicSignalSerializerDetail from a dict
public_signal_serializer_detail_from_dict = PublicSignalSerializerDetail.from_dict(public_signal_serializer_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PaginatedPrivateSignalSerializerListList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedAbridgedChildSignalListLinks**](PaginatedAbridgedChildSignalListLinks.md) |  | [optional] 
**count** | **int** |  | [optional] 
**results** | [**List[PrivateSignalSerializerList]**](PrivateSignalSerializerList.md) |  | [optional] 

## Example

```python
from signals_api_client.models.paginated_private_signal_serializer_list_list import PaginatedPrivateSignalSerializerListList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPrivateSignalSerializerListList from a JSON string
paginated_private_signal_serializer_list_list_instance = PaginatedPrivateSignalSerializerListList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPrivateSignalSerializerListList.to_json())

# convert the object into a dict
paginated_private_signal_serializer_list_list_dict = paginated_private_signal_serializer_list_list_instance.to_dict()
# create an instance of PaginatedPrivateSignalSerializerListList from a dict
paginated_private_signal_serializer_list_list_from_dict = PaginatedPrivateSignalSerializerListList.from_dict(paginated_private_signal_serializer_list_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PaginatedAbridgedChildSignalListLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**PaginatedAbridgedChildSignalListLinksSelf**](PaginatedAbridgedChildSignalListLinksSelf.md) |  | [optional] 
**next** | [**PaginatedAbridgedChildSignalListLinksNext**](PaginatedAbridgedChildSignalListLinksNext.md) |  | [optional] 
**previous** | [**PaginatedAbridgedChildSignalListLinksPrevious**](PaginatedAbridgedChildSignalListLinksPrevious.md) |  | [optional] 

## Example

```python
from signals_api_client.models.paginated_abridged_child_signal_list_links import PaginatedAbridgedChildSignalListLinks

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAbridgedChildSignalListLinks from a JSON string
paginated_abridged_child_signal_list_links_instance = PaginatedAbridgedChildSignalListLinks.from_json(json)
# print the JSON string representation of the object
print(PaginatedAbridgedChildSignalListLinks.to_json())

# convert the object into a dict
paginated_abridged_child_signal_list_links_dict = paginated_abridged_child_signal_list_links_instance.to_dict()
# create an instance of PaginatedAbridgedChildSignalListLinks from a dict
paginated_abridged_child_signal_list_links_from_dict = PaginatedAbridgedChildSignalListLinks.from_dict(paginated_abridged_child_signal_list_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



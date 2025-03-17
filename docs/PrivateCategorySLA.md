# PrivateCategorySLA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**n_days** | **int** |  | 
**use_calendar_days** | **bool** | * &#x60;True&#x60; - Kalender dagen * &#x60;False&#x60; - Werk dagen | [optional] 

## Example

```python
from signals_api_client.models.private_category_sla import PrivateCategorySLA

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateCategorySLA from a JSON string
private_category_sla_instance = PrivateCategorySLA.from_json(json)
# print the JSON string representation of the object
print(PrivateCategorySLA.to_json())

# convert the object into a dict
private_category_sla_dict = private_category_sla_instance.to_dict()
# create an instance of PrivateCategorySLA from a dict
private_category_sla_from_dict = PrivateCategorySLA.from_dict(private_category_sla_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



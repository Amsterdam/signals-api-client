# ProfileList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** |  | [optional] 
**departments** | **List[str]** |  | [readonly] 
**department_ids** | **List[int]** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from signals_api_client.models.profile_list import ProfileList

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileList from a JSON string
profile_list_instance = ProfileList.from_json(json)
# print the JSON string representation of the object
print(ProfileList.to_json())

# convert the object into a dict
profile_list_dict = profile_list_instance.to_dict()
# create an instance of ProfileList from a dict
profile_list_from_dict = ProfileList.from_dict(profile_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



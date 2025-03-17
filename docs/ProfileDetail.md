# ProfileDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** |  | [optional] 
**departments** | **List[str]** |  | [readonly] 
**department_ids** | **List[int]** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**notification_on_user_assignment** | **bool** |  | [optional] 
**notification_on_department_assignment** | **bool** |  | [optional] 

## Example

```python
from signals_api_client.models.profile_detail import ProfileDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileDetail from a JSON string
profile_detail_instance = ProfileDetail.from_json(json)
# print the JSON string representation of the object
print(ProfileDetail.to_json())

# convert the object into a dict
profile_detail_dict = profile_detail_instance.to_dict()
# create an instance of ProfileDetail from a dict
profile_detail_from_dict = ProfileDetail.from_dict(profile_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



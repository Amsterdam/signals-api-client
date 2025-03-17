# UserNameList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Vereist. 150 tekens of minder. Alleen letters, cijfers en de tekens @/,/+/-/_ zijn toegestaan. | 

## Example

```python
from signals_api_client.models.user_name_list import UserNameList

# TODO update the JSON string below
json = "{}"
# create an instance of UserNameList from a JSON string
user_name_list_instance = UserNameList.from_json(json)
# print the JSON string representation of the object
print(UserNameList.to_json())

# convert the object into a dict
user_name_list_dict = user_name_list_instance.to_dict()
# create an instance of UserNameList from a dict
user_name_list_from_dict = UserNameList.from_dict(user_name_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



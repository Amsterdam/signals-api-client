# TmpCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links1**](Links1.md) |  | 
**display** | **str** |  | [readonly] 
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**slug** | **str** |  | [readonly] 
**handling** | [**HandlingEnum**](HandlingEnum.md) |  | [optional] 
**departments** | [**List[NestedPublicDepartment]**](NestedPublicDepartment.md) |  | [readonly] 
**is_active** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**handling_message** | **str** |  | [optional] 

## Example

```python
from signals_api_client.models.tmp_category import TmpCategory

# TODO update the JSON string below
json = "{}"
# create an instance of TmpCategory from a JSON string
tmp_category_instance = TmpCategory.from_json(json)
# print the JSON string representation of the object
print(TmpCategory.to_json())

# convert the object into a dict
tmp_category_dict = tmp_category_instance.to_dict()
# create an instance of TmpCategory from a dict
tmp_category_from_dict = TmpCategory.from_dict(tmp_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



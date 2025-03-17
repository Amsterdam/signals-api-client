# SimpleCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**departments** | **List[str]** |  | [readonly] 

## Example

```python
from signals_api_client.models.simple_category import SimpleCategory

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleCategory from a JSON string
simple_category_instance = SimpleCategory.from_json(json)
# print the JSON string representation of the object
print(SimpleCategory.to_json())

# convert the object into a dict
simple_category_dict = simple_category_instance.to_dict()
# create an instance of SimpleCategory from a dict
simple_category_from_dict = SimpleCategory.from_dict(simple_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



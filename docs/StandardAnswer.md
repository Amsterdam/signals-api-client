# StandardAnswer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_satisfied** | **bool** |  | [optional] 
**text** | **str** |  | 
**topic** | **str** |  | [readonly] 
**open_answer** | **bool** | Als deze optie is aangevinkt, dan wordt een open antwoord verwacht van de melder en is de opgegeven tekst een default waarde. De melding krijgt bij deze optie automatisch de status verzoek tot heropenen. | [optional] 

## Example

```python
from signals_api_client.models.standard_answer import StandardAnswer

# TODO update the JSON string below
json = "{}"
# create an instance of StandardAnswer from a JSON string
standard_answer_instance = StandardAnswer.from_json(json)
# print the JSON string representation of the object
print(StandardAnswer.to_json())

# convert the object into a dict
standard_answer_dict = standard_answer_instance.to_dict()
# create an instance of StandardAnswer from a dict
standard_answer_from_dict = StandardAnswer.from_dict(standard_answer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



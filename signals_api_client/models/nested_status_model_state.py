# coding: utf-8

"""
    Signalen API

    One of the tasks of a municipality is to maintain public spaces. When citizens have complaints about public spaces they can leave these complaints with the municipality. Signalen (SIG) receives these complaints and is used to track progress towards their resolution. SIG provides an API that is used both by the SIG frontend and external systems that integrate with SIG.

    The version of the OpenAPI document: 2.41.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from signals_api_client.models.blank_enum import BlankEnum
from signals_api_client.models.state_a07_enum import StateA07Enum
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

NESTEDSTATUSMODELSTATE_ONE_OF_SCHEMAS = ["BlankEnum", "StateA07Enum"]

class NestedStatusModelState(BaseModel):
    """
    Melding status  * `m` - Gemeld * `i` - In afwachting van behandeling * `b` - In behandeling * `h` - On hold * `ingepland` - Ingepland * `ready to send` - Extern: te verzenden * `o` - Afgehandeld * `a` - Geannuleerd * `reopened` - Heropend * `s` - Gesplitst * `closure requested` - Extern: verzoek tot afhandeling * `reaction requested` - Reactie gevraagd * `reaction received` - Reactie ontvangen * `forward to external` - Doorgezet naar extern * `sent` - Extern: verzonden * `send failed` - Extern: mislukt * `done external` - Extern: afgehandeld * `reopen requested` - Verzoek tot heropenen
    """
    # data type: StateA07Enum
    oneof_schema_1_validator: Optional[StateA07Enum] = None
    # data type: BlankEnum
    oneof_schema_2_validator: Optional[BlankEnum] = None
    actual_instance: Optional[Union[BlankEnum, StateA07Enum]] = None
    one_of_schemas: Set[str] = { "BlankEnum", "StateA07Enum" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = NestedStatusModelState.model_construct()
        error_messages = []
        match = 0
        # validate data type: StateA07Enum
        if not isinstance(v, StateA07Enum):
            error_messages.append(f"Error! Input type `{type(v)}` is not `StateA07Enum`")
        else:
            match += 1
        # validate data type: BlankEnum
        if not isinstance(v, BlankEnum):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BlankEnum`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in NestedStatusModelState with oneOf schemas: BlankEnum, StateA07Enum. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in NestedStatusModelState with oneOf schemas: BlankEnum, StateA07Enum. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into StateA07Enum
        try:
            instance.actual_instance = StateA07Enum.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BlankEnum
        try:
            instance.actual_instance = BlankEnum.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into NestedStatusModelState with oneOf schemas: BlankEnum, StateA07Enum. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into NestedStatusModelState with oneOf schemas: BlankEnum, StateA07Enum. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], BlankEnum, StateA07Enum]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())



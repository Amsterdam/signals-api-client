# coding: utf-8

"""
    Signalen API

    One of the tasks of a municipality is to maintain public spaces. When citizens have complaints about public spaces they can leave these complaints with the municipality. Signalen (SIG) receives these complaints and is used to track progress towards their resolution. SIG provides an API that is used both by the SIG frontend and external systems that integrate with SIG.

    The version of the OpenAPI document: 2.41.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PatchedStoredSignalFilter(BaseModel):
    """
    PatchedStoredSignalFilter
    """ # noqa: E501
    links: Optional[StrictStr] = Field(default=None, alias="_links")
    display: Optional[StrictStr] = Field(default=None, alias="_display")
    id: Optional[StrictInt] = None
    name: Optional[Annotated[str, Field(strict=True, max_length=10000)]] = None
    created_at: Optional[datetime] = None
    options: Optional[Any] = None
    refresh: Optional[StrictBool] = None
    show_on_overview: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["_links", "_display", "id", "name", "created_at", "options", "refresh", "show_on_overview"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PatchedStoredSignalFilter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "links",
            "display",
            "id",
            "created_at",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if options (nullable) is None
        # and model_fields_set contains the field
        if self.options is None and "options" in self.model_fields_set:
            _dict['options'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchedStoredSignalFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_links": obj.get("_links"),
            "_display": obj.get("_display"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "created_at": obj.get("created_at"),
            "options": obj.get("options"),
            "refresh": obj.get("refresh"),
            "show_on_overview": obj.get("show_on_overview")
        })
        return _obj



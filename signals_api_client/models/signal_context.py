# coding: utf-8

"""
    Signalen API

    One of the tasks of a municipality is to maintain public spaces. When citizens have complaints about public spaces they can leave these complaints with the municipality. Signalen (SIG) receives these complaints and is used to track progress towards their resolution. SIG provides an API that is used both by the SIG frontend and external systems that integrate with SIG.

    The version of the OpenAPI document: 2.41.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from signals_api_client.models.links7 import Links7
from signals_api_client.models.signal_context_near import SignalContextNear
from signals_api_client.models.signal_context_reporter import SignalContextReporter
from typing import Optional, Set
from typing_extensions import Self

class SignalContext(BaseModel):
    """
    SignalContext
    """ # noqa: E501
    links: Links7 = Field(alias="_links")
    near: SignalContextNear
    reporter: Optional[SignalContextReporter]
    __properties: ClassVar[List[str]] = ["_links", "near", "reporter"]

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
        """Create an instance of SignalContext from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of near
        if self.near:
            _dict['near'] = self.near.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reporter
        if self.reporter:
            _dict['reporter'] = self.reporter.to_dict()
        # set to None if reporter (nullable) is None
        # and model_fields_set contains the field
        if self.reporter is None and "reporter" in self.model_fields_set:
            _dict['reporter'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SignalContext from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_links": Links7.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "near": SignalContextNear.from_dict(obj["near"]) if obj.get("near") is not None else None,
            "reporter": SignalContextReporter.from_dict(obj["reporter"]) if obj.get("reporter") is not None else None
        })
        return _obj



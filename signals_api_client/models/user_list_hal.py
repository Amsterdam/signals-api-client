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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from signals_api_client.models.links3 import Links3
from signals_api_client.models.profile_list import ProfileList
from typing import Optional, Set
from typing_extensions import Self

class UserListHAL(BaseModel):
    """
    Serializer mixin to make fields only writeable at creation. When updating the field is set to read-only.  In the Meta data of the serializer just add tupple:  write_once_fields = (     '...',  # The name of the field you want to be write once )  or list:  write_once_fields = [     '...',  # The name of the field you want to be write once ]
    """ # noqa: E501
    links: Links3 = Field(alias="_links")
    display: StrictStr = Field(alias="_display")
    id: StrictInt
    username: Annotated[str, Field(strict=True, max_length=150)] = Field(description="Vereist. 150 tekens of minder. Alleen letters, cijfers en de tekens @/,/+/-/_ zijn toegestaan.")
    is_active: Optional[StrictBool] = Field(default=None, description="Bepaalt of deze gebruiker als actief dient te worden behandeld. U kunt dit uitvinken in plaats van een gebruiker te verwijderen.")
    roles: List[StrictStr]
    role_ids: Optional[List[StrictInt]] = None
    profile: Optional[ProfileList] = None
    __properties: ClassVar[List[str]] = ["_links", "_display", "id", "username", "is_active", "roles", "role_ids", "profile"]

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
        """Create an instance of UserListHAL from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "display",
            "id",
            "roles",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of profile
        if self.profile:
            _dict['profile'] = self.profile.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserListHAL from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_links": Links3.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "_display": obj.get("_display"),
            "id": obj.get("id"),
            "username": obj.get("username"),
            "is_active": obj.get("is_active"),
            "roles": obj.get("roles"),
            "role_ids": obj.get("role_ids"),
            "profile": ProfileList.from_dict(obj["profile"]) if obj.get("profile") is not None else None
        })
        return _obj



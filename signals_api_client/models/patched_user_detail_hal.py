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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from signals_api_client.models.links4 import Links4
from signals_api_client.models.permission import Permission
from signals_api_client.models.profile_detail import ProfileDetail
from signals_api_client.models.role import Role
from typing import Optional, Set
from typing_extensions import Self

class PatchedUserDetailHAL(BaseModel):
    """
    Serializer mixin to make fields only writeable at creation. When updating the field is set to read-only.  In the Meta data of the serializer just add tupple:  write_once_fields = (     '...',  # The name of the field you want to be write once )  or list:  write_once_fields = [     '...',  # The name of the field you want to be write once ]
    """ # noqa: E501
    links: Optional[Links4] = Field(default=None, alias="_links")
    display: Optional[StrictStr] = Field(default=None, alias="_display")
    id: Optional[StrictInt] = None
    username: Optional[StrictStr] = Field(default=None, description="Vereist. 150 tekens of minder. Alleen letters, cijfers en de tekens @/,/+/-/_ zijn toegestaan.")
    email: Optional[StrictStr] = None
    first_name: Optional[Annotated[str, Field(strict=True, max_length=150)]] = None
    last_name: Optional[Annotated[str, Field(strict=True, max_length=150)]] = None
    is_active: Optional[StrictBool] = Field(default=None, description="Bepaalt of deze gebruiker als actief dient te worden behandeld. U kunt dit uitvinken in plaats van een gebruiker te verwijderen.")
    is_staff: Optional[StrictBool] = Field(default=None, description="Bepaalt of de gebruiker zich op deze beheerwebsite kan aanmelden.")
    is_superuser: Optional[StrictBool] = Field(default=None, description="Bepaalt dat deze gebruiker alle rechten heeft, zonder deze expliciet toe te wijzen.")
    roles: Optional[List[Role]] = None
    role_ids: Optional[List[StrictInt]] = None
    permissions: Optional[List[Permission]] = None
    profile: Optional[ProfileDetail] = None
    __properties: ClassVar[List[str]] = ["_links", "_display", "id", "username", "email", "first_name", "last_name", "is_active", "is_staff", "is_superuser", "roles", "role_ids", "permissions", "profile"]

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
        """Create an instance of PatchedUserDetailHAL from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "display",
            "id",
            "username",
            "email",
            "is_staff",
            "is_superuser",
            "roles",
            "permissions",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in roles (list)
        _items = []
        if self.roles:
            for _item_roles in self.roles:
                if _item_roles:
                    _items.append(_item_roles.to_dict())
            _dict['roles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in permissions (list)
        _items = []
        if self.permissions:
            for _item_permissions in self.permissions:
                if _item_permissions:
                    _items.append(_item_permissions.to_dict())
            _dict['permissions'] = _items
        # override the default output from pydantic by calling `to_dict()` of profile
        if self.profile:
            _dict['profile'] = self.profile.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchedUserDetailHAL from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_links": Links4.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "_display": obj.get("_display"),
            "id": obj.get("id"),
            "username": obj.get("username"),
            "email": obj.get("email"),
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "is_active": obj.get("is_active"),
            "is_staff": obj.get("is_staff"),
            "is_superuser": obj.get("is_superuser"),
            "roles": [Role.from_dict(_item) for _item in obj["roles"]] if obj.get("roles") is not None else None,
            "role_ids": obj.get("role_ids"),
            "permissions": [Permission.from_dict(_item) for _item in obj["permissions"]] if obj.get("permissions") is not None else None,
            "profile": ProfileDetail.from_dict(obj["profile"]) if obj.get("profile") is not None else None
        })
        return _obj



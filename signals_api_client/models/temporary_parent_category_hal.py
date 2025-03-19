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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from signals_api_client.models.handling_enum import HandlingEnum
from signals_api_client.models.links1 import Links1
from signals_api_client.models.nested_public_department import NestedPublicDepartment
from typing import Optional, Set
from typing_extensions import Self

class TemporaryParentCategoryHAL(BaseModel):
    """
    SIG-2287 [BE] Afdeling geeft categorie zonder main slug terug  Added a TemporaryParentCategoryHALSerializer so that we can override the serializer_url_field to render the correct url for a parent category  TODO: Refactor the TemporaryCategoryHALSerializer and TemporaryParentCategoryHALSerializer serializers
    """ # noqa: E501
    links: Links1 = Field(alias="_links")
    display: StrictStr = Field(alias="_display")
    id: StrictInt
    name: Annotated[str, Field(strict=True, max_length=255)]
    slug: Annotated[str, Field(strict=True)]
    handling: Optional[HandlingEnum] = None
    departments: List[NestedPublicDepartment]
    is_active: Optional[StrictBool] = None
    description: Optional[StrictStr] = None
    handling_message: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["_links", "_display", "id", "name", "slug", "handling", "departments", "is_active", "description", "handling_message"]

    @field_validator('slug')
    def slug_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[-a-zA-Z0-9_]+$", value):
            raise ValueError(r"must validate the regular expression /^[-a-zA-Z0-9_]+$/")
        return value

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
        """Create an instance of TemporaryParentCategoryHAL from a JSON string"""
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
            "display",
            "id",
            "slug",
            "departments",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in departments (list)
        _items = []
        if self.departments:
            for _item_departments in self.departments:
                if _item_departments:
                    _items.append(_item_departments.to_dict())
            _dict['departments'] = _items
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if handling_message (nullable) is None
        # and model_fields_set contains the field
        if self.handling_message is None and "handling_message" in self.model_fields_set:
            _dict['handling_message'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TemporaryParentCategoryHAL from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_links": Links1.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "_display": obj.get("_display"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "slug": obj.get("slug"),
            "handling": obj.get("handling"),
            "departments": [NestedPublicDepartment.from_dict(_item) for _item in obj["departments"]] if obj.get("departments") is not None else None,
            "is_active": obj.get("is_active"),
            "description": obj.get("description"),
            "handling_message": obj.get("handling_message")
        })
        return _obj



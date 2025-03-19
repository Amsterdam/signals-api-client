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
from signals_api_client.models.category_department import CategoryDepartment
from signals_api_client.models.links3 import Links3
from typing import Optional, Set
from typing_extensions import Self

class PrivateDepartmentSerializerDetail(BaseModel):
    """
    PrivateDepartmentSerializerDetail
    """ # noqa: E501
    links: Links3 = Field(alias="_links")
    display: StrictStr = Field(alias="_display")
    id: StrictInt
    name: Annotated[str, Field(strict=True, max_length=255)]
    code: Annotated[str, Field(strict=True, max_length=3)]
    is_intern: Optional[StrictBool] = None
    categories: Optional[List[CategoryDepartment]] = None
    can_direct: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["_links", "_display", "id", "name", "code", "is_intern", "categories", "can_direct"]

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
        """Create an instance of PrivateDepartmentSerializerDetail from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "display",
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in categories (list)
        _items = []
        if self.categories:
            for _item_categories in self.categories:
                if _item_categories:
                    _items.append(_item_categories.to_dict())
            _dict['categories'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PrivateDepartmentSerializerDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_links": Links3.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "_display": obj.get("_display"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "code": obj.get("code"),
            "is_intern": obj.get("is_intern"),
            "categories": [CategoryDepartment.from_dict(_item) for _item in obj["categories"]] if obj.get("categories") is not None else None,
            "can_direct": obj.get("can_direct")
        })
        return _obj



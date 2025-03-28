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
from enum import Enum
from typing_extensions import Self


class BlankEnum(str, Enum):
    """
    BlankEnum
    """

    """
    allowed enum values
    """
    EMPTY = ''

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of BlankEnum from a JSON string"""
        return cls(json.loads(json_str))



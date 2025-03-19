# coding: utf-8

"""
    Signalen API

    One of the tasks of a municipality is to maintain public spaces. When citizens have complaints about public spaces they can leave these complaints with the municipality. Signalen (SIG) receives these complaints and is used to track progress towards their resolution. SIG provides an API that is used both by the SIG frontend and external systems that integrate with SIG.

    The version of the OpenAPI document: 2.41.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class StatusEnum(str, Enum):
    """
    * `m` - Gemeld * `i` - In afwachting van behandeling * `b` - In behandeling * `h` - On hold * `ingepland` - Ingepland * `ready to send` - Extern: te verzenden * `o` - Afgehandeld * `a` - Geannuleerd * `reopened` - Heropend * `s` - Gesplitst * `closure requested` - Extern: verzoek tot afhandeling * `reaction requested` - Reactie gevraagd * `reaction received` - Reactie ontvangen * `forward to external` - Doorgezet naar extern * `sent` - Extern: verzonden * `send failed` - Extern: mislukt * `done external` - Extern: afgehandeld * `reopen requested` - Verzoek tot heropenen
    """

    """
    allowed enum values
    """
    M = 'm'
    I = 'i'
    B = 'b'
    H = 'h'
    INGEPLAND = 'ingepland'
    READY_TO_SEND = 'ready to send'
    O = 'o'
    A = 'a'
    REOPENED = 'reopened'
    S = 's'
    CLOSURE_REQUESTED = 'closure requested'
    REACTION_REQUESTED = 'reaction requested'
    REACTION_RECEIVED = 'reaction received'
    FORWARD_TO_EXTERNAL = 'forward to external'
    SENT = 'sent'
    SEND_FAILED = 'send failed'
    DONE_EXTERNAL = 'done external'
    REOPEN_REQUESTED = 'reopen requested'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of StatusEnum from a JSON string"""
        return cls(json.loads(json_str))



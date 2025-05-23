"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .asyncresponse import AsyncResponse, AsyncResponseTypedDict
from .asyncwebhookresponse import AsyncWebhookResponse, AsyncWebhookResponseTypedDict
from typing import Union
from typing_extensions import TypeAliasType


ResponseProCannyV1FluxPro10CannyPostTypedDict = TypeAliasType(
    "ResponseProCannyV1FluxPro10CannyPostTypedDict",
    Union[AsyncResponseTypedDict, AsyncWebhookResponseTypedDict],
)
r"""Successful Response"""


ResponseProCannyV1FluxPro10CannyPost = TypeAliasType(
    "ResponseProCannyV1FluxPro10CannyPost", Union[AsyncResponse, AsyncWebhookResponse]
)
r"""Successful Response"""

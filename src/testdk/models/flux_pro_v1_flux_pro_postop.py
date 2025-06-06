"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .asyncresponse import AsyncResponse, AsyncResponseTypedDict
from .asyncwebhookresponse import AsyncWebhookResponse, AsyncWebhookResponseTypedDict
from typing import Union
from typing_extensions import TypeAliasType


ResponseFluxProV1FluxProPostTypedDict = TypeAliasType(
    "ResponseFluxProV1FluxProPostTypedDict",
    Union[AsyncResponseTypedDict, AsyncWebhookResponseTypedDict],
)
r"""Successful Response"""


ResponseFluxProV1FluxProPost = TypeAliasType(
    "ResponseFluxProV1FluxProPost", Union[AsyncResponse, AsyncWebhookResponse]
)
r"""Successful Response"""

"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from testdk.types import BaseModel
from typing_extensions import TypedDict


class AsyncWebhookResponseTypedDict(TypedDict):
    id: str
    status: str
    webhook_url: str


class AsyncWebhookResponse(BaseModel):
    id: str

    status: str

    webhook_url: str

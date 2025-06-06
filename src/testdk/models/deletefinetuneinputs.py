"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from testdk.types import BaseModel
from typing_extensions import TypedDict


class DeleteFinetuneInputsTypedDict(TypedDict):
    finetune_id: str
    r"""ID of the fine-tuned model you want to delete."""


class DeleteFinetuneInputs(BaseModel):
    finetune_id: str
    r"""ID of the fine-tuned model you want to delete."""

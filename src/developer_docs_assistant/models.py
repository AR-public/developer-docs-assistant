"""Validated data models used by the Developer Docs Assistant."""

from pydantic import BaseModel, ConfigDict, Field


class AskRequest(BaseModel):
    """A question accepted at the assistant's input boundary."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    question: str = Field(
        min_length=1,
        max_length=2_000,
        description="A developer documentation question.",
    )

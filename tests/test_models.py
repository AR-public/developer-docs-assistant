"""Tests for the request-validation boundary."""

import pytest
from pydantic import ValidationError

from developer_docs_assistant.models import AskRequest


def test_request_strips_surrounding_whitespace() -> None:
    request = AskRequest(question="  Where is the API guide?  ")

    assert request.question == "Where is the API guide?"


@pytest.mark.parametrize(
    "question",
    ("", "   ", "x" * 2_001),
    ids=("empty", "whitespace-only", "too-long"),
)
def test_request_rejects_invalid_question(question: str) -> None:
    with pytest.raises(ValidationError):
        AskRequest(question=question)


def test_request_rejects_unexpected_fields() -> None:
    with pytest.raises(ValidationError):
        AskRequest.model_validate({"question": "Where is the API guide?", "extra": True})

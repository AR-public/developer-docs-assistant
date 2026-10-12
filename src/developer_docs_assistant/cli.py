"""Command-line entry point for validating assistant requests."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence

from pydantic import ValidationError

from developer_docs_assistant.models import AskRequest


def main(argv: Sequence[str] | None = None) -> int:
    """Validate a question supplied on the command line."""
    parser = argparse.ArgumentParser(description="Validate a Developer Docs Assistant question.")
    parser.add_argument("question", help="Question to validate.")
    args = parser.parse_args(argv)

    try:
        AskRequest(question=args.question)
    except ValidationError as error:
        for issue in error.errors():
            location = ".".join(str(part) for part in issue["loc"])
            print(f"{location}: {issue['msg']}", file=sys.stderr)
        return 2

    print("Request validated. No model call was made (Lesson 1 foundation only).")
    return 0

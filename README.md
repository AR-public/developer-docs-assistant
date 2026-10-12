# Developer Docs Assistant

Lesson 1 foundation for a Python developer documentation assistant capstone.

This is a small, reproducible Python package that will grow into the course
capstone. This repository is the **Lesson 1 checkpoint**.

## Lesson 1 checkpoint

At this stage the app accepts a question, validates its shape, and reports
whether it is valid. It does **not** call a language model, search documentation,
or claim to answer questions. Keeping that boundary explicit gives us something
small and testable before adding model behavior in Lesson 2.

No API key, network access, or external service is required.

## Requirements

- [uv](https://docs.astral.sh/uv/) for Python version selection, environments,
  dependencies, locking, and command execution
- Python 3.11 or newer (the project selects Python 3.11 through `.python-version`)

## Set up the project

From this directory, run:

```powershell
uv sync --locked
```

This creates the local `.venv` if needed and installs the exact dependency
versions recorded in `uv.lock`, including the development tools. Keep
`pyproject.toml` and `uv.lock` together so another checkout can reproduce the
environment.

## Try the command-line app

Pass a question as one quoted argument:

```powershell
uv run developer-docs-assistant "Where do I configure API authentication?"
```

Expected output:

```text
Request validated. No model call was made (Lesson 1 foundation only).
```

The same entry point is available as a Python module:

```powershell
uv run python -m developer_docs_assistant "Where do I configure API authentication?"
```

The Pydantic request model trims surrounding whitespace, requires a question
between 1 and 2,000 characters, and rejects unexpected fields in structured
input. The command-line interface currently accepts one positional question.
For example:

```powershell
uv run developer-docs-assistant "   "
```

Validation details are written to standard error and the command exits with
status `2`; valid input exits with status `0`. Use `--help` to see the command
usage:

```powershell
uv run developer-docs-assistant --help
```

## Run the checks

Run these from the project directory:

```powershell
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv build
```

To apply Ruff formatting after editing:

```powershell
uv run ruff format .
```

`uv build` uses Hatchling to create the source distribution and wheel in
`dist/`. The build outputs and local caches are ignored by Git.

## Project layout

```text
.
|-- pyproject.toml
|-- uv.lock
|-- src/
|   `-- developer_docs_assistant/
|       |-- __init__.py
|       |-- __main__.py
|       |-- cli.py
|       `-- models.py
`-- tests/
    |-- test_cli.py
    `-- test_models.py
```

- `models.py` defines the Pydantic `AskRequest` boundary.
- `cli.py` validates one question and reports errors without echoing the
  question back to the terminal.
- `__main__.py` supports `python -m developer_docs_assistant`.
- `tests/` covers successful normalization, invalid input, and CLI behavior.

## What each tool is responsible for

| Tool | Responsibility in this checkpoint |
| --- | --- |
| uv | Select Python, create the environment, resolve and lock dependencies, and run project commands |
| Pydantic | Validate request data at runtime; Python type hints alone do not validate input |
| pytest | Exercise the request model and command-line behavior |
| Ruff | Check Python style and apply consistent formatting |
| Hatchling | Build the distributable Python package |

These tools solve different problems; for example, Hatchling is the build
backend, while uv manages the project workflow.

## Continue with Lesson 2

After the checks above pass, continue with **Lesson 2: Foundation models and
APIs** in the course workspace. Keep this request-validation boundary and add
the lesson's model interface and deterministic fake implementation as a
separate increment. That lets later tests exercise the assistant flow without
requiring credentials or a live provider.

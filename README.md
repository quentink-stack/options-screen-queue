# options-screen-queue

## Summary
This project is intended to be used as an elementary tool to design basic options trading strategies (simple calls and puts).
The strategy can then be backtested.

Prerequisite
- Poetry (used for dependency and environment management). Install from https://python-poetry.org/docs/#installation or run:

```bash
curl -sSL https://install.python-poetry.org | python -
```

Quick start (from project root)

```bash
poetry install        # create venv and install dependencies
poetry run python main.py   # run the main script without installing the package
# or, after `poetry install`, run the console script:
poetry run run-main
```

## Notes

- Keep `pyproject.toml` and `poetry.lock` under version control. Ignore the `.venv/` folder.


License / Author
- Update this file with project license and author information as needed.

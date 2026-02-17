# options-screen-queue

This project uses Poetry for dependency management and a project-local virtual environment (`.venv`). Below are quick setup and VS Code tips.

## Setup (recommended)

1. Install Poetry (recommended via pipx) or with pip:

```powershell
# pipx (recommended)
python -m pip install --user pipx
python -m pipx ensurepath
# restart PowerShell, then:
pipx install poetry

# or (alternative)
py -3 -m pip install --user poetry
```

2. Create and use the project venv and install dependencies:

```powershell
cd "C:\Users\Quentin\Documents\Personal Projects\git\options-screen-queue"
# Create project-local .venv and install
py -3 -m poetry config virtualenvs.in-project true
py -3 -m poetry install
```

3. Activate the venv (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
# then run
python main.py
# or use poetry run
py -3 -m poetry run python main.py
```

## Adding dependencies

Add runtime dependencies with:

```powershell
py -3 -m poetry add <package>
py -3 -m poetry add --dev <dev-package>
```

This project currently uses: `pandas`, `numpy`, and `yfinance`.

## VS Code interpreter

If Poetry created `.venv` in the project root, set VS Code Python interpreter to:

```
# Windows
<project-root>\.venv\Scripts\python.exe
```

Or use the Command Palette: `Python: Select Interpreter` and pick the `.venv` entry.

## Testing/Running
```
poetry install
poetry run run-main
```

## Notes

- Commit `pyproject.toml` and `poetry.lock`. Ignore `.venv/` (this repo's `.gitignore` already does).

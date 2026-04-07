# justfile for Research Paper Pipeline
# Run `just` to see available commands, `just <command>` to execute one.

# Default: list available commands
default:
    @just --list

# ── Environment ───────────────────────────────────────────────────────────────

# Create virtual environment, install dependencies, set up pre-commit hooks,
# and create a local .env file from the example if one does not already exist.
install:
    @echo "--- creating virtual environment ---"
    uv venv .venv
    @echo "--- installing dependencies ---"
    uv pip install -e ".[dev]"
    @echo "--- installing pre-commit hooks ---"
    .venv/bin/pre-commit install --install-hooks
    @echo "--- creating .env from .env.example ---"
    @if [ ! -f .env ]; then cp .env.example .env && echo ".env created — edit it to set your API keys."; \
    else echo ".env already exists — skipping."; fi
    @echo "--- done. Run 'just --list' to see available commands. ---"

# ── Code quality ──────────────────────────────────────────────────────────────

# Run linter, formatter check, and type checker across the codebase.
check:
    @echo "--- ruff lint ---"
    .venv/bin/ruff check code/ workflow/ tests/
    @echo "--- ruff format (check) ---"
    .venv/bin/ruff format --check code/ workflow/ tests/
    @echo "--- mypy ---"
    .venv/bin/mypy code/ workflow/

# Auto-fix formatting and lint issues in place.
fmt:
    .venv/bin/ruff format code/ workflow/ tests/
    .venv/bin/ruff check --fix code/ workflow/ tests/

# ── Tests ─────────────────────────────────────────────────────────────────────

# Run the test suite.
test:
    .venv/bin/pytest

# ── Agent Pipeline ────────────────────────────────────────────────────────────

# Run the full research pipeline (Phases 1-3). Pass extra flags after --.
# Examples:
#   just agents                        # full pipeline from scratch
#   just agents -- --start-phase 3     # jump to Phase 3
#   just agents -- --start-iteration 2 # resume loop at iteration 2
agents *FLAGS:
    @echo "Running agent pipeline..."
    bash workflow/run_pipeline.sh {{FLAGS}}

# ── Empirical Pipeline ────────────────────────────────────────────────────────

# Download raw data from source
data:
    @echo "Downloading data..."
    .venv/bin/python code/download_data.py

# Build the cleaned dataset from raw data
dataset: data
    @echo "Building dataset..."
    .venv/bin/python code/build_dataset.py

# Run regressions and generate figures
empirics: dataset
    @echo "Running regressions..."
    .venv/bin/python code/run_regressions.py
    @echo "Generating figures..."
    .venv/bin/python code/generate_figures.py

# Run the full empirical pipeline: data → dataset → empirics
run-pipeline: empirics
    @echo "Empirical pipeline complete."

# ── Paper ─────────────────────────────────────────────────────────────────────

# Compile the LaTeX paper to PDF using latexmk
render-paper:
    @echo "Compiling LaTeX paper..."
    latexmk -pdf -interaction=nonstopmode -outdir=paper paper/main.tex

# Remove LaTeX auxiliary files (keep the PDF)
clean:
    @echo "Cleaning LaTeX build artifacts..."
    latexmk -outdir=paper -c paper/main.tex
    rm -f paper/*.bbl

# ── Full Pipeline ─────────────────────────────────────────────────────────────

# Run the complete research pipeline: agents → empirics → paper
research: agents run-pipeline render-paper
    @echo "Research pipeline complete."

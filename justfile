# justfile for AI-Finance Research Pipeline
# Run `just` to see available commands, `just <command>` to execute one.

# Default: list available commands
default:
    @just --list

# ── Environment ───────────────────────────────────────────────────────────────

# Create a virtual environment and install dependencies
install:
    @echo "Setting up Python virtual environment..."
    python3 -m venv .venv
    @echo "Activating environment and installing dependencies..."
    .venv/bin/pip install --upgrade pip
    @if [ -f requirements.txt ]; then \
        .venv/bin/pip install -r requirements.txt; \
    else \
        echo "No requirements.txt found — skipping package install."; \
    fi

# ── Agent Pipeline ────────────────────────────────────────────────────────────

# Run the AI agent pipeline (Research Director → Theory → Literature → Writer → Referee)
agents:
    @echo "Running AI agent pipeline..."
    .venv/bin/python workflow/run_agents.py

# ── Empirical Pipeline ────────────────────────────────────────────────────────

# Download raw data from source
data:
    @echo "Downloading data..."
    .venv/bin/python code/download_data.py

# Build the cleaned dataset from raw data
dataset:
    @echo "Building dataset..."
    .venv/bin/python code/build_dataset.py

# Run regressions and generate figures
empirics:
    @echo "Running regressions..."
    .venv/bin/python code/run_regressions.py
    @echo "Generating figures..."
    .venv/bin/python code/generate_figures.py

# ── Paper ─────────────────────────────────────────────────────────────────────

# Compile the LaTeX paper to PDF using latexmk
paper:
    @echo "Compiling LaTeX paper..."
    latexmk -pdf -interaction=nonstopmode -outdir=paper paper/main.tex

# Remove LaTeX auxiliary files (keep the PDF)
clean:
    @echo "Cleaning LaTeX build artifacts..."
    latexmk -outdir=paper -c paper/main.tex
    rm -f paper/*.bbl

# ── Full Pipeline ─────────────────────────────────────────────────────────────

# Run the complete research pipeline: agents → empirics → paper
research: agents empirics paper
    @echo "Research pipeline complete."

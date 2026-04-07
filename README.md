# Research Paper Pipeline

A multi-agent pipeline that drafts academic research papers autonomously using [Claude Code](https://docs.anthropic.com/en/docs/claude-code). You write a one-page research idea; the pipeline scans the literature, iterates on a research plan, derives formal results, verifies the math, and writes a full LaTeX manuscript.

Built for formal theory papers targeting top journal standards (JF / RFS / Econometrica), but adaptable to other fields.

---

## How It Works

The pipeline has four phases. You provide `context/research_context.md` (your research idea), then the agents handle the rest:

| Phase | What happens | Agents involved |
|-------|-------------|-----------------|
| **1. Pre-loop** | Scans literature for novelty threats; produces initial research plan | Literature Guardian, Research Director |
| **2. Planning loop** | Iteratively refines the plan until it scores >= 4.0/5.0 (max 5 iterations) | Research Director, Literature Guardian, Research Evaluator |
| **3. Execution** | Derives formal model, verifies math, writes manuscript in four editing passes | Theory Builder, Model Verifier, Paper Writer, Research Evaluator |
| **4. Quality assurance** | Three self-review lenses critique the manuscript; agents fix issues | Theory/Presentation/Framing Lenses, Research Director, Paper Writer |

All inter-agent communication happens through shared markdown files in `context/` — no databases, no servers, no API orchestration code. The pipeline script simply calls `claude -p "prompt..."` for each step.

See [PIPELINE_MAP.md](PIPELINE_MAP.md) for the full architecture, flowcharts, and agent catalogue.

---

## Two Ways to Run the Pipeline

There are two ways to use this pipeline, depending on whether you have a **Claude Pro/Max subscription** or an **Anthropic API key**. Both use [Claude Code](https://docs.anthropic.com/en/docs/claude-code) — the difference is how Claude Code is authenticated and how you invoke it.

| | **Option A: Claude Code (Interactive)** | **Option B: Anthropic API (Headless)** |
|---|---|---|
| **What you need** | A Claude Pro or Max subscription | An Anthropic API key (`sk-ant-...`) |
| **How it runs** | You open Claude Code in the terminal and run commands interactively, or paste prompts from the pipeline script | The `run_pipeline.sh` script calls `claude -p "..."` in headless mode — fully automated |
| **Cost model** | Included in your subscription (subject to rate limits) | Pay-per-token via API credits ($5–30+ per full run) |
| **Automation** | Manual — you drive each step | Fully automated — runs overnight unattended |
| **Best for** | Exploring, iterating on individual phases, running Phase 4 QA | Full end-to-end runs, overnight batch execution |

Both options require Docker, VS Code, and the Dev Containers extension (see [Prerequisites](#prerequisites) below). The devcontainer has Claude Code pre-installed.

### Option A: Claude Code with a Subscription

If you have a Claude Pro or Max subscription, Claude Code authenticates through your browser — no API key needed.

1. Open the devcontainer (see [Quick Start](#quick-start) steps 1–2)
2. In the devcontainer terminal, run:
   ```bash
   claude
   ```
3. On first launch, Claude Code will open a browser window to authenticate with your Claude account. Follow the prompts to log in.
4. Once authenticated, you can run pipeline steps interactively. For example:
   ```
   # Inside the Claude Code session, paste prompts from run_pipeline.sh,
   # or ask Claude directly:
   > Read context/research_context.md, then run as the Literature Guardian
   >   in Mode 1 (Quick Scan) following skills/literature-review-light/SKILL.md.
   >   Produce threat_map_v1.md, threat_map.md, literature_constraints.md,
   >   and search_log.md in context/.
   ```
5. You can also run Phase 4 (QA) this way, which requires interactive subagent dispatch — see [PIPELINE_MAP.md](PIPELINE_MAP.md#phase-4--pipeline-commands).

> **Tip:** You can run the automated pipeline script with a subscription too — Claude Code's `claude -p` headless mode works with subscription auth. Just run `./workflow/run_pipeline.sh` as described in Option B. The only difference is rate limits may throttle long runs, whereas API keys have no rate limit (only cost).

### Option B: Anthropic API Key (Headless)

If you have an Anthropic API key, the pipeline runs fully automated via `claude -p` (headless mode). No browser login required.

1. Get an API key from [console.anthropic.com](https://console.anthropic.com/) → **Settings > API Keys > Create Key**
2. Export it in your shell profile so the devcontainer picks it up:
   ```bash
   # Add to ~/.zshrc (macOS) or ~/.bashrc (Linux):
   export ANTHROPIC_API_KEY="sk-ant-your-key-here"
   ```
3. Restart your terminal (or `source ~/.zshrc`), then **open VS Code from that same terminal** so it inherits the environment variable:
   ```bash
   cd ai-finance-paper
   code .
   ```
   > **Important:** Launching VS Code from the terminal (rather than from Finder/Start Menu/dock) ensures it inherits your shell's environment variables. If you open VS Code via the GUI, it may not see `ANTHROPIC_API_KEY`.
4. Reopen in the devcontainer — the key is passed through automatically via `devcontainer.json`.
5. Run the full pipeline:
   ```bash
   ./workflow/run_pipeline.sh
   ```

> **Alternative (`.env` file):** You can also set the key in the `.env` file in the project root:
> ```bash
> # .env
> ANTHROPIC_API_KEY=sk-ant-your-actual-key-here
> ```
> This is less secure because Claude Code can read files in the project directory, meaning the key is visible in context during agent runs. Prefer the shell profile approach above when possible.

> **Cost note:** The full pipeline makes 15–20 Claude API calls (each a substantial prompt with file context). Depending on model tier and paper complexity, a full run costs $5–30+ in API credits. You can resume from any phase if interrupted — see [Resuming a partial run](#resuming-a-partial-run).

### Which should I use?

- **Start with Option A** if you already have a Claude subscription. It lets you run steps one at a time, inspect intermediate outputs, and iterate without worrying about API costs.
- **Use Option B** when you want a fully hands-off run (e.g., kick it off before bed and have a draft by morning), or if you don't have a Claude subscription.
- **You can mix both.** For example, run Phases 1–3 overnight with the API, then do Phase 4 (QA) interactively with your subscription.

---

## Prerequisites

You need these installed on your machine **before** cloning the repo:

| Requirement | Why | Install |
|-------------|-----|---------|
| [Docker Desktop](https://docs.docker.com/get-docker/) | Runs the pipeline in an isolated container | Follow the link for your OS |
| [VS Code](https://code.visualstudio.com/) | Opens the devcontainer environment | Download from the link |
| [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) | Lets VS Code build and enter the Docker container | Install from VS Code Extensions tab (search "Dev Containers") |
| Claude Pro/Max subscription **or** Anthropic API key | Powers the Claude agents | See [Two Ways to Run](#two-ways-to-run-the-pipeline) above |

**Optional:** A GitHub personal access token (only if you want agents to interact with GitHub).

---

## Quick Start

### 1. Clone and open in the devcontainer

```bash
git clone <your-repo-url>
cd ai-finance-paper
code .
```

VS Code will detect the devcontainer configuration and show a popup: **"Reopen in Container"** — click it.

> **First build takes 3-5 minutes** (it installs Python, Node.js, LaTeX, and Claude Code inside the container). Subsequent opens are instant.

If you don't see the popup, open the Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`) and run **"Dev Containers: Reopen in Container"**.

### 2. Install dependencies

Once inside the devcontainer terminal:

```bash
just install
```

This creates a Python virtual environment, installs all packages, and sets up pre-commit hooks. It also creates a `.env` file from the template if one doesn't exist yet.

### 3. Authenticate Claude Code

Choose based on your setup (see [Two Ways to Run](#two-ways-to-run-the-pipeline)):

- **Subscription:** Run `claude` in the devcontainer terminal and follow the browser login prompt.
- **API key:** Export `ANTHROPIC_API_KEY` in your host shell profile (e.g. `~/.zshrc`), then **open VS Code from that terminal** with `code .` so it inherits the variable. The devcontainer passes it through automatically. You can also set it in the `.env` file, but this is less secure — Claude Code can read project files, so the key would be visible in agent context. Prefer the shell profile approach.

### 4. Write your research idea

Open `context/research_context.md` and fill in the placeholders:

- **Research question** — a single, precise question
- **Mechanism** — the causal chain you plan to formalise
- **Key primitive** — the central modelling object
- **Contributions** — planned formal results (number each one)
- **Prior art** — foundational papers your model builds on
- **Scope constraints** — binding design choices (e.g., "static model only")
- **Target venue** — the journal standard you're writing for
- **Empirical strategy** — brief description, or "Theory only"

This is the only file you need to write. Everything else is generated by the pipeline.

### 5. Run the pipeline

**Automated (headless)** — works with either auth method:

```bash
chmod +x workflow/run_pipeline.sh
./workflow/run_pipeline.sh
```

The pipeline runs autonomously. Progress is logged to the terminal and to `workflow/research-log.md`. It will:

- Run Phases 1–3 end-to-end
- Produce all intermediate artifacts in `context/`
- Write the manuscript sections in `paper/sections/`
- Stop if the Model Verifier flags critical issues (you'll see the error and can check `context/model_verifier_report.md`)

**Interactive** — run steps manually in a Claude Code session:

```bash
claude
```

Then paste individual step prompts from `workflow/run_pipeline.sh`, or describe what you want in natural language. This is useful for iterating on a single phase or debugging.

### 6. Compile the paper

After the pipeline finishes:

```bash
just render-paper
```

This compiles the LaTeX manuscript to `paper/main.pdf`.

> **Note:** You will likely need to add `\input{sections/...}` lines to `paper/main.tex` to include the generated sections. The Paper Writer creates the section files, but you wire them into the main document.

---

## Resuming a partial run

The pipeline persists all state to files, so you can resume from any point:

```bash
# Resume Phase 2 loop from iteration 3 (skips Phase 1):
./workflow/run_pipeline.sh --start-iteration 3

# Jump straight to Phase 3 (skips Phases 1 and 2):
./workflow/run_pipeline.sh --start-phase 3
```

Check `context/loop_state.md` to see which iteration you're on and what the last score was.

### Phase 4 (Quality Assurance)

Phase 4 is **not yet automated** in the pipeline script. It requires interactive Claude Code sessions because it uses parallel subagent dispatch. To run it manually:

1. Open a Claude Code session in the devcontainer
2. Follow the step-by-step commands in [PIPELINE_MAP.md — Phase 4 Pipeline Commands](PIPELINE_MAP.md#phase-4--pipeline-commands)

---

## Customising for Your Paper

### Changing the evaluation criteria

Edit `context/evaluation_criteria.md` to adjust the scoring rubric. The default is calibrated for top-5 finance/economics journals. You can change:

- The 8 scoring criteria and their standards
- The quality threshold (default: 4.0/5.0)
- Hard failure conditions

### Adapting for a different field

The pipeline structure is field-agnostic, but the default skills and evaluation criteria are written for formal economics/finance theory. To adapt:

1. Edit `context/evaluation_criteria.md` for your field's standards
2. Review the skills in `skills/` — the literature search heuristics in `skills/literature-review-light/references/` are finance-specific
3. Adjust `context/research_context.md` scope constraints for your methodology

### Empirical papers

The empirical pipeline is scaffolded but not implemented. The Python scripts in `code/` are stubs:

- `code/download_data.py` — data acquisition (stub)
- `code/build_dataset.py` — data cleaning (stub)
- `code/run_regressions.py` — estimation (stub)
- `code/generate_figures.py` — visualisation (stub)

Fill these in for your project. Run the empirical pipeline with:

```bash
just run-pipeline   # runs: data → dataset → empirics
```

---

## Directory Structure

```
context/                  # Research artifacts — agents read and write here
  research_context.md     # YOUR INPUT — the only file you write
  evaluation_criteria.md  # Scoring rubric (customise for your venue)
  self_reviews/           # QA loop review reports
  README.md               # File registry explaining each context file

paper/                    # LaTeX manuscript
  main.tex                # Document preamble (add \input lines for sections)
  references.bib          # Bibliography
  sections/               # Section .tex files (generated by Paper Writer)
  tables/                 # Table .tex files (generated by Empirical Agent)

code/                     # Python scripts for data and analysis
  verification/           # SymPy verification scripts (generated by Model Verifier)

workflow/                 # Pipeline orchestration
  run_pipeline.sh         # Automated pipeline runner (Phases 1-3)
  research-log.md         # Append-only process log

skills/                   # Reusable prompt templates for agents
  academic-writing/       # LaTeX writing conventions
  manuscript-layout/      # Layout and formatting standards
  self-critique/          # Structured self-critique workflow
  economic-model-builder/ # Model derivation workflow
  literature-review-*/    # Literature search workflows (light/targeted/deep)
  empirical-design/       # Empirical pipeline (stub)

.claude/agents/           # Agent definitions (role, tools, modes)
archive/                  # Worked example from a prior project
```

---

## Agents

| Agent | Role | Phase |
|-------|------|-------|
| Research Director | Strategic planning, task decomposition, quality synthesis | 1, 2, 3, 4 |
| Literature Guardian | Novelty risk analysis, literature mapping (uses web search) | 1, 2, 3, 4 |
| Research Evaluator | Quality scoring against rubric, referee simulation | 2, 3 |
| Theory Builder | Formal model derivation, equilibrium solving | 3, 4 |
| Model Verifier | Mathematical verification via SymPy | 3 |
| Paper Writer | LaTeX manuscript writing (4 sequential passes) | 3, 4 |
| Theory/Presentation/Framing Lenses | Self-review critique (run in parallel) | 4 |
| Comprehensive Reviewer | Full referee simulation (5 modes) | 3, 4 |

Each agent's full specification is in `.claude/agents/<name>.md`.

---

## Worked Example

The `archive/` directory contains a complete worked example from a prior project (AI homogeneity in financial markets). It shows all artifacts the pipeline produces — useful as a reference for what to expect.

---

## Available Commands

```bash
just install        # Set up Python environment, pre-commit hooks, and .env
just test           # Run smoke tests (verifies repo structure)
just check          # Run linter (ruff) and type checker (mypy)
just fmt            # Auto-fix formatting issues
just render-paper   # Compile LaTeX manuscript to PDF
just run-pipeline   # Run the empirical pipeline (data → regressions → figures)
just clean          # Remove LaTeX build artifacts
```

---

## Troubleshooting

### "Reopen in Container" doesn't appear

Make sure the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) is installed in VS Code, and that Docker Desktop is running.

### `just install` fails

- Make sure you're inside the devcontainer (the terminal prompt should show the container)
- If you see permission errors, run: `sudo chown -R vscode:vscode /home/vscode`

### Pipeline fails with "ANTHROPIC_API_KEY not set"

If using an API key:
- Export it in your host shell profile **before** opening the devcontainer, or
- Set it in the `.env` file inside the project root

If using a Claude subscription:
- Run `claude` interactively first to complete the browser login flow. Once authenticated, `claude -p` (headless mode) will use your subscription credentials automatically.

### Pipeline stops at Model Verifier with "FAIL"

This means the formal model has issues the Theory Builder couldn't auto-fix. Check `context/model_verifier_report.md` for details. You may need to revise `context/research_context.md` (e.g., simplify scope constraints) and re-run from Phase 3.

### LaTeX compilation errors

- Make sure section files exist in `paper/sections/` before running `just render-paper`
- Check that `paper/main.tex` has the right `\input{sections/...}` lines
- Citation warnings are normal on first compile — run `just render-paper` twice

### I want to run only part of the pipeline

```bash
./workflow/run_pipeline.sh --start-phase 2    # skip Phase 1
./workflow/run_pipeline.sh --start-phase 3    # skip Phases 1 and 2
./workflow/run_pipeline.sh --start-iteration 3  # resume loop at iteration 3
```

---

## Platform Notes

This pipeline is designed to run **inside the devcontainer**. Running it directly on macOS or Linux is possible but requires manual setup:

- Install Python 3.12+, Node.js 20+, and Claude Code CLI (`npm install -g @anthropic-ai/claude-code`)
- Install LaTeX (`texlive-full` or equivalent)
- Install `just` command runner
- Install `uv` package manager
- The pipeline script uses Linux-style `sed -i` — on macOS, you'd need `gsed` or adjust the commands

Using the devcontainer avoids all of this.

---

## Contributing

1. Fork the repo
2. Open in the devcontainer
3. Make your changes
4. Run `just check` and `just test` to verify
5. Submit a pull request

The agent definitions in `.claude/agents/` and skills in `skills/` are the most impactful places to contribute improvements.

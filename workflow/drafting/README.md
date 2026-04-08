# Drafting Pipeline

> **Setup first:** See the [top-level README](../../README.md) for prerequisites, installation, and authentication.

This workflow takes a one-page research idea and produces a full LaTeX manuscript autonomously. You provide `context/research_context.md`; the agents handle the rest.

---

## How the Drafting Pipeline Works

The pipeline has four phases:

| Phase | What happens | Agents involved |
|-------|-------------|-----------------|
| **1. Pre-loop** | Scans literature for novelty threats; produces initial research plan | Literature Guardian, Research Director |
| **2. Planning loop** | Iteratively refines the plan until it scores >= 4.0/5.0 (max 5 iterations) | Research Director, Literature Guardian, Research Evaluator |
| **3. Execution** | Derives formal model, verifies math, writes manuscript in four editing passes | Theory Builder, Model Verifier, Paper Writer, Research Evaluator |
| **4. Quality assurance** | Three self-review lenses critique the manuscript; agents fix issues | Theory/Presentation/Framing Lenses, Research Director, Paper Writer |

All inter-agent communication happens through shared markdown files in `context/` — no databases, no servers, no API orchestration code. The pipeline script simply calls `claude -p "prompt..."` for each step.

See [PIPELINE_MAP.md](../../PIPELINE_MAP.md) for the full architecture, flowcharts, and agent catalogue.

---

## Two Ways to Run

There are two ways to use this pipeline, depending on whether you have a **Claude Pro/Max subscription** or an **Anthropic API key**. Both use [Claude Code](https://docs.anthropic.com/en/docs/claude-code) — the difference is how Claude Code is authenticated and how you invoke it.

| | **Option A: Claude Code (Interactive)** | **Option B: Anthropic API (Headless)** |
|---|---|---|
| **What you need** | A Claude Pro or Max subscription | An Anthropic API key (`sk-ant-...`) |
| **How it runs** | You open Claude Code in the terminal and run commands interactively, or paste prompts from the pipeline script | The `run_pipeline.sh` script calls `claude -p "..."` in headless mode — fully automated |
| **Cost model** | Included in your subscription (subject to rate limits) | Pay-per-token via API credits ($5–30+ per full run) |
| **Automation** | Manual — you drive each step | Fully automated — runs overnight unattended |
| **Best for** | Exploring, iterating on individual phases, running Phase 4 QA | Full end-to-end runs, overnight batch execution |

### Option A: Claude Code with a Subscription

If you have a Claude Pro or Max subscription, Claude Code authenticates through your browser — no API key needed.

1. Open the devcontainer (see [top-level README](../../README.md) Quick Start steps 1–2)
2. In the devcontainer terminal, run:
   ```bash
   claude
   ```
3. On first launch, Claude Code will open a browser window to authenticate with your Claude account. Follow the prompts to log in.
4. Once authenticated, follow the [Interactive Runbook](interactive_runbook.md) — it has the exact prompt to paste for every step across all four phases.
5. You can also run Phase 4 (QA) this way, which requires interactive subagent dispatch — see [PIPELINE_MAP.md](../../PIPELINE_MAP.md#phase-4--pipeline-commands).

> **Tip:** You can run the automated pipeline script with a subscription too — Claude Code's `claude -p` headless mode works with subscription auth. Just run `./workflow/drafting/run_pipeline.sh` as described in Option B. The only difference is rate limits may throttle long runs, whereas API keys have no rate limit (only cost).

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
   ./workflow/drafting/run_pipeline.sh
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

## Running the Drafting Pipeline

### 1. Write your research idea

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

### 2. Run the pipeline

**Automated (headless)** — works with either auth method:

```bash
chmod +x workflow/drafting/run_pipeline.sh
./workflow/drafting/run_pipeline.sh
```

The pipeline runs autonomously. Progress is logged to the terminal and to `workflow/drafting/research-log.md`. It will:

- Run Phases 1–3 end-to-end
- Produce all intermediate artifacts in `context/`
- Write the manuscript sections in `paper/sections/`
- Stop if the Model Verifier flags critical issues (you'll see the error and can check `context/model_verifier_report.md`)

**Interactive** — run steps manually in a Claude Code session:

```bash
claude
```

Then follow the [Interactive Runbook](interactive_runbook.md), which has the exact prompt to paste for every step. This is useful for iterating on individual phases, inspecting intermediate outputs, or debugging.

### 3. Compile the paper

After the pipeline finishes:

```bash
just render-paper
```

This compiles the LaTeX manuscript to `paper/main.pdf`.

> **Note:** You will likely need to add `\input{sections/...}` lines to `paper/main.tex` to include the generated sections. The Paper Writer creates the section files, but you wire them into the main document.

---

## Resuming a Partial Run

The pipeline persists all state to files, so you can resume from any point:

```bash
# Resume Phase 2 loop from iteration 3 (skips Phase 1):
./workflow/drafting/run_pipeline.sh --start-iteration 3

# Jump straight to Phase 3 (skips Phases 1 and 2):
./workflow/drafting/run_pipeline.sh --start-phase 3
```

Check `context/loop_state.md` to see which iteration you're on and what the last score was.

### Phase 4 (Quality Assurance)

Phase 4 is **not yet automated** in the pipeline script. It requires interactive Claude Code sessions because it uses parallel subagent dispatch. To run it manually:

1. Open a Claude Code session in the devcontainer
2. Follow the step-by-step commands in [PIPELINE_MAP.md — Phase 4 Pipeline Commands](../../PIPELINE_MAP.md#phase-4--pipeline-commands)

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
2. Review the skills in `skills/` — the literature search heuristics in `.claude/skills/literature-review/references/` are finance-specific
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

## Contents of This Directory

| File | Purpose |
|------|---------|
| `run_pipeline.sh` | Automated pipeline runner (Phases 1–3) |
| `interactive_runbook.md` | Step-by-step prompts for interactive runs |
| `research-log.md` | Append-only process log |
| `phase1_flowchart.md` | Phase 1 flowchart: Pre-Loop |
| `phase2_flowchart.md` | Phase 2 flowchart: Planning Loop |
| `phase3_flowchart.md` | Phase 3 flowchart: Post-Loop Execution |
| `phase4_flowchart.md` | Phase 4 flowchart: Quality Assurance Loop |

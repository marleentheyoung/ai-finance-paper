# Claude Code — Project Instructions

## Environment

You are running inside a Docker devcontainer (Debian Bookworm, Python 3.11).
The container boundary provides isolation from the host machine.
`--dangerously-skip-permissions` is enabled — act responsibly within these boundaries.

## Project

This is an academic finance research project. The goal is to produce a
peer-reviewed working paper using a multi-agent pipeline:

- **Research Director** — coordinates milestones and assigns tasks
- **Theory Builder** — develops model structure and predictions
- **Literature Guardian** — validates novelty and framing
- **Empirical Agent** — builds data pipeline and estimates models
- **Paper Writer** — integrates outputs into the manuscript

## Permitted actions

- Read and write files under:
  - `paper/` — LaTeX manuscript
  - `code/` — Python scripts for data and analysis
  - `context/` — research notes and model equations
  - `workflow/` — logs, runbooks, and orchestration
  - `data/` — raw and processed datasets (may be created at runtime)
  - `agents/` — agent instruction files
  - `skills/` — skill definitions
- Run Python scripts in `code/` via `python` or `just`
- Compile the paper via `latexmk` or `just paper`
- Read Git history and status

## Prohibited actions

- Do NOT modify `.devcontainer/` files (Dockerfile, devcontainer.json)
- Do NOT run `git push` or open pull requests without explicit user instruction
- Do NOT install system packages via `apt-get` or `brew`
- Do NOT modify `CLAUDE.md` itself
- Do NOT access or exfiltrate the `ANTHROPIC_API_KEY` or `GITHUB_TOKEN`
- Do NOT write outside `/workspaces/ai-finance-paper/`

## Coordination

- Log major decisions and progress in `workflow/research-log.md`
- Track open questions and critiques in `context/referee_reports/` and `context/evaluator_feedback.md`
- Agents must not overwrite each other's outputs without reading them first
- Always read the relevant `agents/<name>.md` before acting as that agent

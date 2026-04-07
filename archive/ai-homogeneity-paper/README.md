# AI Homogeneity Paper — Worked Example

This directory contains the complete output from running the multi-agent paper drafting pipeline on the research project "AI Signal Homogeneity and Systemic Financial Fragility."

It serves as a reference example of what the pipeline produces.

## Contents

- `context/` — all research artifacts: plans, threat maps, evaluator feedback, model equations, literature reviews
- `paper/` — the complete LaTeX manuscript (sections, tables, bibliography)
- `code/verification/` — SymPy verification scripts produced by the Model Verifier
- `workflow/research-log.md` — the append-only process log from the pipeline run

## How this was generated

1. A human provided `context/research_context.md` (the "idea seed")
2. The pipeline ran Phases 1-4 autonomously (planning loop, execution, QA)
3. All intermediate and final artifacts were preserved here

See `PIPELINE_MAP.md` in the repository root for the full pipeline architecture.

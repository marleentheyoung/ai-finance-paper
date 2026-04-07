# Workflow Directory

Pipeline orchestration, process logs, and human audit notes live here.

**Boundary rule:**
- **`context/`** = research content that agents read and write (the "what")
- **`workflow/`** = pipeline scripts, process logs, human audit notes (the "how")

## Contents
- `run_pipeline.sh` — overnight pipeline orchestration script
- `interactive_runbook.md` — step-by-step prompts for running the pipeline interactively
- `research-log.md` — append-only process log (agents + pipeline write here)

### Pipeline flowcharts
Visual phase-by-phase flowcharts showing agent sequencing, file I/O, and decision points.
- `phase1_flowchart.md` — Phase 1: Pre-Loop (literature scan → initial plan)
- `phase2_flowchart.md` — Phase 2: Planning Loop (iterative refinement → quality gate)
- `phase3_flowchart.md` — Phase 3: Post-Loop Execution (derive → verify → evaluate → write)

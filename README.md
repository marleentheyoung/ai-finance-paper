# ai-finance-paper

Minimal scaffold for an AI-assisted finance research paper.

## Structure
- `paper/`: LaTeX manuscript, section files, bibliography, figures, and tables.
- `agents/`: Prompt templates for specialized AI research roles.
- `context/`: Research framing notes, literature summaries, and threat-paper tracking.
- `code/`: Data and analysis pipeline scripts.
- `data/`: Raw and processed datasets.
- `workflow/`: AI workflow, progress log, and referee-style review notes.

## How AI Agents Contribute
- Research Director coordinates tasks and integration.
- Theory Builder develops formal models and predictions.
- Literature Guardian checks novelty and positioning.
- Empirical Agent executes data and econometric workflow.
- Paper Writer turns outputs into journal-style prose.

This scaffold is intentionally minimal: fill in each template as the project evolves.

## Workflow

Human → Idea

Literature Guardian → quick scan
    output:
        threat_map_v1

while score < threshold and n_iterations < 5:

    Research Director → research plan

    Literature Guardian → targeted literature check
        update threat_map

    Research Evaluator → evaluate plan

Literature Guardian → deep literature review
    output:
        threat_map_final
        literature_review
        literature_review.tex

---

name: literature-review
description: Conducts structured academic literature reviews in economics and finance. Use when mapping research literature, identifying related papers, evaluating novelty claims, or summarizing theoretical models from academic papers.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Literature Review Skill

## Purpose

Perform systematic academic literature analysis suitable for finance PhD research and top-journal papers.

The skill ensures literature reviews are structured, reproducible, and focused on mechanisms rather than superficial summaries.

Outputs should prioritize:

* theoretical mechanisms
* equilibrium structures
* novelty comparisons
* citation accuracy

---

# Workflow

## Step 1 — Identify Relevant Papers

Search for papers related to the research topic.

Focus on:

* top finance journals (JF, JFE, RFS)
* AER / Econometrica / QJE
* NBER working papers
* leading theoretical contributions

Return a list of papers with:

* authors
* year
* journal
* main mechanism

---

## Step 2 — Structured Paper Extraction

For each paper produce a structured summary:

Paper:
Authors:
Journal / Year:

Core Question:
What economic problem does the paper address?

Model Structure:
Describe primitives, agents, information structure, and equilibrium concept.

Key Mechanism:
Explain the main theoretical channel.

Key Result:
Summarize the main proposition or theorem.

Relation to Current Project:
Explain whether the mechanism overlaps with the project model.

Novelty Threat Level:

* High overlap
* Moderate overlap
* Low overlap

---

## Step 3 — Mechanism Mapping

Construct a literature map identifying the mechanisms used in the literature.

Example categories:

* coordination games
* information acquisition
* market microstructure
* algorithmic trading
* AI finance

For each category list the relevant papers and mechanisms.

---

## Step 4 — Novelty Check

Compare literature with the proposed model.

Identify:

1. mechanisms already studied
2. missing mechanisms
3. potential novelty contributions

Flag any papers that might invalidate novelty claims.

---

## Output Format

Produce three outputs:

1. `literature_notes.md`
   Structured summaries of all papers.

2. `mechanism_map.md`
   Mechanism classification of literature.

3. `novelty_analysis.md`
   Assessment of research novelty.

---

## Quality Criteria

The literature review must:

* cite canonical papers
* identify mechanisms precisely
* distinguish between similar models
* avoid vague summaries

Prefer analytical descriptions over narrative summaries.

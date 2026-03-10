# AI Finance Paper — Project Runbook

This document describes the step-by-step workflow for developing the AI-assisted finance research paper.

The purpose of this file is to:

• guide the research process
• maintain consistency across AI sessions
• ensure reproducibility of the AI workflow
• document how agents are used in the project

All AI conversations working on this project should read this document before performing tasks.

---

# Project Goal

Develop a formal financial economics theory explaining how **AI model homogeneity creates systemic financial fragility**.

The theoretical primitive is the cross-agent signal correlation parameter:

ρ ∈ [0,1]

Agents observe signals:

εᵢ = √ρ η + √(1−ρ) ξᵢ

where η is the shared AI model error component and ξᵢ is idiosyncratic noise.

The paper analyzes how increasing ρ affects:

1. coordination failures
2. information acquisition
3. market liquidity

---

# Repository Structure

The project repository contains the following directories.

```
ai-finance-paper

agents/
AI agent role definitions

context/
core research context and literature notes

paper/
LaTeX manuscript

code/
empirical scripts

data/
raw and processed datasets

workflow/
documentation of the AI research workflow
```

---

# Research Workflow Overview

The project follows a multi-agent research pipeline.

```
Research Director
        ↓
Theory Builder
        ↓
Literature Guardian
        ↓
Paper Writer
        ↓
LaTeX manuscript
```

The human researcher orchestrates communication between agents.

---

# Step 1 — Construct the Research Context

Create the file:

```
context/research_context.md
```

This document defines the permanent intellectual context of the project.

It must include:

• model primitives
• signal structure
• theoretical channels
• amplification loop
• core contributions
• threat papers

All agents should receive this file as input before performing tasks.

Purpose:

Ensure every AI interaction is grounded in the same theoretical framework.

Notes:

The research context is the **single most important document in the system**.
It should remain stable once finalized.

---

# Step 2 — Configure AI Agents

Agent prompt files are stored in:

```
agents/
```

Each agent represents a specialized research role.

Agents used in this project:

Research Director
Theory Builder
Literature Guardian
Empirical Agent
Paper Writer

Each agent file should include:

ROLE
OBJECTIVES
WORKFLOW
INPUTS
OUTPUT FORMAT

Agents should not contain project-specific theory.
They define behavior rather than research content.

---

# Step 3 — Plan Modeling Tasks

Run the Research Director agent.

Input:

• research_context.md
• research-director.md

Prompt example:

"Identify the first three theoretical modeling tasks required to develop the paper."

Expected output:

Task assignments such as:

1 Develop the coordination failure channel
2 Extend Grossman-Stiglitz to correlated AI signals
3 Formalize liquidity withdrawal equilibrium

These tasks define the research roadmap.

---

# Step 4 — Develop Theoretical Channels

Use the Theory Builder agent to construct each channel.

Channels:

1 Coordination failure (global games)
2 Information acquisition (Grossman-Stiglitz)
3 Liquidity withdrawal (market microstructure)

For each channel the agent should produce:

• primitives
• equilibrium conditions
• propositions
• proof sketches
• intuition

Store results in:

```
context/model_equations.md
```

---

# Step 5 — Check Literature Overlap

After each model component is developed, run the Literature Guardian.

Input:

• research_context.md
• literature-guardian.md
• model output

Tasks:

• verify novelty
• identify related papers
• clarify differentiators

Purpose:

Prevent accidental duplication of existing research.

---

# Step 6 — Integrate the Model

Combine the three channels into a unified equilibrium.

Key task:

Characterize the joint system:

(ρ_eff, θ*, N_eff)

Analyze whether the integrated system produces a fragile equilibrium.

Outputs should include:

• equilibrium definitions
• comparative statics
• amplification mechanism

---

# Step 7 — Begin Paper Writing

Write sections of the paper in:

```
paper/sections/
```

Suggested order:

1 introduction
2 literature review
3 model
4 equilibrium analysis
5 empirical motivation
6 conclusion

Use the Paper Writer agent to convert model outputs into academic prose.

---

# Step 8 — Build Empirical Motivation

Use the Empirical Agent to design a motivating empirical section.

Potential proxies for signal homogeneity:

• portfolio overlap measures
• analyst forecast correlation
• AI adoption shocks

The empirical section is intended to motivate the theory rather than establish causal identification.

Scripts are stored in:

```
code/
```

---

# Step 9 — Generate Figures and Tables

Use Python scripts to produce:

• correlation measures
• regression tables
• illustrative plots

Save outputs in:

```
paper/figures
paper/tables
```

---

# Step 10 — Run AI Referee Simulations

Before finalizing the paper, simulate referee reports.

Store outputs in:

```
workflow/referee-reports.md
```

Referee tasks:

• identify weaknesses
• request robustness checks
• test novelty claims

Multiple simulated reports improve the final paper.

---

# Step 11 — Document AI Workflow

Create a workflow description for submission.

File:

```
workflow/ai-workflow.md
```

This document should explain:

• how AI agents were used
• how tasks were structured
• how outputs were validated

The Human × AI Finance submission requires a description of the AI workflow.

---

# Operating Guidelines

Always load the following before running research tasks:

```
research_context.md
+
relevant agent prompt
+
task description
```

Avoid modifying the research context mid-project unless necessary.

Major conceptual changes should be documented in:

```
workflow/research-log.md
```

---

# Final Output

The completed project should produce:

• a LaTeX research paper
• reproducible empirical scripts
• a documented AI research workflow

Together these form the final submission package.

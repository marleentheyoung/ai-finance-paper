---
name: academic-writing
description: Converts structured prose and research outputs into publication-ready LaTeX manuscript sections for a formal theory paper. Use when drafting, revising, or formatting paper sections (.tex files), when converting context artifacts (literature_review.md, model_equations.md) into LaTeX, when checking that text matches quantitative results in tables or figures, or when ensuring manuscript consistency with top-journal conventions. Also use when asked to "write the introduction", "draft a section", "format for LaTeX", "check the manuscript", or "convert to tex". Do NOT use for literature analysis (use literature-review-deep), model derivation (use economic-model-builder), or evaluation/scoring (use self-critique).
---

# Academic Writing Skill

## Purpose

Produce publication-ready LaTeX manuscript sections for a formal theory paper targeting a top-5 journal in the relevant field. This skill is the final conversion layer: it takes structured prose and research outputs from upstream agents and produces `.tex` files that compile cleanly and meet top-journal conventions.

This skill does not perform research, derive models, or evaluate quality. It writes and formats.

---

## Inputs

Depending on which section is being written, read the relevant subset:

- `context/paper_structure.md` — section-by-section map from the Research Director (always read first)
- `context/research_context.md` — the permanent project specification
- `context/research_plan_final.md` — the finalised research plan
- `context/literature_review.md` — structured prose literature review from the Literature Guardian
- `context/threat_map_final.md` — for introduction framing and differentiators
- `context/model_equations.md` — formal derivations and propositions from the Theory Builder
- `context/evaluator_feedback.md` — final evaluator notes (for addressing anticipated referee concerns)
- `paper/sections/*.tex` — any existing sections (for cross-referencing and consistency)
- `paper/figures/` and `paper/tables/` — for results sections

---

## Workflow

### Step 1 — Read the Paper Structure Map

Always start by reading `context/paper_structure.md`. This defines what each section must contain and how sections connect. Do not invent section structure; follow the map.

### Step 2 — Identify the Section to Write

Determine which section is requested. The expected paper structure is defined in `context/paper_structure.md`. A typical layout is:

```
paper/sections/
├── introduction.tex
├── literature.tex
├── model.tex
├── [section_name].tex    # one file per model component / channel
├── ...
├── extensions.tex
├── empirics.tex
└── conclusion.tex
```

Each section has different source material and different conventions. See the section-specific guidance below.

### Step 3 — Write the Section

Write LaTeX that compiles cleanly and reads as top-journal prose. Follow all style rules and LaTeX conventions specified below.

### Step 4 — Compression Pass

After writing the section, re-read it with one question: "If I cut this sentence, does the reader lose anything they need?"

Apply these rules before proceeding:
- Delete any sentence that restates a point already made in the same section.
- Replace "It is worth noting that X" with "X."
- If a paragraph has more than two hedge phrases ("may," "potentially," "it is possible that"), remove all but one.
- If a subsection exceeds its target length by more than 20%, cut the weakest paragraphs before proceeding.

**Section word-count targets (treat as hard ceilings, not aspirations):**
- Introduction: 2,500–3,500 words
- Literature review: 2,500–3,500 words
- Each model component section: 1,500–2,500 words
- Integrating section (if any): 1,500–2,000 words
- Empirics: 1,500–2,500 words
- Conclusion: 800–1,200 words

### Step 5 — Verify Consistency

Before finalising any section:

1. Check that every quantitative claim references a specific table, figure, or proposition
2. Check that all `\cite{}` keys exist (or flag missing entries for the human)
3. Check that notation is consistent with `context/model_equations.md`
4. Check that cross-references (`\ref{}`, `\eqref{}`) point to valid labels
5. Check that the section's argument is consistent with adjacent sections

---

## Section-Specific Guidance

### Introduction

**Source material:** `threat_map_final.md` (differentiators), `research_plan_final.md` (contributions), `research_context.md` (mechanism overview)

**Structure:**
1. Opening paragraph: the economic problem
2. What this paper does: the model components and their interaction, stated precisely
3. Main results: each contribution as a concrete finding (threshold, comparative static, or characterisation)
4. Related literature: brief positioning (2-3 paragraphs), not a full review
5. Paper organisation: one paragraph mapping sections

**Rules:**
- State each contribution as a result, not a topic ("We show that..." not "We study...")
- Engage the 2-3 closest threat papers by name with precise differentiators
- Do not oversell; use "characterise", "show", "derive" rather than "prove" or "demonstrate conclusively"
- The integrating contribution (if any) must be framed as the core contribution

### Literature Review

**Source material:** `context/literature_review.md` (the Literature Guardian's structured prose)

**Task:** Convert the prose into LaTeX. The analytical structure is already defined in the source file. Do not reorganise or rewrite the argument; format it.

**Rules:**
- Preserve the section structure from `literature_review.md`
- Convert all citations to `\citet{}` (in-text) or `\citep{}` (parenthetical) as appropriate
- Do not add papers not in the source file
- Do not change threat classifications or differentiator language

### Model Sections (model.tex, [section_name].tex files)

**Source material:** `context/model_equations.md`, `context/research_context.md`

**Task:** Write the prose that surrounds the formal derivations. The equations and propositions come from the Theory Builder; this skill writes the setup, motivation, interpretation, and discussion around them.

**Structure per component section:**
1. Setup and motivation (1-2 paragraphs): why this component matters, what the foundational model is
2. Model environment: agents, information, timing, written in prose with inline math
3. Equilibrium definition
4. Main result(s): stated as formal propositions in `\begin{proposition}...\end{proposition}`
5. Comparative statics in the key primitive
6. Discussion: economic interpretation, connection to the next component

**Rules:**
- All equations in `align` or `equation` environments with `\label{eq:...}`
- All propositions labelled `\label{prop:...}`
- Notation must match `model_equations.md` exactly; do not rename variables
- Use LaTeX math commands consistently (never spell out variable names in prose where a math symbol is defined)
- Interpret every mathematical result economically; no unexplained equations

### Extensions

**Source material:** `research_plan_final.md` (extension descriptions), `model_equations.md` (if formal results exist)

**Rules:**
- Frame as natural extensions, not afterthoughts
- Clearly separate from the main model; these are not core contributions

### Empirics

**Source material:** `research_plan_final.md`, `paper/figures/`, `paper/tables/`

**Rules:**
- Frame as motivating evidence, not causal identification (unless the research design supports causal claims)
- Every number in the text must match a table or figure exactly
- Report statistics with appropriate precision (t-statistics to 2 decimals, coefficients to 3-4 significant figures)
- Use `\input{}` to include tables generated by the Empirical Agent

### Conclusion

**Rules:**
- Restate contributions concisely (1 sentence each, not a paragraph rehash)
- Policy implications: state concretely
- Limitations: state the scope constraints from `research_context.md` honestly
- Future work: 2-3 concrete directions, not vague gestures

---

## Style Rules

These rules apply to all sections.

### Prose

- Flowing academic prose in paragraphs; no bullet points in the manuscript
- No em-dashes; use commas, semicolons, or parentheses instead
- No bold text within paragraphs (bold is reserved for theorem/proposition labels)
- Active voice for the paper's contributions ("We show that..."); passive voice acceptable for describing others' work or methods
- Present tense for general claims and model properties; past tense for specific empirical findings
- "which" for non-restrictive clauses (with comma); "that" for restrictive clauses (no comma)
- Spell out numbers one through nine; numerals for 10 and above
- First person plural ("we") throughout; never "I" or "the authors"

### Citations

- `\citet{author2024}` when the author is the grammatical subject: "\citet{smith2024} show that..."
- `\citep{author2024}` for parenthetical references: "...as shown in prior work \citep{smith2024}"
- `\citet{author2024a, author2024b}` for multiple in-text citations
- Never write author-year citations manually; always use `\citet{}` or `\citep{}`

### Mathematics

- Display equations: `\begin{equation}...\end{equation}` for single equations, `\begin{align}...\end{align}` for multi-line
- Every display equation gets a `\label{eq:descriptive-name}`
- Inline math for short expressions
- Use `\text{}` inside math for subscript words: $c_{\text{P}}$ not $c_P$
- Parentheses: `\left(` and `\right)` for expressions that vary in height
- Operators: `\max`, `\min`, `\arg\max`, `\mathbb{E}` (never italic versions)

### LaTeX Conventions

- Use `\section{}`, `\subsection{}` — never `\paragraph{}` or manual bold headers
- Tables: `\begin{table}[t]` with `\caption{}` above the tabular, `\label{tab:...}` inside the caption
- Figures: `\begin{figure}[t]` with `\caption{}` below, `\label{fig:...}` inside the caption
- Reference as "Table~\ref{tab:...}" and "Figure~\ref{fig:...}" (capitalised, with non-breaking space)
- Propositions: `\begin{proposition}[Short title]\label{prop:...}` followed by `\begin{proof}` if proof is included
- No `\textbf{}` for emphasis in running text; use italics sparingly or restructure the sentence
- `\footnote{}` for tangential points; keep footnotes short

### Consistency Checks

Before producing any `.tex` file, verify:

- [ ] Every `\cite` key appears in the BibTeX file (or flag as missing)
- [ ] Every `\ref` and `\eqref` points to a defined `\label`
- [ ] Notation matches `model_equations.md` (variable names, subscripts, operator conventions)
- [ ] No orphaned claims (quantitative statements without table/figure/proposition reference)
- [ ] Section transitions are smooth (the last paragraph of each section should motivate the next)
- [ ] The introduction's contribution list matches what the body actually delivers

---

## Output

One or more `.tex` files in `paper/sections/`, written to or updated in place.

This skill produces LaTeX source only. It does not compile the document. If the project uses a build system (Quarto, Makefile, justfile), compilation is handled separately.

---

## Anti-patterns

Do not:

- Reorganise the literature review's analytical structure (the Literature Guardian defined it; this skill formats it)
- Invent model results or propositions (those come from the Theory Builder via `model_equations.md`)
- Use `\textbf{}` for section-like headers within the body text
- Write bullet-point lists in the manuscript (convert to prose)
- Include raw code, filenames, or pipeline references in the manuscript text
- Use em-dashes anywhere in the manuscript
- Write "as shown above" or "as mentioned earlier" without a specific cross-reference
- Leave `\cite{???}` placeholders without flagging them for the human

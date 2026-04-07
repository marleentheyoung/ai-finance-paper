---
name: manuscript-layout
description: Layout and formatting standards for a top-journal theory paper manuscript. Use when checking or fixing abstract structure, section balance, equation density, paragraph length, LaTeX conventions, and submission formatting. Referenced by presentation-lens and paper-writer (Improvement Pass).
---

# Manuscript Layout Skill

## Purpose

Define the concrete layout and formatting standards for a formal theory paper targeting a top-5 journal in the relevant field. These are measurable targets, not aspirational guidelines.

---

## Abstract

**Structure (5 sentences):**
1. The economic problem and why it matters (no equations, no citations)
2. What this paper does: the approach or mechanism in one sentence
3. Main result 1: stated as a concrete finding with the key object (threshold, comparative static, characterisation)
4. Main result 2 (or: the interaction / integrating result)
5. Implication: one policy or welfare takeaway

**Length:** 100–150 words. Hard maximum 200 words.
**No equations.** Inline variable names are acceptable. Full equations are not.
**No citations.**

---

## Section Length Targets

For a 40–50 page main text (double-spaced, 12pt, 1-inch margins = ~250 words per page = ~10,000–12,500 words):

| Section | Target word range | Notes |
|---------|------------------|-------|
| Introduction | 1,500–2,000 | No more; use footnotes for excess detail |
| Literature Review | 1,000–1,500 | Positioning only; not a full survey |
| Model Primitives | 800–1,200 | Signal structure, agent types, timing |
| Each component section | 1,000–1,500 each | Setup + proposition + interpretation |
| Integrating section | 1,200–1,800 | The core contribution; can be longer |
| Extensions | 800–1,200 | Framed as natural extensions |
| Empirics | 800–1,200 | Motivating only; not full empirical section |
| Conclusion | 500–700 | Concise restatement; not a summary |

Total target: **~10,000–12,500 words** (main text, excluding references and appendix).

---

## Equation Density Standards

**Per-section limit:** No more than 8 displayed equations per section in the main text. Derivations beyond this belong in an appendix.

**Prose requirement:** Every displayed equation must be followed by at least one sentence of interpretive prose before the next displayed equation appears.

**Consecutive equations:** No more than 2 displayed equations in a row without an intervening prose sentence.

**First page rule:** The first page of any section must be mostly prose. Do not open a section with a displayed equation in the first 10 lines.

**Appendix rule:** Proof details, extended derivations, and auxiliary lemmas belong in an appendix. The main text states the proposition and proof sketch only.

---

## Paragraph Structure

**Length:** 100–200 words is the optimal range. Flag paragraphs over 250 words for splitting.
**Minimum:** 3 sentences. Single-sentence paragraphs are structural fragments; merge or expand.
**Opening sentence:** Every paragraph's first sentence signals what the paragraph is about.
**One point per paragraph.** If a paragraph makes two distinct points, split it.

---

## Introduction Structure (strict)

1. **Opening paragraph** (3–5 sentences): the economic problem; why it matters now; the gap this paper fills. No equations. No citations to prior work in the first paragraph.
2. **What this paper does** (1–2 paragraphs): the approach, the model structure, the key components. One or two key equations may appear here.
3. **Main results** (1–2 paragraphs): each contribution as a concrete finding. "We show that..." not "We study...". State the threshold, the comparative static, or the characterisation explicitly.
4. **Related literature** (2–3 paragraphs): engage the 3–5 closest papers by name with mechanism-level differentiators. Not a full survey.
5. **Paper organisation** (1 paragraph): one sentence per section. Last sentence only.

Total introduction length: 1,500–2,000 words.

---

## LaTeX Conventions

### Spacing and margins
- `\documentclass[12pt]{article}` with `\geometry{margin=1in}` and `\doublespacing`
- Do not override spacing locally in any section file

### Floats
- Tables: `\begin{table}[t]` (top of page). Caption above the tabular. Label inside caption.
- Figures: `\begin{figure}[t]`. Caption below the figure. Label inside caption.
- Never use `[h]`, `[H]`, or `[!h]` — these force awkward placement in double-spaced manuscripts
- Reference as `Table~\ref{tab:...}` and `Figure~\ref{fig:...}` (capital letter, non-breaking space)

### Equations
- Single equation: `\begin{equation}\label{eq:name}\end{equation}`
- Multi-line: `\begin{align}...\end{align}` with `\label` on the last line or on each numbered line
- Reference as `\eqref{eq:name}` (not `(\ref{eq:name})`)
- Never use `$$...$$` (use `equation` environment instead)

### Propositions
```latex
\begin{proposition}[Short descriptive title]
\label{prop:name}
Statement of the proposition.
\end{proposition}
\begin{proof}[Proof sketch]
Key steps.
\end{proof}
```

### Cross-references
- Always use `~\ref{}` and `~\eqref{}` (non-breaking space before the reference)
- Capitalise when used as a noun: "Proposition~\ref{prop:...}", "Section~\ref{sec:...}", "Equation~\eqref{eq:...}"

### Footnotes
- Maximum 50 words per footnote. Longer material belongs in the text or appendix.
- Do not use footnotes to hide important results or assumptions.

---

## Prohibited Patterns

- Em-dashes anywhere in the manuscript (`---` or `\textemdash`)
- Bold text within paragraphs (`\textbf{}` is for proposition labels only)
- Bullet points or itemised lists in the manuscript body
- Manual author-year citations (written as plain text instead of `\citet{}` / `\citep{}`)
- `\paragraph{}` headers within sections (use `\subsection{}` or prose transitions instead)
- Equations in the abstract
- Citations in the abstract
- "In this paper, we..." as an opening sentence (start with the economic phenomenon)
- "The rest of the paper is organised as follows:" (use "Section X introduces..." instead, or restructure)

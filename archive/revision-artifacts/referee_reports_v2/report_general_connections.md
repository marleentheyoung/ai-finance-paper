# General Referee Report — Logical Connections (Citation Graph Audit)
Date: 2026-03-12
Mode: connections
Sections reviewed: introduction.tex, model.tex, channel1.tex, channel2.tex, channel3.tex, amplification.tex, extensions.tex, conclusion.tex, literature.tex, context/model_equations.md, context/research_plan_final.md, context/threat_map_final.md

## What Works

The paper's citation practice is above average for the subfield. The introduction names the two closest predecessors (Danielsson-Uthemann 2025; Yang 2024) and states precise, multi-dimensional differentiators for each. The dedicated literature review (Section 2) is organised by channel, which mirrors the paper's own structure and makes intellectual lineage traceable. The Danielsson-Shin-Zigrand (2012) nesting result (Proposition 7) is an exemplary case of engaged citation: the paper formally demonstrates that a predecessor is a limiting case, making the relationship verifiable rather than asserted.

## Summary

The paper engages meaningfully with its core predecessors but has a significant gap between the technical sections (Channels 1-3, amplification, extensions) and the literature section: most citations in the technical sections are engaged, while the literature section contains substantial catalogue-style listing. Several important intellectual chains are incomplete (Morris-Shin to Hellwig to Goldstein-Pauzner is implicit but never stated as a chain; Kyle-Glosten-Milgrom relationship is unacknowledged). The extensions and amplification sections are nearly citation-free, which is defensible for the amplification section (novel contribution) but problematic for the extensions section (prisoner's dilemma in adoption has predecessors in technology adoption and network externality literatures that are not acknowledged). Three to four missing references would be expected by a knowledgeable referee.

## Issues

### Priority 1 — Blocking (must fix before submission)

| ID   | File | Location | Issue | Why it matters |
|------|------|----------|-------|----------------|
| G-01 | extensions.tex | Entire section | Zero citations in the extensions section. The prisoner's dilemma in AI adoption (Proposition 10) cites no predecessor for the tracking error motive, the strategic complementarity in adoption, or the diversity mandate concept. The technology adoption externality literature (Katz-Shapiro 1985, Farrell-Saloner 1985), network effects literature, and the Gans (2023) AI adoption paper cited in the literature review are not referenced where the model is actually developed. | A referee will question whether the authors are aware of the adoption externality literature. The prisoner's dilemma structure has well-known antecedents; not citing them suggests either ignorance or deliberate avoidance, neither of which is a good signal. |
| G-02 | literature.tex | Section 5 (Cross-Channel) | The cross-channel interaction subsection lists Kleinberg-Raghavan (2021), Peng et al. (2024), and Gans (2023) in a parenthetical cluster with no stated relationship to the paper's argument. These are orphan citations -- each appears exactly once, in a list, with no sentence explaining what the paper does or why it matters here. | At a top journal, every citation must earn its place. Parenthetical name-dropping without engagement is the hallmark of a paper that is padding its reference list rather than mapping its intellectual terrain. Either engage with each (one sentence per paper stating the relationship) or remove them. |

### Priority 2 — Important (fix in this revision cycle)

| ID   | File | Location | Issue | Why it matters |
|------|------|----------|-------|----------------|
| G-03 | channel3.tex | Lines 16, 53, 95 | Kyle (1985) and Glosten-Milgrom (1985) are cited together as "foundational models" but their intellectual relationship is never stated. Kyle models a single informed trader with a market maker; Glosten-Milgrom model a competitive specialist with heterogeneous traders. The two papers solve related but distinct problems. A reader seeing both cited as "foundational" without explanation cannot understand which foundation is being used where. | Chain completeness failure. These are among the most cited papers in financial economics. A referee in microstructure will expect the paper to acknowledge the distinction and state which model's structure is inherited by Channel 3. The Avellaneda-Stoikov framework descends primarily from the Kyle tradition (inventory management, not adverse selection per se); this lineage should be stated. |
| G-04 | channel1.tex, literature.tex | Multiple | The intellectual chain Morris-Shin (1998/2002) -> Hellwig (2002) -> Goldstein-Pauzner (2005) is the backbone of Channel 1, but it is never stated as a chain. Morris-Shin established uniqueness; Hellwig showed public information breaks it; Goldstein-Pauzner applied the framework to bank runs. The paper cites all three but leaves the reader to reconstruct the chain. | A reader unfamiliar with the global games literature cannot follow the logical progression without this chain being explicit. The paper's own contribution (rho converts private signals into effective public signals, activating Hellwig's result in the Goldstein-Pauzner setting) only makes sense against this chain. State it in one sentence at the beginning of Channel 1. |
| G-05 | amplification.tex | Entire section | The amplification section contains exactly one economic citation: Danielsson (2022) in the safety illusion discussion (line 111). The Brouwer fixed-point theorem is invoked without citing a source; the Ostrowski theorem is cited to Ortega-Rheinboldt (1970); the Guckenheimer-Holmes (1983) bifurcation reference appears in the proof sketch. No economic papers on amplification mechanisms are cited. The positive feedback loop (liquidity withdrawal -> signal correlation -> crisis -> information collapse -> liquidity withdrawal) has antecedents in the amplification/contagion literature (Allen-Gale 2000; Brunnermeier-Pedersen 2009 for margin spirals; Shleifer-Vishny 1997 for limits of arbitrage). None are cited in this section. | The amplification loop is the paper's centrepiece. A referee will ask: how does this feedback mechanism relate to existing amplification mechanisms? The paper should position the loop relative to Brunnermeier-Pedersen (2009) margin spirals and other feedback mechanisms, even if the formal structure is novel. |
| G-06 | channel2.tex | Lines 6, 18 | The Grossman-Stiglitz (1980) citation in Channel 2 setup is engaged (the paper states it extends GS with two information types). However, the relationship to Verrecchia (1982), who first derived the GS equilibrium with a continuum of agents and Gaussian signals (the exact setup used here), is absent. A referee familiar with the rational expectations literature will notice this gap. | Missing reference. Verrecchia (1982) is the standard reference for the CARA-normal GS equilibrium with a continuum of agents. The paper uses this exact setup but cites only GS (1980), which uses a two-agent model. |
| G-07 | literature.tex | Subsection 2 (Information) | Vives (2014) is cited with an engaged relationship: "a privately revealing equilibrium obtains when correlation in traders' valuations is not too large; AI-driven signal correlation progressively violates this condition." However, the specific condition from Vives that is violated is never stated. This makes the engagement imprecise -- the reader cannot verify the claim without reading Vives. | Vague engagement. "Progressively violates this condition" -- which condition? State the specific bound (e.g., on the correlation of private values) and explain how rho maps to it. |
| G-08 | literature.tex | Subsection 2 (Information) | Banerjee-Davis-Gondhi (2018) is cited with a stated mechanism ("greater transparency can paradoxically reduce informativeness") but the relationship to the present paper's mechanism is listed, not engaged. The sentence describes what BDG do but not how this paper relates to, extends, or differs from BDG. | Listed rather than engaged. One additional sentence stating the specific relationship (e.g., "Our Channel 2 mechanism is distinct: BDG's paradox operates through composition of learning targets, while ours operates through cross-sectional signal correlation") would convert this from listed to engaged. |

### Priority 3 — Minor (fix if time permits)

| ID   | File | Location | Issue | Why it matters |
|------|------|----------|-------|----------------|
| G-09 | introduction.tex | Line 38 | Hansen-Lee (2025) is cited with an engaged relationship ("find that independently queried AI agents reduce herding, consistent with the low-rho regime; they do not test the high-rho regime"). This is good engagement. However, the citation appears only in the introduction, not in Channel 1 where the non-monotonicity is formally established. | Citation placement. The Hansen-Lee finding directly supports the "wisdom of AI" effect at low rho (Proposition 2). It should appear in Channel 1 near the non-monotonicity discussion, not only in the introduction. |
| G-10 | model.tex | Line 20 | Morris-Shin (1998) is cited as the "heterogeneous-signal benchmark" at rho = 0. This is correct but the paper cites "morris1998" while Morris-Shin (2002) ("Social Value of Public Information") is more directly relevant to the rho > 0 case (public information effects). The 2002 paper is cited elsewhere but not here, where the rho = 0 benchmark is introduced. | Minor precision issue. When introducing the benchmark, cite both 1998 (uniqueness) and 2002 (social value of public information) to signal that the paper is aware of both dimensions. |
| G-11 | channel3.tex | Line 77 | Pagano (1989) is cited for the "low-liquidity trap" analogy. The relationship is stated as an analogy ("analogous to") but the specific element inherited from Pagano -- the coordination failure in market participation where low expected liquidity deters entry, validating the low-liquidity expectation -- is not explained. | Vague connector. "Analogous to" does not state which specific element is analogous. A single clause would suffice: "analogous to the Pagano (1989) low-liquidity trap, where the expectation of thin markets deters participation, validating the expectation." |
| G-12 | channel2.tex | Line 27 | The footnote defining k_A and k_P references "the standard Kyle-type model" without a citation. Kyle (1985) is cited in Channel 3 but not in Channel 2, despite the linear equilibrium demand schedules being Kyle-derived. | Minor omission. Add a Kyle (1985) citation to the footnote. |
| G-13 | conclusion.tex | Line 16 | Acemoglu-Ozdaglar-Tahbaz-Salehi (2015) is cited for network topology and balance sheet linkages. This is the only citation of this paper in the entire manuscript. The relationship is stated ("the model abstracts from network topology") but the specific dimension of Acemoglu et al. that is relevant (whether network structure amplifies or dampens cascades depending on connectivity) is not stated. | Orphan citation with vague relationship. Either engage (one sentence on what Acemoglu et al. show about network topology that would interact with the rho mechanism) or remove. |
| G-14 | literature.tex | Subsection 2 | Farboodi-Matray-Veldkamp-Venkateswaran (2022) is cited in a catalogue sentence ("document that data technology concentrates information on large firms") without a stated relationship to the present paper. | Listed, not engaged. State the specific relationship: does the concentration of data on large firms increase or decrease rho for those firms? This would connect the empirical finding to the theoretical primitive. |

## Citation Engagement Summary Table

| Section | Total unique citations | Engaged | Listed | Engagement rate |
|---------|----------------------|---------|--------|----------------|
| Introduction (Sec. 1) | 16 | 14 | 2 | 88% |
| Model (Sec. 3) | 5 | 5 | 0 | 100% |
| Channel 1 (Sec. 4) | 7 | 7 | 0 | 100% |
| Channel 2 (Sec. 5) | 5 | 4 | 1 | 80% |
| Channel 3 (Sec. 6) | 7 | 6 | 1 | 86% |
| Amplification (Sec. 7) | 1 | 1 | 0 | 100% |
| Extensions (Sec. 8) | 0 | 0 | 0 | N/A |
| Conclusion (Sec. 10) | 2 | 1 | 1 | 50% |
| Literature Review (Sec. 2) | 28 | 19 | 9 | 68% |
| **Total (unique across paper)** | **~35** | **~26** | **~9** | **~74%** |

Notes on counting: Citations appearing in multiple sections are counted once per section. The introduction has the highest raw citation count and the literature review has the highest absolute number of listed citations. The technical sections (model, channels, amplification) have excellent engagement rates. The literature review section brings the overall rate down due to catalogue-style listing in the information acquisition and AI subsections.

## Flagged Issues Table

| Category | ID | Citation(s) | Section | Nature of problem |
|----------|-----|-------------|---------|-------------------|
| Orphan citation | G-02 | Kleinberg-Raghavan (2021), Peng et al. (2024), Gans (2023) | literature.tex S5 | Appear once in a parenthetical list with no stated relationship |
| Orphan citation | G-13 | Acemoglu et al. (2015) | conclusion.tex | Appears once with vague relationship ("abstracts from") |
| Orphan citation | G-14 | Farboodi et al. (2022) | literature.tex S2 | Catalogue sentence, no stated relationship to rho |
| Missing reference | G-06 | Verrecchia (1982) | channel2.tex | Standard CARA-normal GS derivation reference absent |
| Missing reference | G-05 | Allen-Gale (2000), Shleifer-Vishny (1997) | amplification.tex | Feedback/amplification literature absent from the amplification section |
| Missing reference | G-01 | Katz-Shapiro (1985), Farrell-Saloner (1985) | extensions.tex | Technology adoption externality literature absent from adoption game |
| Broken chain | G-04 | Morris-Shin -> Hellwig -> Goldstein-Pauzner | channel1.tex | Chain never stated explicitly; reader must reconstruct |
| Broken chain | G-03 | Kyle (1985) vs. Glosten-Milgrom (1985) | channel3.tex | Both cited as "foundational" without distinguishing their roles |
| Vague connector | G-07 | Vives (2014) | literature.tex S2 | "Progressively violates this condition" -- which condition? |
| Vague connector | G-08 | Banerjee-Davis-Gondhi (2018) | literature.tex S2 | Described but not related to the present paper |
| Vague connector | G-11 | Pagano (1989) | channel3.tex | "Analogous to" without stating the specific analogy |
| Citation-free section | G-01 | N/A | extensions.tex | Entire section has zero citations |
| Citation-sparse section | G-05 | Danielsson (2022) only | amplification.tex | One economic citation in the paper's centrepiece section |

## Self-Positioning Assessment

The paper's self-positioning in the introduction is strong. The two closest predecessors (Danielsson-Uthemann 2025; Yang 2024) are named, and three specific dimensions of differentiation are stated for each. The distinction between the extensive margin (mu) and intensive margin (rho) is precise and falsifiable. The introduction also names Hansen-Lee (2025) as a boundary condition that supports the non-monotonicity claim, which is an effective use of a potential counterargument.

The positioning weakens in the body of the paper. Channel 1 positions against Danielsson-Uthemann clearly (the numerical comparison in Section 4.3 is effective). Channel 2 positions against Dugast-Foucault (temporal vs. cross-sectional dimension) clearly. Channel 3 positions against Cespa-Vives (opacity vs. algorithmic similarity) clearly. The amplification section does not position itself against any existing amplification mechanism, which is the most significant positioning gap. A referee will ask: how is this feedback loop different from Brunnermeier-Pedersen margin spirals, from the Allen-Gale contagion channel, or from the Shleifer-Vishny limits-of-arbitrage feedback? The answer is likely "the trigger is information homogeneity rather than funding constraints or network links," but this must be stated.

The extensions section positions the diversity mandate against Danielsson (2022) qualitative recommendations but does not position the adoption game against any predecessor, which is a gap given that technology adoption externalities have a substantial literature.

## Overall Assessment

The paper maps its intellectual terrain competently in the introduction and technical sections, where engagement rates are high (80-100%) and the key differentiators are precise. The literature review section, while comprehensive in coverage, contains too much catalogue-style listing (9 of 28 citations are listed rather than engaged, a 32% listing rate). The most serious gaps are structural: the extensions section is citation-free, the amplification section has only one economic citation, and several important intellectual chains (Morris-Shin -> Hellwig -> Goldstein-Pauzner; the relationship between Kyle and Glosten-Milgrom) are left implicit.

The missing references (Verrecchia 1982; adoption externality literature) and orphan citations (Kleinberg-Raghavan, Peng et al., Gans, Acemoglu et al.) are individually minor but collectively suggest that the citation practice becomes less careful in the later sections and the literature review's "broader context" paragraphs. A top-journal referee will notice this pattern.

## Recommendation
MAJOR REVISION

The citation engagement in the core technical sections is strong, and the self-positioning against the two closest competitors is precise and well-executed. However, the citation-free extensions section, the citation-sparse amplification section, the orphan citations, and the missing intellectual chains constitute a pattern of declining care in the paper's later sections. These issues are fixable in a single revision cycle but are numerous enough to warrant major rather than minor revision from the connections perspective. The most important fix is adding economic positioning to the amplification and extensions sections -- these are the paper's two most novel contributions, and they are the least well-positioned in the existing literature.

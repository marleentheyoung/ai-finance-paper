# Referee C Report -- Literature and Framing
Date: 2026-03-11

## Summary

The manuscript's literature engagement is now comprehensive. All 38 threat map papers are cited, the five contributions are each backed by named propositions, and the differentiators against the four required competitor papers are stated at the mechanism level. The previous round's issues (missing Margaretic-Pasten, missing Barucca-Morone, FPE non-monotonicity omission in Channel 2 summary, plain-text Pagano citation, incomplete D-U three-part differentiator) have all been addressed. Two new issues emerge: a citation integrity problem with the Barucca-Morone (2025) bib entry whose title and journal do not match the threat map source, and a missing qualifier on the RPE monotonicity claim.

## Issues

### Priority 1 -- Blocking (must fix before submission)

| ID  | Location | Issue | Evidence |
|-----|----------|-------|----------|
| C1  | references.bib lines 388-394 | The Barucca-Morone (2025) bib entry has title "AI in Financial Risk Management: A Survey" in journal "Journal of Financial Risk Management (Forthcoming)." The threat map records this paper as "How Low-Cost AI Universal Approximators Reshape Market Efficiency," arXiv 2501.07489. The title, journal, and paper description are all inconsistent. The bib entry appears to describe a different paper or contains fabricated metadata. A referee who looks up arXiv 2501.07489 will find a paper with a different title than the one cited, which is a serious credibility issue. | threat_map_final.md: "Barucca and Morone (2025) -- How Low-Cost AI Universal Approximators Reshape Market Efficiency, arXiv 2501.07489" |
| C2  | literature.tex line 26 | The description of Barucca-Morone (2025) as "a recent survey of AI applications in financial risk management, contextualising the rapid adoption of shared model architectures" does not match the threat map characterisation: "Discusses how AI as universal approximators pushes markets toward a generalized notion of efficiency. Argues that cheap AI enables increasingly sophisticated strategies." The manuscript describes a survey of risk management applications; the actual paper discusses universal approximators and market efficiency. These are substantively different characterisations. | threat_map_final.md engagement strategy: "Reference as part of the emerging literature on AI and market efficiency, but note the absence of formal modelling of the signal correlation mechanism." |

### Priority 2 -- Important

| ID  | Location | Issue | Evidence |
|-----|----------|-------|----------|
| C3  | introduction.tex line 14 | The claim "revelatory price efficiency is monotonically decreasing in rho" omits the qualifier "for c_P > 0" that appears in Proposition prop:rpe (channel2.tex line 71). The same omission occurs at line 30 ("Revelatory price efficiency...is monotonically decreasing in rho"). Without the positive-cost qualifier, the result is either trivial or undefined when no private research exists. A theory referee will flag this. | channel2.tex Proposition prop:rpe part (ii): "which is monotonically decreasing in rho for c_P > 0" |

### Priority 3 -- Minor

| ID  | Location | Issue | Evidence |
|-----|----------|-------|----------|
| C4  | introduction.tex line 38 | The Hellwig-integration distinction against Danielsson-Uthemann (2025) remains implicit rather than explicit. The threat map records that D-U "discuss [the Hellwig 2002 multiplicity result] qualitatively (Section 2.2.2) but derive theta*(mu) under standard Morris-Shin uniqueness conditions." The introduction states that "we apply the Hellwig result" and that D-U use a different primitive (mu), but does not explicitly say that D-U do not integrate Hellwig into their formal model. The current framing is adequate but a single clause would sharpen the distinction. | threat_map_final.md Danielsson-Uthemann differentiator part (2): "Does not integrate Hellwig (2002) multiplicity result into the formal model. Discusses it qualitatively (Section 2.2.2) but derives theta*(mu) under standard Morris-Shin uniqueness conditions." |

## Missing Citations

All papers in threat_map_final.md and literature_review.md are now cited in the manuscript. No missing citations.

## Differentiator Gaps

1. **Barucca-Morone (2025) characterisation mismatch**: The manuscript's description of this paper does not match the threat map's characterisation. The threat map says the paper discusses AI as universal approximators and market efficiency in the Grossman-Stiglitz tradition; the manuscript calls it a survey of AI in financial risk management. This is not a differentiator gap per se but a mischaracterisation of a cited paper, which is arguably worse. Flagged as C1/C2 above.

2. **Danielsson-Uthemann (2025) Hellwig integration**: Part (2) of the three-part differentiator is implicit. See C4 above. Not blocking but a missed opportunity to strengthen the positioning.

All other differentiators match or exceed the threat map's recorded distinctions.

## Citation Integrity Flags

| Key | Location | Issue |
|-----|----------|-------|
| barucca2025 | references.bib lines 388-394 | Title "AI in Financial Risk Management: A Survey" and journal "Journal of Financial Risk Management" do not match the threat map source (arXiv 2501.07489, titled "How Low-Cost AI Universal Approximators Reshape Market Efficiency"). The bib entry must be corrected to match the actual paper. |

All other citation keys in introduction.tex, literature.tex, and conclusion.tex exist in references.bib with correct author-year combinations consistent with the threat map. No hallucinated citations detected beyond the Barucca-Morone metadata issue.

## Recommendation
MINOR REVISION
The Barucca-Morone (2025) citation integrity issue (C1, C2) is the only blocking problem and is mechanically fixable: correct the bib entry to match arXiv 2501.07489 and revise the one-sentence characterisation in literature.tex. The RPE qualifier (C3) requires adding three words. The Hellwig-integration distinction (C4) is a polish item. No structural framing problems, no overclaims, and no missing citations remain.

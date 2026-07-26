# Extended media-reconstruction manuscript

The file `aura-file-defender-extended.tex` is the dissertation-oriented main
article on the transport-independent method of policy-indexed media
reconstruction and fail-closed publication. Aura File Defender is the reference
implementation rather than the scientific scope of the method. The release
layout is the ordinary single-column Elsevier preprint format at 12 pt and is
capped at 55 A4 pages. The current build is 55 pages including references. The
10-page `aura-file-defender.tex` remains the concise journal manuscript.

The main article uses the consolidated files in `extended/compact/` for the
front half and discussion, while retaining the full technical format,
isolation, implementation, corpus, and evaluation sections. Field-level policy
and format registers, the 34-scenario catalogue, and the reproducibility
checklist build separately as `aura-file-defender-supplement.tex`.

The extended version separates behavioral malware terminology from measurable
carrier properties. Controlled outcome values must come only from
`results/generated-results.tex` after a run reports
`release_eligibility.eligible=true`. Release-ineligible experimental
observations are isolated in `results/server-experiment-results.tex`; they may
document exact finite-corpus, differential, fidelity, fault, fuzz, and
performance outcomes but cannot populate controlled outcome fields or authorize
population, capacity, or release claims. The current bounded package contains
no paired mechanism-ablation stream, so it also authorizes no isolated
mechanism-contribution claim.

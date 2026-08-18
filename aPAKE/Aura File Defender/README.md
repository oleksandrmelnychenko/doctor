# Aura File Defender manuscript

Current title: **Policy-Indexed Authorization for Canonical Reconstruction and
Fail-Closed Delivery of Untrusted Media**.

The manuscript is a methods-and-evaluation paper. Its novelty is the composed
acceptance method at the endpoint boundary, not a claim that a new codec or a
universal antivirus classifier has been invented.

## Target structure

1. Introduction and research gap.
2. Related work and claim boundary.
3. System and adversary model.
4. Canonical reconstruction method.
5. Format profiles and polyglot handling.
6. Implementation and process isolation.
7. Evaluation protocol and results.
8. Discussion, limitations, and conclusion.

The extended manuscript PDF is 23 A4 pages including references in the
two-column Elsevier 5p layout. The related-work section is grounded in
source-by-source verified IEEE, ACM, USENIX, NIST, RFC, and W3C publications.
Retained finite observations are reported with explicit evidence boundaries.
Controlled, population, capacity, and release claims remain pending until the
complete scientific gate passes.

## Editorial formats

- `aura-file-defender-extended.tex` and its 23-page PDF remain the authoritative
  two-column manuscript.
- `aura-file-defender-extended.docx` is a visually verified 23-page A4
  scientific-layout copy. Its title block and abstract are full width; the
  body and references use two columns; and all 13 tables and 7 figures retain
  full-width sections. Word equation objects, clickable links, numbered
  references, and human-readable internal references are preserved.
- `aura-file-defender-extended.md` is the semantic interchange copy. Its
  relative figure links resolve through `word-assets/`; a tested Pandoc
  round-trip retains all 13 tables and 7 figures without conversion warnings.

The Word and Markdown files are derived snapshots for editing and exchange;
scientific changes must be reconciled back into the LaTeX source before the
submission PDF is regenerated.

## Scientific contribution to keep explicit

- Symmetric endpoint placement before encryption and after decryption while the
  relay remains blind.
- Concrete convergence of portable name, parsed media type, and byte-derived
  format profile.
- A reconstruction-strength order that prevents structural fallback when the
  policy requires semantic reconstruction.
- Independent complete output parsing as the delivery authorization boundary.
- Clean-only publication across Rust, filesystem, C, and Swift interfaces.
- A preregistered, schema-valid evidence chain that separates carrier
  properties, parser behavior, fidelity, and performance.

## Results rule

`results/generated-results.tex` supplies controlled-release values only after a
completed run whose `run-manifest.json` has
`release_eligibility.eligible=true`. Versioned finite observations retained in
`results/server-experiment-results.tex` may enter the manuscript only with
their run identity, denominator, and release-ineligible boundary. Laptop
measurements and unbound ad hoc counts must not enter the paper.

## Independent review

The next evidence dependency is two-cluster independent review of the frozen
public-source packet. The author-side materials are:

- [reviewer/README.md](reviewer/README.md): packet identity and evidence
  boundary;
- [reviewer/INVITATION.md](reviewer/INVITATION.md): copy-paste reviewer
  invitation;
- [reviewer/RUNBOOK.md](reviewer/RUNBOOK.md): offline verification, decision,
  Ed25519 signing, and return procedure;
- [reviewer/REVIEWER-TRACKER.md](reviewer/REVIEWER-TRACKER.md): two-reviewer
  independence and return-bundle status;
- [reviewer/SERVER-PUBLISH-TASK.md](reviewer/SERVER-PUBLISH-TASK.md):
  completed off-server private-prerelease publication record.

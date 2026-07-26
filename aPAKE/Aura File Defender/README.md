# Aura File Defender paper plan

Working title: **Aura File Defender: Endpoint-Local Canonical Reconstruction of
Media Attachments in End-to-End Encrypted Messaging**.

The manuscript is a methods-and-evaluation paper. Its novelty is the composed
acceptance method at the endpoint boundary, not a claim that a new codec or a
universal antivirus classifier has been invented.

## Target structure and page budget

1. Introduction and research gap: 1.0 page.
2. Related work and claim boundary: 1.25 pages.
3. System and adversary model: 0.75 page.
4. Canonical reconstruction method: 2.0 pages.
5. Format profiles and polyglot handling: 1.25 pages.
6. Implementation and process isolation: 1.0 page.
7. Evaluation protocol and results: 1.75 pages.
8. Discussion, limitations, and conclusion: 1.0 page.

The current drafting PDF is ten journal pages including references. The
related-work section is grounded in source-by-source verified IEEE, ACM,
USENIX, NIST, RFC, and W3C publications. Empirical cells remain intentionally
pending until the controlled server run passes the complete release gate.

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

Only `results/generated-results.tex` may supply empirical values. It must be
generated from a completed run whose `run-manifest.json` has
`release_eligibility.eligible=true`. Laptop measurements and ad hoc corpus
counts must not enter the paper.

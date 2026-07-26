# Critical Review — *A Policy-Indexed Method for Canonical Reconstruction and Fail-Closed Delivery of Untrusted Media* (Aura File Defender, extended)

Reviewed source: `aura-file-defender-extended.tex` and all `\input` sections (compact 01–08 + full sections 11–16), plus `results/server-experiment-results.tex`. Reviewed revision `823a5ec7a0dd`. This is a reviewer-style report; it makes no edits to the manuscript.

---

## 1. One-paragraph summary

The paper defines a transport-independent authorization method for admitting untrusted media at a local trust boundary. Evidence from filename, declared media type, and a bounded byte probe must converge on exactly one source profile; a policy-selected reconstruction level (`NotProcessed ≺ Structural ≺ Semantic`) is performed; the complete candidate is validated by an authorizing parser on a code path separate from construction; and only a `Clean` verdict may be published, non-overwriting. Two analytical results are offered (conditional delivery; post-reconstruction monotonicity) and a deliberately release-*ineligible* bounded experiment over 104 synthetic records is reported.

## 2. Overall assessment

The manuscript's greatest strength is also the frame for its greatest weakness: it is unusually **honest about what it has not shown**. The formal boundary between *structural* reconstruction (retains codec payload; cannot claim payload neutralization) and *semantic* reconstruction (serialized from a decoded buffer) is genuinely well-drawn and is the paper's most valuable idea. But the **empirical contribution is close to vacuous for the security thesis**: the experiment exercises none of the adversarially interesting corpus strata, and the analytical results are largely definitional. The paper is publishable as a *method-and-protocol* paper only if it stops presenting the bounded experiment as evidence for the threat model and either (a) proves the formal results properly, or (b) runs the strata the method is actually about.

**Recommendation:** Major revision. The honesty is commendable and rare; the substance behind the two headline claim-types (formal soundness, empirical fail-closed behavior) is not yet there.

---

## 3. Strengths

1. **Structural-vs-semantic reconstruction lattice with a policy floor** (`q_{p,s} ≤ ℓ`, Eq. reconstruction-order / level-satisfaction). The explicit refusal to let a well-formed *structural* candidate satisfy a *semantic* requirement — even when it parses cleanly — is the correct and non-obvious design choice, and Table `format-profile-comparison` states per-format exactly what survives a structural route. Most CDR literature blurs this; this paper does not.
2. **Validation on a code path separate from construction**, with the honest caveat that separation ≠ verification, and the reserved term "implementation-diverse validator" for the external tools. This terminological discipline is exactly right.
3. **Fail-closed postcondition is uniform**: every non-clean path (panic, timeout, cancellation, launch failure, ambiguity, validation failure) returns empty bytes and the digest of the empty string. This is a clean invariant (F8) and is traced to source.
4. **Reproducibility hygiene is strong**: frozen run IDs, commit hashes, policy SHA-256 digests, pinned external-tool versions (ImageMagick 6.9.12-98, FFprobe/libavformat 6.1.1, MediaInfo 24.01), append-only run discipline, and a release gate `G_sci` that the authors themselves report as **false**.
5. **Scope exclusions are stated plainly and repeatedly**: steganography, harmful decoded meaning, decoder-compromise host effects without an external sandbox, malware-family attribution. The paper does not overclaim "malware-free media."
6. **Internal arithmetic is fully consistent** (verified independently — see §7). Every count in the abstract, body, and results macros reconciles.

---

## 4. Major concerns

### M1. The experiment tests essentially none of the threat model.
The corpus contains only **S0 (50 canonical benign), S1 (30 noncanonical benign), and S6 (24 inert unsupported)**. The five security-relevant strata are **entirely absent**: S2 malformed/truncated, S3 classifier disagreement, S4 polyglots/prefix camouflage/trailing objects, S5 resource exhaustion, S7 parser/decoder regressions. The paper's entire thesis is fail-closed handling of malformed, ambiguous, polyglot, and resource-abuse carriers — and the experiment exercises **none** of them.

Consequently the headline "0/24 false acceptances" is over **inert, unsupported, media-policy-blocked** files (executables/scripts/archives), which the media-only allowlist rejects trivially and near-tautologically. It is not evidence that the method resists a single adversarial *media* carrier. The paper concedes this in the `G_sci`-false discussion, but the framing throughout the abstract/results ("all fixture-derived action oracles matched", "no publication-invariant violation") still reads as security corroboration. **State plainly, in the abstract, that the experiment validates the benign/usability and unsupported-block paths only, and exercises zero adversarial-media strata.**

### M2. Oracle circularity makes "104/104 agreement" near-tautological.
Expected actions were **generated by the fixtures**, so 104/104 agreement measures fixture↔policy consistency, not ground truth. The paper says this (§Deployment implications, and the results boundary column) — but it is the single most important caveat and it is buried. A canonical parser can share a misunderstanding with the handler that produced the fixture; the external tools can share a codec library (common-mode). The "match" is a consistency check, not a validation. Elevate this to the abstract and do not report the agreement as a result without the immediate qualifier.

### M3. The two formal results are definitional, not derived.
- **Conditional delivery** (`Accept ⇒ y ∈ L_{p,k}`): holds "if each configured authorizing parser is sound." Since `Accept` *contains* `Valid` (a conjunction of `CompleteOK`), and soundness is exactly `CompleteOK ⇒ membership`, the implication is immediate. The entire weight rests on an **unproven, unverified parser-soundness assumption** about hand-written Rust parsers. This is the crux of the whole security argument and it is assumed, not established. It should be foregrounded as *the* central limitation of the analytical contribution, not left as a conditional aside.
- **Post-reconstruction monotonicity** (Eq. validation-monotonicity): `p₂ ⊑ p₁` is **defined extensionally** ("every object accepted by p₂ is also admitted by p₁"). The stated implication `p₂ ⊑ p₁ ∧ PostOK_{p₂}(w) ⇒ PostOK_{p₁}(w)` is then a **restatement of that definition** applied to witness `w` — the "under monotone component predicates" qualifier and the syntactic list ("no larger scalar bounds, no weaker level, no broader language, no scan/publication bypass") do no work in the proof as written. The result that would carry content is the **converse grounding**: that those *syntactic* conditions (bounds ⊇, level ≤, language ⊆, scan/pub preserved) *imply* the extensional inclusion. That requires proving each component predicate is monotone under the ordering — including `ScanOK` (a larger signature set in `p₁` can *reject* what `p₂` accepted, so the direction of the signature-set ordering must be pinned down and shown compatible). This proof is **asserted, not given**. Fix by defining ⊑ syntactically and proving the extensional consequence, per predicate.

### M4. Half of all accepted outputs fail their fidelity profile — and the misses are large, not marginal.
`0/32` audio and `0/8` source-WebM passed fidelity (`40/80` overall). These are not near-threshold:
- **Audio duration drift 6.16–12.95%** against a **≤2%** bound — a 3–6× overshoot. A duration drift of this size on transcode strongly suggests an encoder-delay / padding / sample-rate handling defect in the `libmp3lame` semantic path (LAME encoder/decoder delay and padding are a classic source of exactly this magnitude of duration error). This looks like a concrete engineering bug, not an inherent usability trade-off.
- **WebM→MP4 SSIM 0.667–0.712** against **≥0.90** — a large perceptual-structure gap for a re-encode that should be visually near-lossless at reasonable settings.

The paper frames these as "operational limitations" and "security acceptance did not imply usability acceptance." That framing is fair *if* the numbers were near the bound; at 3–6× (audio) and a 0.2 SSIM deficit (video) they instead indicate the **semantic reconstruction pipeline as configured is producing materially degraded output**. This deserves diagnosis, not a footnote — and the abstract, which reports only "Fidelity passed for 40 accepted records," should also report that it **failed for the other 40**, including every audio and every video output.

### M5. Adversarial budgets are a fraction of the prespecified protocol.
- **Fuzzing**: executed 7 targets × ~30 s = **210 target-seconds** vs. the protocol's **3 × 1 h per target = 75,600 target-seconds** — i.e. **~0.3%** of budget. "7,299,439 executions, no crash" is ~35k exec/s, consistent with trivially small/fast inputs; at 0.3% of budget it is weak evidence. Report the fraction explicitly next to the execution count.
- **Fault schedule**: only **11 selected single-test** checks, not the full schedule; S5 (resource exhaustion) and the complete fault campaign are absent, so the availability/bounds claims (F6) are not empirically exercised at all.

### M6. Latency measurement is not controlled and cannot be a throughput claim.
Warm numbers come from **1,560 repeated, non-independent calls** (104 × 5 × 3) on a **shared host with 33 other active containers**, with **no bootstrap interval** (the protocol required 10⁴ hierarchical bootstrap replicates). The "7.94 sequential calls/s" is a single-worker service rate on a contended host, correctly caveated as "not concurrent capacity" — but given the contention it should not appear as a quantitative performance result at all, only as an order-of-magnitude observation (in-process ≪1 ms; external-codec paths ~229–357 ms).

### M7. Novelty relative to existing CDR is under-argued.
Commercial/academic content-disarm-and-reconstruction already performs canonical reconstruction and metadata stripping. The paper's stated differentiator is the *composition* of F1–F8 into one auditable authorization relation plus the reconstruction-strength floor. That is a real but modest contribution; the manuscript would be strengthened by a concrete, side-by-side statement of what a practitioner using an existing CDR product **cannot** express or guarantee that this method can (the F4 payload-independence claim and the semantic-floor refusal are the strongest candidates — lead with them).

---

## 5. Minor / technical concerns

- **F4 is verified by construction, not by observing the artifact.** Its oracle is a "source-to-candidate provenance trace," but byte-level provenance across a decode→re-encode can only be established by the *code path* (semantic handler serializes from the decoded buffer). That makes F4 effectively an F7-style structural property, in slight tension with the paper's recurring "validated independently of construction" theme. Acknowledge that F4 rests on construction.
- **Output diversity is small.** 80 accepted evaluations collapse to **40 unique output digests**; the differential gate therefore corroborates only 40 distinct artifacts. Note this diversity ceiling where the 40 figure is introduced.
- **GIF version-extension check is a known open gap** (§GIF method: the parser "does not couple extension use to the GIF89a signature"); it is listed as a release condition. Good that it is disclosed — but it means an 89a-only extension can currently ride on an 87a signature. Flag its severity.
- **Directory crash-durability is explicitly not claimed** (parent not fsync'd). Fine, but pair this with the atomic-visibility "must be verified for the deployment" caveat so a reader does not infer power-loss safety.
- **Abstract imbalance**: reports the 40 fidelity passes but omits the 40 failures; reports "all oracles matched" without the fixture-circularity qualifier. Rebalance both.
- **Notation load is very high.** Several equations restate ordinary logic (e.g. the stopping rule `E_{j+1}=E_j G_j` is "AND"; `deliverable(...)` is an `if Clean`). Consider demoting a few to prose to reduce the ~40-predicate cognitive load.
- **Two propositions, no numbered theorem environment.** For a doctoral/journal formal contribution, state them as numbered Proposition/Theorem with explicit assumption lists and short proofs, so the conditional nature (M3) is unmistakable.

## 6. Specific corrections (line-referenced, mechanical)

Five sentence-initial lowercase words (broken sentence case). All verified against source:

| File | Line | Current | Fix |
|---|---|---|---|
| `extended/sections/11-format-methods.tex` | 331 | "...structural evidence only. **the** authorized claim..." | capitalize **The** |
| `extended/sections/11-format-methods.tex` | 453 | "...in \cref{sec:evaluation}. **incomplete** runs..." | capitalize **Incomplete** |
| `extended/sections/16-evaluation.tex` | 132 | "...parser reports fixed. **end-to-end** comparisons..." | capitalize **End-to-end** |
| `extended/sections/16-evaluation.tex` | 162 | "...disable its prerequisite. **for** records without one..." | capitalize **For** (in Table `mechanism-ablation`) |
| `extended/sections/16-evaluation.tex` | 328 | "...version hypothesis. **its** paired discordances..." | capitalize **Its** |

(The build itself is clean: no undefined references or citations in `aura-file-defender-extended.log`.)

## 7. Independent verification log

I recomputed every cross-count in the results macros; **all reconcile exactly**:

- Strata `50 + 30 + 24 = 104`; accepted `50 + 30 = 80`; blocked `= 24`. ✔
- Fidelity pass `24 + 8 + 8 = 40`; fail `32 + 8 = 40`; pass+fail `= 80` (= accepted). ✔
- Second-pass closure `32 exact + 48 lossy = 80`. ✔
- Performance `312 cold + 1,560 warm = 1,872`; `cold = 104×3`, `warm = 104×5×3`. ✔
- Per-profile warm obs `{unsupported 360, raster 360, gif 120, audio 480, video 240}` sum `1,560`; implied records `{24, 24, 8, 32, 16}` sum `104`; accepted-path records `24+8+32+16 = 80`. ✔
- Sequential rate `1000 / 125.936 ms = 7.94 /s`. ✔
- Fuzz `7,299,439 / 210 s ≈ 34,760 exec/s`. ✔ (and 210 s = 0.28% of the prescribed 75,600 target-seconds — see M5).

No arithmetic error was found. The concerns above are about **scope, proof rigor, and framing**, not numerical inconsistency.

---

### Bottom line
Keep the honesty — it is the paper's best quality and most CDR papers lack it. But the manuscript currently presents (i) definitional formal results as theorems and (ii) a benign-only experiment as threat-model evidence. Address M1–M4 and the paper becomes a solid method-and-protocol contribution; add the missing strata and prove the monotonicity grounding and it becomes a strong one.

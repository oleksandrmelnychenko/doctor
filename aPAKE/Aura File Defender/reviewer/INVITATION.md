# Reviewer invitation

## Email subject

Independent offline review of a frozen public-media evidence packet

## Copy-paste invitation

Dear [Reviewer name],

I am seeking an independent technical review of a frozen public-media evidence
packet used in a study of policy-indexed canonical reconstruction and
fail-closed delivery of untrusted media.

The task is not to endorse the software or assess malware-detection efficacy.
It is to independently adjudicate source provenance, license, collection and
content lineage, dependence cluster, encoder family, and S0/S1 placement for
candidate public media. Provisional claims in the packet are leads rather than
accepted facts, and rejection is an expected valid outcome.

The packet contains 316 source byte strings with their provider evidence,
canonical audit records, and three retained inspection outputs per source. The
compressed download is approximately 1.53 GB. Decisions are authored as
canonical JSON and signed offline with an Ed25519 key that you generate and
retain outside the packet. You return only the public key, registry facts,
decision JSON files, and detached signatures. Your private key must never be
shared.

Scientific admission requires matching approvals from two reviewers in
different independence clusters. You must work without access to the other
reviewer's decisions. Please participate only if you were independent of the
candidate-discovery and audit-packet-generation work.

Frozen packet identity:

- producer commit:
  `8aa55ef684c2aed5c25811c3d3ec004b08e3f680`;
- archive size:
  `1,534,238,629` bytes;
- SHA-256:
  `35848d3851d67808070fcc643a32cee825944f2765e8aaf50091161b60fa72cd`.

If you agree, I will send an access-controlled download link separately. The
attached runbook provides the exact verification, decision-authoring, signing,
and return procedure.

Please reply with:

1. your organization or professional affiliation;
2. a short description of your relevant expertise;
3. confirmation that you were independent of candidate discovery and packet
   generation;
4. your proposed independence-cluster identifier;
5. the media profiles you are qualified to review;
6. whether you can complete the review without consulting the other reviewer.

Negative findings, exclusions, and disagreements will be retained unchanged.
Participation is an independent evidence review, not authorship approval or a
release recommendation.

Kind regards,

Oleksandr Melnychenko

Khmelnytskyi National University

# Independent Reviewer Kit

This directory is the author-side handoff wrapper for the independent
public-source review required by the Aura File Defender evidence protocol. It
does not replace the frozen review packet or any contract contained in that
packet.

## Frozen packet

Use only the following archive:

- server path:
  `/srv/aura-file-defender/public-source-review-handoff-8aa55ef-evidence.tar.zst`;
- packet-producing commit:
  `8aa55ef684c2aed5c25811c3d3ec004b08e3f680`;
- evidence commit:
  `8065a3582528b6061aacac1a7159dce04feebb2a`;
- size:
  `1,534,238,629` bytes;
- SHA-256:
  `35848d3851d67808070fcc643a32cee825944f2765e8aaf50091161b60fa72cd`.

Verified off-server copy:

- private GitHub prerelease:
  [evidence-public-source-review-handoff-20260725T231947Z-8aa55ef](https://github.com/oleksandrmelnychenko/ecliptix-file-defender/releases/tag/evidence-public-source-review-handoff-20260725T231947Z-8aa55ef);
- release ID: `360560459`;
- archive asset ID: `491668337`;
- upload attestation asset ID: `491670170`;
- upload attestation SHA-256:
  `e9df8a92dca4318c5c9fab0dfc80f8fe61371968e26bc330346d6a9c299fcd6a`.

The local, uploaded, and downloaded archive copies were all
`1,534,238,629` bytes and had the same full SHA-256. The downloaded
attestation was byte-identical to the uploaded attestation.

The 47,774,624-byte GitHub prerelease asset whose digest begins
`d7ba66114453` is a different ten-file compatibility-pilot archive. It is not
the independent-review packet and must not be substituted for it.

The repository and prerelease are private. A reviewer can use the release URL
only when granted appropriate read access. Otherwise, the author must download
the verified asset and redistribute that exact byte string through another
access-controlled channel. Send the download location privately and the
expected SHA-256 through a second channel.

## Independence requirement

At least two reviewers are required. They must:

- belong to different independence clusters;
- be independent of candidate discovery and audit-packet generation;
- keep separate Ed25519 private keys outside the packet and audit server;
- work without seeing the other reviewer's decisions;
- return a decision for each inspected source, including explicit rejections;
- independently adjudicate provisional provenance and licensing claims.

The author, the candidate-discovery operator, and the audit-packet generator do
not qualify as independent reviewers for this gate.

## What each reviewer receives

Send each reviewer:

1. the frozen `.tar.zst` packet;
2. its full SHA-256 through a separate channel;
3. [INVITATION.md](INVITATION.md);
4. [RUNBOOK.md](RUNBOOK.md).

Track invitations and returned bundles in
[REVIEWER-TRACKER.md](REVIEWER-TRACKER.md). Do not place private keys in the
tracker or repository.

The packet itself contains:

- 316 exact source byte strings;
- 316 canonical audit records and review inputs;
- 722 provider-evidence references;
- 948 retained inspection outputs;
- frozen JSON Schemas;
- `tools/author-public-source-review.py`;
- `SHA256SUMS` covering the packet.

## What each reviewer returns

Private keys must never be returned. Each reviewer returns one directory
containing:

- their Ed25519 public key in PEM form;
- canonical decision `.json` files;
- raw 64-byte detached `.sig` files;
- the registry facts listed in the runbook;
- a checksum inventory for the returned files.

Approvals are usable only when two independently signed decisions agree on the
source binding and reviewed claims. Rejections and disagreements remain
evidence and must not be discarded or rewritten.

## Author-side acceptance boundary

Receiving files is not admission. The server must subsequently:

1. validate both public keys and registry entries;
2. verify every detached signature and packet binding;
3. confirm two distinct independence clusters;
4. run fail-closed deterministic selection;
5. perform full-file input admission;
6. freeze the protocol-budget corpus manifest.

If any check fails, the affected source remains unadmitted and the scientific
gate remains false.

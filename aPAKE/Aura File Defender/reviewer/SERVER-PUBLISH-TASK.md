# Server task: publish the frozen reviewer packet off-server

Run this task on the audit server before inviting reviewers.

## Objective

Create a private GitHub prerelease containing the exact frozen independent
review packet. This is a distribution step only. It must not alter the packet,
create reviewer decisions, or change any scientific gate.

## Frozen inputs

- repository: `oleksandrmelnychenko/ecliptix-file-defender`;
- branch: `agent/server-validation-pilot`;
- target evidence commit:
  `8065a3582528b6061aacac1a7159dce04feebb2a`;
- archive:
  `/srv/aura-file-defender/public-source-review-handoff-8aa55ef-evidence.tar.zst`;
- expected size:
  `1,534,238,629` bytes;
- expected SHA-256:
  `35848d3851d67808070fcc643a32cee825944f2765e8aaf50091161b60fa72cd`;
- proposed tag:
  `evidence-public-source-review-handoff-20260725T231947Z-8aa55ef`.

## Required procedure

1. Confirm that the archive is a regular file, is not a symlink, has the exact
   byte size, and matches the full expected SHA-256.
2. Confirm that remote commit
   `8065a3582528b6061aacac1a7159dce04feebb2a` exists and contains the Git-safe
   rehearsal at
   `docs/research/rehearsals/20260725T231947Z-8aa55ef-public-source-review-handoff/`.
3. Confirm that the proposed release tag does not already exist. If it exists,
   stop and report it; do not overwrite or silently reuse it.
4. Create a private prerelease targeted exactly at evidence commit `8065a358`.
5. Upload:
   - the `.tar.zst` archive;
   - the retained `evidence-archive.SHA256`;
   - `handoff-summary.json`;
   - a new external attestation containing repository, target commit, archive
     filename, byte size, SHA-256, upload timestamp, and GitHub asset identity.
6. Download the archive back from GitHub into a newly created temporary
   directory.
7. Verify that the downloaded object has the same byte size and SHA-256.
8. Verify that the uploaded and downloaded attestation files are
   byte-identical.
9. Keep the original server archive unchanged. Safely remove only the
   explicitly created temporary download after successful verification.
10. Do not publish a public release, move the tag, add reviewer decisions, or
    set release eligibility.

## Prerelease notes

Use notes that state:

> Frozen offline public-source reviewer handoff produced by runner commit
> 8aa55ef684c2aed5c25811c3d3ec004b08e3f680 and retained at evidence commit
> 8065a3582528b6061aacac1a7159dce04feebb2a. The packet contains 316 review
> inputs and source byte strings, zero private keys, zero decisions, and zero
> signatures. It enables independent review but establishes neither corpus
> admission nor release eligibility.

## Required report

Return:

- prerelease URL and tag;
- target commit;
- GitHub asset names and asset IDs;
- upload and download byte sizes;
- local, uploaded, and downloaded SHA-256 values;
- attestation SHA-256 and byte-identity result;
- confirmation that the original archive was unchanged;
- confirmation that the release is private and marked prerelease;
- local and remote Git HEAD and worktree status;
- explicit statement that reviewer signatures and admitted sources remain
  `0`, `G_sci=false`, and `release_eligibility=false`.

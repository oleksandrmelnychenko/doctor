# Offline Reviewer Runbook

This procedure applies to
`public-source-review-handoff-8aa55ef-evidence.tar.zst` only.

## 1. Prepare an isolated workspace

Required tools:

- Python 3;
- `jsonschema==4.26.0`;
- OpenSSL with Ed25519 support;
- GNU `sha256sum`;
- a `tar` implementation with Zstandard support.

Install the Python dependency before disconnecting the review workstation:

```sh
python3 -m venv reviewer-venv
reviewer-venv/bin/python -m pip install 'jsonschema==4.26.0'
```

Create three separate locations. The private key and decisions must be outside
the extracted read-only packet:

```sh
umask 077
mkdir -p reviewer-work/packet reviewer-work/private reviewer-work/decisions
```

## 2. Verify and extract the packet

```sh
printf '%s  %s\n' \
  '35848d3851d67808070fcc643a32cee825944f2765e8aaf50091161b60fa72cd' \
  'public-source-review-handoff-8aa55ef-evidence.tar.zst' \
  | sha256sum --check -

tar --zstd -xf public-source-review-handoff-8aa55ef-evidence.tar.zst \
  -C reviewer-work/packet

cd reviewer-work/packet/public-source-review-handoff-8aa55ef
sha256sum --check SHA256SUMS
```

Stop and report the mismatch if either verification fails. Do not repair,
replace, or normalize packet files.

## 3. Generate a private reviewer key

Generate the key outside the packet:

```sh
openssl genpkey -algorithm ED25519 \
  -out ../../private/reviewer.private.pem

openssl pkey \
  -in ../../private/reviewer.private.pem \
  -pubout \
  -out ../../decisions/reviewer.public.pem

openssl pkey \
  -pubin \
  -in ../../decisions/reviewer.public.pem \
  -outform DER \
  | sha256sum
```

Record the resulting public-key SPKI SHA-256. Never upload, email, archive, or
return `reviewer.private.pem`.

## 4. Inspect one source

For every `review-inputs/<source-id>.json`:

1. inspect the exact source byte string identified by
   `source.packet_relative_path`;
2. inspect the bound audit record;
3. inspect all provider-evidence items;
4. inspect all three retained inspection outputs;
5. independently evaluate:
   - license name and HTTPS license URL;
   - source collection;
   - content lineage;
   - dependence cluster;
   - encoder family;
   - whether S0 or S1 is justified;
6. treat `provisional_claims` only as hypotheses;
7. approve only when at least two concrete evidence references support the
   reviewed claims.

Do not approve a source merely because it decodes, resembles the expected
format, or originated from a generally reputable provider.

## 5. Author an approval

Create a per-source claims file outside the packet:

```json
{
  "basis": "Concise independent justification tied to the listed evidence.",
  "content_lineage_id": "reviewed-lineage-id",
  "dependence_cluster_id": "reviewed-dependence-cluster",
  "encoder_family": "reviewed-encoder-family",
  "evidence_refs": [
    "exact packet-relative evidence path or stable evidence identifier",
    "second independent packet-relative evidence path or identifier"
  ],
  "license_name": "Reviewed license name",
  "license_url": "https://reviewed.example/license",
  "proposed_stratum": "S0",
  "source_collection_id": "reviewed-collection-id"
}
```

Use actual reviewed values. Do not copy placeholder values or provisional
claims without independent verification.

Run the frozen author tool from inside the packet while writing outside it:

```sh
../../../reviewer-venv/bin/python \
  tools/author-public-source-review.py \
  --review-input review-inputs/<source-id>.json \
  --reviewer-id <stable-reviewer-id> \
  --reviewed-at <YYYY-MM-DDTHH:MM:SSZ> \
  --decision approve \
  --reviewed-claims ../../private/<source-id>.claims.json \
  --private-key ../../private/reviewer.private.pem \
  --output-root ../../decisions
```

The tool revalidates the packet bindings, emits canonical JSON, creates a raw
64-byte Ed25519 signature, and verifies that signature before publication.

## 6. Author a rejection

Rejection is required when a material claim cannot be independently supported,
the evidence conflicts, or S0/S1 placement is not justified:

```sh
../../../reviewer-venv/bin/python \
  tools/author-public-source-review.py \
  --review-input review-inputs/<source-id>.json \
  --reviewer-id <stable-reviewer-id> \
  --reviewed-at <YYYY-MM-DDTHH:MM:SSZ> \
  --decision reject \
  --rejection-reason 'Specific evidence-based reason' \
  --private-key ../../private/reviewer.private.pem \
  --output-root ../../decisions
```

Repeat `--rejection-reason` for additional distinct reasons. Never convert an
uncertain case into an approval to satisfy a corpus quota.

## 7. Prepare registry facts

Return the following facts as a separate UTF-8 JSON document:

```json
{
  "authorized_profiles": ["profile-id"],
  "independence_basis": "Concrete explanation of organizational and operational independence.",
  "independence_cluster_id": "stable-cluster-id",
  "independent_from_audit_packet_generator": true,
  "independent_from_candidate_discovery": true,
  "organization": "Reviewer organization or professional affiliation",
  "public_key_filename": "reviewer.public.pem",
  "public_key_spki_sha256": "64-lowercase-hex-characters",
  "reviewer_id": "stable-reviewer-id"
}
```

The server will bind these facts into the frozen reviewer registry. Do not
claim independence that cannot be documented.

## 8. Verify and return the result

Before return:

```sh
python3 - <<'PY'
from pathlib import Path

signatures = sorted(Path("../../decisions").glob("*.sig"))
if not signatures:
    raise SystemExit("no detached signatures found")
invalid = [str(path) for path in signatures if path.stat().st_size != 64]
if invalid:
    raise SystemExit(f"non-64-byte signatures: {invalid}")
print(f"verified {len(signatures)} detached signature lengths")
PY

(
  cd ../../decisions
  sha256sum reviewer.public.pem *.json *.sig > RETURN-SHA256SUMS
)
```

Return only:

- `reviewer.public.pem`;
- `reviewer-registry-facts.json`;
- all decision `.json` files;
- all raw `.sig` files;
- `RETURN-SHA256SUMS`.

Do not return:

- the private key;
- per-source working notes containing sensitive personal data;
- modified packet files;
- another reviewer's decisions;
- unsigned spreadsheets or informal approval lists as substitutes for the
  canonical decision files.

Send the return bundle through an access-controlled channel and communicate its
top-level SHA-256 separately.

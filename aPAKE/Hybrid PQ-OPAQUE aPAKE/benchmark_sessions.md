# Benchmark sessions — run-to-run variance backing

Criterion measurements on the stated Linux/Xeon platform. The manuscript reports
the **point estimates and within-run 95% bootstrap intervals of Session 1** (the
first of three). Sessions 2 and 3 repeat the dominant (KSF-dominated and
KSF-free-overhead) workloads to bound run-to-run variability. The benchmark
targets that produce these numbers ship in the reproducibility artifact
(`aura-security-opaque-rs`, release `v2.1.0`, commit `1fa11c8`), so the variance
can be reproduced on other hardware with `cargo bench`.

Format per row: `[low  point-estimate  high]` (Criterion within-run bootstrap).

## Session 1 (canonical — values reported in the paper)

### bench_micro
```
ristretto255/keygen            [28.116  28.483  28.906] µs
ristretto255/single_dh         [56.291  56.690  57.122] µs
ristretto255/3dh               [174.83  178.09  182.80] µs
ristretto255/4dh               [223.09  224.23  225.49] µs
ml-kem-768/keygen              [99.964  100.72  101.62] µs
ml-kem-768/encapsulate         [98.824  103.25  108.04] µs
ml-kem-768/decapsulate         [117.14  118.13  119.23] µs
ml-kem-768/full_round          [332.25  336.09  340.43] µs
oprf/blind                     [78.621  79.338  80.141] µs
oprf/evaluate                  [64.612  65.072  65.587] µs
oprf/finalize                  [76.188  77.601  79.433] µs
hkdf/extract                   [2.2423  2.2616  2.2838] µs
hkdf/expand_64B                [2.0226  2.0368  2.0512] µs
hmac-sha512/256B               [2.7125  2.7337  2.7567] µs
xsalsa20-poly1305/encrypt_96B  [2.3144  2.3307  2.3491] µs
xsalsa20-poly1305/decrypt_96B  [2.5854  2.6271  2.6993] µs
argon2id/moderate_params       [780.86  787.03  793.34] ms
pq_combiner/combine            [2.3649  2.3898  2.4182] µs
```

### bench_protocol
```
registration/create_request    [113.81  114.49  115.23] µs
registration/create_response   [67.828  68.463  69.171] µs
registration/finalize          [777.98  783.75  790.14] ms
authentication/generate_ke1    [219.21  220.31  221.80] µs
authentication/generate_ke2    [547.57  557.13  568.88] µs
authentication/generate_ke3    [779.01  784.95  792.64] ms
authentication/responder_finish[2.6742  2.8994  3.2624] µs
full_protocol/authentication_e2e [797.65  806.13  816.30] ms
```

### bench_pq_overhead
```
pq_overhead/ke1/classic              [106.72  107.38  108.16] µs
pq_overhead/ke1/hybrid               [211.12  212.39  213.87] µs
pq_overhead/ke2_no_ksf/classic       [301.51  305.17  309.19] µs
pq_overhead/ke2_no_ksf/hybrid        [405.47  407.71  410.03] µs
pq_overhead/ke3_no_ksf/classic       [315.52  316.96  318.61] µs
pq_overhead/ke3_no_ksf/hybrid        [441.61  ~444    ~446 ] µs
pq_overhead/full_ake_no_ksf/classic  [762.71  768.10  774.45] µs
pq_overhead/full_ake_no_ksf/hybrid   [1104.5  1119.9  1139.7] µs
```
KSF-free post-quantum overhead (Session 1) = 1119.9 − 768.10 = **351.80 µs** (+45.8%).

## Sessions 2 and 3 (dominant workloads, for variance)

```
                                   Session 1     Session 2     Session 3
argon2id/moderate_params           787.03 ms     798.49 ms     842.42 ms
full_protocol/authentication_e2e   806.13 ms     810.26 ms     814.45 ms
pq_overhead/full_ake/classic       768.10 µs     824.43 µs     774.11 µs
pq_overhead/full_ake/hybrid       1119.90 µs    1124.50 µs    1123.20 µs
  -> KSF-free PQ overhead delta    351.80 µs     300.07 µs     349.09 µs
```

## Summary (variance reported in the paper)

| Workload | Range across 3 sessions |
|---|---|
| Argon2id (MODERATE) | 787 – 842 ms |
| End-to-end authentication | 806 – 814 ms |
| KSF-free hybrid full handshake | ~1.12 ms (stable) |
| KSF-free post-quantum overhead | 0.30 – 0.35 ms |

The KSF-free overhead is a difference of two sub-millisecond measurements, so its
session-to-session spread is wider in relative terms than the individual
workloads. Sub-millisecond figures should be read with a tolerance of order ten
percent.

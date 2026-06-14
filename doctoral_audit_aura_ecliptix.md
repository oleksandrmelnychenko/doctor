# Аудит AURA/Ecliptix для докторської роботи

Дата аудиту: 2026-06-14  
Область: `/Users/oleksandrmelnychenko/dev`  
Мета: визначити науковий каркас, готовність методів, шви між репозиторіями і структуру докторської роботи.

## 1. Executive Summary

Найсильніша докторська рамка тут не "месенджер" і не "AI moderation" окремо. Найсильніша рамка:

**Методи та інформаційна технологія постквантово-посиленої автентифікації, наскрізного захищеного обміну повідомленнями та приватної контекстної безпеки в месенджерах.**

Це дає цілісну систему з чотирма науковими методами:

1. **Hybrid PQ-OPAQUE** для створення й автентифікації акаунтів без передачі пароля серверу.
2. **Hybrid PQ E2EE messaging protocol** для 1:1 обміну з ратчет-рівневим KEM-підсиленням і metadata protection.
3. **Messenger-native contextual safety runtime** для локальної/приватної оцінки ризику з пам'яттю контакту, розмови, часу і продуктового рішення.
4. **Server-blind supervision relay** для передачі safety-сигналів між child/parent endpoint-ами без plaintext на сервері.

Розділ 7 найкраще робити як **інформаційну технологію**, яка інтегрує всі методи: iOS client, Rust platform, gateway, runtime, relay, OPAQUE, protected protocol, FFI, release artifacts.

Оцінка стану: ядро вже достатньо сильне для докторського каркаса. Головний ризик не в ідеї, а в синхронізації claims, доказів, тестів і меж застосування.

## 2. Карта репозиторіїв

| Репозиторій | Роль у докторській | Стан |
|---|---|---|
| `aura-security-opaque-rs` | Метод 1: Hybrid PQ-OPAQUE автентифікація | Найбільш paper-ready. Clean worktree. |
| `aura-protected-protocol-rs` | Метод 2: Hybrid PQ E2EE protocol | Сильний, але є documentation drift по ProVerif claims. |
| `ecliptix-aura` | Метод 3/4: AURA Core contextual safety runtime | Великий artifact, сильна release discipline, але треба не overclaim clinical validity. |
| `aura-platform` | Розділ 7: backend інформаційної технології, runtime integration, supervision relay | Clean worktree. Містить актуальні pair-key packages. |
| `ecliptix-auth-relay` | Evidence branch для supervision relay consent/data-plane | Clean. Може бути історичним/паралельним доказом, але canonical краще вибрати один. |
| `aura-messenger-ios` | Integration/proof-of-portability, mobile artifact | Сильний integration layer, але worktree dirty. |
| `ecliptix-file-defender` | Допоміжний метод для attachment/media defense | Можна використати як частину інформаційної технології або окремий minor method. |
| `aura-web` | Claims registry / public-facing story | Є stale claims, не використовувати як джерело наукових тверджень без оновлення. |

## 3. Головна наукова новизна

### 3.1 Системна новизна

Новизна не в тому, що кожен криптографічний компонент існує окремо. Новизна в інтеграції:

- password-based account establishment без передачі password-equivalent матеріалу серверу;
- post-quantum reinforced E2EE messaging;
- stateful safety runtime, який працює в messenger context, а не як generic classifier;
- server-blind supervision data plane, де сервер маршрутизує opaque blobs, але не отримує plaintext safety payload;
- reproducible artifact discipline: формальні моделі, Rust тести, FFI boundary, release reports, audit evidence, dataset governance.

Це можна формулювати як **end-to-end secure-and-safe messenger architecture**, де security і safety не конфліктують через server-side plaintext moderation.

### 3.2 Методична новизна

1. **Hybrid PQ-OPAQUE method**  
   Внесок: адаптація augmented PAKE до post-quantum transition model через hybrid DH/KEM session establishment, чітке operational scoping `oprf_seed`, артефактні докази і Rust реалізація.

2. **Hybrid PQ protected protocol**  
   Внесок: open two-party hybrid secure messaging construction з ratchet-level KEM binding, metadata-key rotation, MRAE payload protection, scoped formal evidence і executable validation.

3. **AURA contextual runtime**  
   Внесок: messenger-native safety engine з longitudinal context, latent state, sender/conversation memory, policy action surface, privacy-safe audit and release gating.

4. **Server-blind supervision relay**  
   Внесок: consent-gated parent-child safety relay, де initial pair key provisioned per parent device through existing E2E key package path, а server stores/routes only opaque payloads and sealed key packages.

## 4. Оцінка готовності по методах

| Метод | Готовність | Коментар |
|---|---:|---|
| Hybrid PQ-OPAQUE | 88/100 | Найстабільніший розділ. Є formal docs, tests, threat model, artifact guide, paper. |
| Hybrid PQ E2EE 1:1 | 82/100 | Сильний метод. Треба закрити drift: README каже ProVerif 3/6, formal README каже active 4/4 + group 6/6. |
| Group/Shield protocol | 68/100 | Можна включати, але claims мають бути scoped. Не називати full asynchronous MLS proof. |
| AURA Core runtime | 78/100 | Дуже сильний artifact. Потрібна наукова рамка evaluation validity, не clinical proof. |
| Server-blind supervision relay | 76/100 | Pair-key provisioning вже є у platform + iOS. Потрібен зафіксований end-to-end test/artifact. |
| Platform information technology | 80/100 | Добрий кандидат для Розділу 7. Потрібно вибрати canonical repo/status. |
| iOS artifact | 67/100 | Добрий integration proof, але dirty worktree і release blockers. |
| File defender | 65/100 | Допоміжний компонент. Для окремого методу потрібні benchmarks/eval/threat model. |

## 5. Критичні шви, які треба дотягнути

### 5.1 Protected Protocol documentation drift

Знайдено суперечність:

- `aura-protected-protocol-rs/README.md`: ProVerif `3/6 queries discharged`.
- `formal/README.md`: active ProVerif model `4/4 discharged`, group scoped model `6/6 discharged`.
- `docs/artifact-reproducibility.md`: ProVerif `3/6`.
- paper text still mostly follows `3/6 primary claims`.

Рішення: обрати чесну модель формулювання:

> ProVerif discharges 3 primary claims plus one additional scoped honest-message correspondence check; group model discharges 6 scoped group-epoch queries. Stress obligations remain non-claims.

Або оновити все на 4/4, але тільки якщо paper, artifact guide і logs справді підтримують це без overclaim.

### 5.2 AURA Core не є clinical validation

`ecliptix-aura` сильний як engineering safety runtime, але не як доказ психологічної/клінічної ефективності.

Докторська має писати:

- "contextual risk assessment";
- "messenger-native safety decision support";
- "release-gated evaluation on curated and synthetic messenger-like corpora";
- "privacy-safe auditability".

Не писати:

- "clinical diagnosis";
- "guaranteed child protection";
- "psychological truth inference".

### 5.3 Supervision relay: дизайн став сильним, але треба E2E доказ

У `aura-platform` вже є:

- `SUPERVISION_GET_RECIPIENT_DEVICES = 644`;
- `SUBMIT/LIST/ACK_PAIR_KEY_PACKAGES = 639..641`;
- pair-key package migration;
- consent gates;
- per-device routing;
- revoke/purge behavior.

В iOS вже є:

- `SupervisionRelayPairKeyProvisioningService`;
- wrap via `ChannelMessageCryptoService`;
- parent consume/unwrap/install/ACK;
- fail-closed no-device state;
- local key zeroization.

Потрібен release-grade proof:

- targeted XCTest або integration test: grant consent -> list recipient devices -> wrap pair key -> submit package -> parent consume -> ACK -> child sends sealed relay message -> parent opens -> revoke purges.
- one short artifact document with exact command and expected output.

### 5.4 Stale public claims in aura-web

`aura-web/src/lib/facts.ts` still says AURA Core is planned/not runnable, while `ecliptix-aura` is a large local artifact.

Also likely stale:

- fuzz target count for protected protocol;
- OPAQUE test count;
- ProVerif status.

For dissertation, do not quote `aura-web` until it is synchronized.

### 5.5 Canonical source selection

`aura-platform` and `ecliptix-auth-relay` overlap. For dissertation evidence, use one canonical backend repo.

Recommendation:

- canonical backend: `aura-platform`;
- mention `ecliptix-auth-relay` only as historical branch/evidence if needed;
- avoid split claims across both.

### 5.6 Dirty worktrees

Current dirty state:

- `aura-messenger-ios`: many modified/untracked UI and transcript files.
- `ecliptix-aura`: staged/modified `.gitignore` and `Cargo.lock`.
- `aura-protected-protocol-rs`: Xcode scheme metadata modified.

Before dissertation artifact freeze: every method must have a clean commit hash, tag, release note, and verification command.

## 6. Recommended Dissertation Structure

> **⚠️ ЗАСТАРІЛО (станом на 2026-06-14).** Структуру нижче (крипто-центричну:
> OPAQUE = розділ 3, E2EE = розділ 4) **замінено** на runtime-центричну
> 8-розділову структуру в `Записка/` (git: «Center dissertation on AURA runtime»).
> Актуальна структура: 1) Аналіз; 2) Концепція AURA Runtime + модель загроз;
> 3) Контекстна оцінка ризику; 4) policy-aware рішення; 5) PQ-OPAQUE;
> 6) гібридний PQ E2EE; 7) серверно-сліпий канал нагляду; 8) інформаційна технологія.
> Розділи 3–9 цього аудиту (**claim boundaries, готовність методів, шви,
> ProVerif drift, evidence**) залишаються чинними й використовуються як джерело
> меж тверджень.

### Розділ 1. Аналіз стану проблеми

Scope:

- secure account creation and password-authenticated protocols;
- OPAQUE and augmented PAKE;
- PQ migration in authentication and messaging;
- Signal/X3DH/Double Ratchet/PQXDH/PQ3/MLS;
- E2EE moderation dilemma;
- child/teen safety and privacy-preserving safety systems;
- server-side moderation vs client-side/contextual safety;
- artifact reproducibility and formal verification for security systems.

Goal of the chapter: show the gap:

> Existing secure messengers treat authentication, post-quantum E2EE, and trust/safety as separate layers. Server-side safety weakens privacy, while purely local safety lacks accountable relay and review workflows. A unified architecture is needed.

### Розділ 2. Загальна ідея та архітектура

Present the whole AURA/Ecliptix concept:

- account establishment layer: Hybrid PQ-OPAQUE;
- protected messaging layer: hybrid PQ E2EE protocol;
- contextual safety layer: AURA Core;
- supervision relay layer: server-blind consented parent-child safety channel;
- implementation layer: Rust services + iOS + FFI + reproducibility.

This chapter must define shared threat model and claim boundaries:

- classical vs quantum adversary;
- server-compromise vs endpoint-compromise;
- E2EE plaintext boundary;
- AURA safety evaluation boundary;
- metadata leakage boundary;
- operational key management boundary.

### Розділ 3. Метод постквантово-посиленої OPAQUE-автентифікації

Use `aura-security-opaque-rs`.

Core claims:

- password never sent to server;
- DB compromise does not give immediate offline dictionary under classical model without `oprf_seed`;
- PQ hybrid protects session establishment against future DH break within scope;
- Argon2id remains password-hardening layer;
- formal and executable validation map.

Must include:

- OPRF seed operational model;
- quantum exposure limitation;
- message sizes and latency;
- formal proof scope;
- Rust implementation mapping.

### Розділ 4. Метод гібридного постквантового захищеного обміну повідомленнями

Use `aura-protected-protocol-rs`.

Core claims:

- X25519 + ML-KEM-768 hybrid root;
- Ed25519 classical authentication, explicitly not PQ signatures;
- Double Ratchet with KEM-enhanced step;
- metadata AEAD/key rotation;
- replay/rollback/skipped-key limits;
- scoped Tamarin/ProVerif evidence.

Must fix before final:

- synchronize ProVerif claims;
- decide whether group protocol is subsection or separate chapter;
- keep group claims scoped.

### Розділ 5. Метод приватної контекстної безпеки в месенджері

Use `ecliptix-aura`.

Core claims:

- context-aware safety decisions, not isolated message classification;
- contact/conversation/timing memory;
- kids/military/domain modules;
- policy action surface;
- privacy-safe audit records;
- release-gated evaluation with curated and synthetic corpora.

Must include:

- dataset governance;
- release criteria;
- privacy audit policy;
- limitation: not clinical validation.

### Розділ 6. Метод server-blind supervision relay

Use `aura-platform` + `aura-messenger-ios`.

Core claims:

- child-controlled consent;
- active parent-child binding;
- server stores opaque payloads only;
- initial pair key is generated client-side and sealed per parent device;
- server routes sealed key packages and cannot read pair key;
- ACK only after parent install;
- revoke/purge crypto-shreds state.

Must include:

- protocol flow diagram;
- authorization model;
- pair-key package lifecycle;
- replay/TTL/DoS limits;
- privacy boundary.

### Розділ 7. Інформаційна технологія захищеного месенджера AURA/Ecliptix

This should integrate:

- Rust backend services;
- iOS client;
- OPAQUE FFI;
- protected protocol FFI;
- AURA runtime;
- supervision relay;
- search privacy boundary;
- deployment/reproducibility scripts;
- artifact manifest.

This chapter proves engineering feasibility and integration, not a new cryptographic theorem.

## 7. Recommended Title Options

### Strong Ukrainian title

**Методи та інформаційна технологія постквантово-посиленої автентифікації, захищеного обміну повідомленнями та приватної контекстної безпеки в месенджерах**

### More compact

**Методи постквантово-посиленої автентифікації та приватної контекстної безпеки для захищених месенджерів**

### More security-heavy

**Методи побудови захищеного месенджера з постквантово-посиленою автентифікацією, наскрізним шифруванням і server-blind safety relay**

Recommendation: use the first as working dissertation title. It is broad enough to cover all chapters and precise enough to avoid sounding like a product description.

## 8. What To Fix Before Writing The Dissertation Text

Priority order:

1. Freeze canonical repo map and commit hashes.
2. Fix `aura-protected-protocol-rs` ProVerif claim drift.
3. Add/record E2E supervision relay provisioning test.
4. Clean/tag `aura-messenger-ios` or define it as non-frozen integration prototype.
5. Clean/tag `ecliptix-aura` release artifact with `Cargo.lock` decision.
6. Synchronize `aura-web` facts or ignore it for dissertation evidence.
7. Prepare one artifact index:
   - repo;
   - commit;
   - method/chapter;
   - verification command;
   - expected result;
   - limitations.
8. Write one cross-system threat model covering all methods.
9. Write one claim-boundary table for the dissertation.

## 9. Reviewer-Style Verdict

Current dissertation potential: **high**.

Estimated readiness as a doctoral program:

- scientific idea: **86/100**;
- implementation artifacts: **82/100**;
- proof/evaluation discipline: **76/100**;
- dissertation readiness today: **72/100**;
- after fixing claim drift and adding E2E supervision artifact: **82-86/100**.

The work can be positioned as a serious doctoral system if the novelty is framed as a unified secure messenger architecture with multiple validated methods. It should not be framed as "we built a messenger" or "we added AI moderation". The defensible scientific core is the combination of post-quantum authentication, hybrid E2EE, privacy-preserving contextual safety, and server-blind supervision under explicit claim boundaries.

## 10. Immediate Next Step

Start the dissertation with two tables:

1. **Problem-to-method map**
   - password exposure -> Hybrid PQ-OPAQUE;
   - future quantum decryption -> Hybrid PQ E2EE;
   - E2EE safety dilemma -> AURA contextual runtime;
   - guardian review without server plaintext -> server-blind supervision relay.

2. **Claim-boundary map**
   - what is proven formally;
   - what is tested;
   - what is evaluated statistically;
   - what is an implementation artifact;
   - what is explicitly not claimed.

These two tables will make the doctoral story coherent from the first chapter.

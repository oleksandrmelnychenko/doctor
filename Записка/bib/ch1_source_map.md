# Карта джерел Розділу 1 (SOTA) — веб-верифікована база

> Згенеровано research-workflow + adversarial-верифікацією (2026-06-14). **59 кандидатів, усі резолвляться.**
> Це робоча база для курування. Після узгодження → переносимо у `references.bib` (ДСТУ) і пишемо прозу.
> Психологічні поняття всюди — **операціоналізовані сигнали, не клінічні діагнози**.

---

## 1.1 Приватна цифрова комунікація та модель E2EE
**Теза:** E2EE (X3DH+Double Ratchet → MLS → PQXDH/PQ3) надійно захищає **вміст**, але модель захисту зупиняється на межі шифротексту — **метадані й endpoint/контекст** лишаються поза нею.
- `marlinspike2016x3dh` — X3DH Key Agreement Protocol (Signal spec, 2016) — первинна специфікація асинхронного узгодження ключів.
- `perrin2016doubleratchet` — Double Ratchet Algorithm (Signal spec, 2016) — per-message FS + post-compromise security.
- `cohngordon2020signal` — Cohn-Gordon et al., *J. Cryptology* 33(4):1914-1983, 2020 (EuroS&P 2017) — рецензований формальний доказ X3DH+Double Ratchet.
- `rfc9420` — MLS Protocol, RFC 9420, IETF 2023 — стандартизація E2EE на групи (TreeKEM).
- `kret2023pqxdh` — PQXDH (Signal spec, 2023) — перший розгорнутий PQ-крок (X25519+ML-KEM).
- `linker2025pq3` — Linker, Sasse, Basin, USENIX Sec 2025 (ePrint 2024/1395) — Tamarin-аналіз Apple PQ3.
- `martiny2021sealedsender` — Martiny et al., NDSS 2021 — межі Sealed Sender (метадані витікають).

## 1.2 Ризикові інформаційні впливи в приватних каналах
**Теза:** шкідливі впливи (grooming, coercion, bullying, scams, дезінформація, self-harm) концентруються саме в приватних каналах; вони **операціоналізовні як сигнали**, а вразливі групи (діти/підлітки) — найбільш експоновані.
- `smahel2020eukids` — EU Kids Online 2020 (19 країн, 25 101 дитина) — масштаб/вразливість.
- `borj2023grooming` — Borj, Raja, Bours, *Knowledge-Based Systems* 259:110039, 2023 — огляд детекції grooming у чатах.
- `vogels2022cyberbullying` — Pew Research 2022 (n=1316) — 46% підлітків зазнали кібербулінгу. *(індустріальне опитування — маркувати)*
- `vosoughi2018falsenews` — Vosoughi, Roy, Aral, *Science* 359(6380):1146-1151, 2018 — дифузія фейків. *(дані з публічного Twitter — обережно з перенесенням на приватні канали)*
- `norris2019fraud` — Norris, Brookes, Dowell, *J. Police Crim. Psych.* 34(3), 2019 — психологія шахрайства.
- `susi2023selfharm` — Susi et al., *J. Child Psychol. Psychiatry* 64(8), 2023 — self-harm контент (і шкода, і захисний ефект).
- `kamara2022e2ee` — Kamara et al., arXiv:2202.04617 (CDT) — toolbox модерації за E2EE. *(think-tank report)*

## 1.3 Дилема модерації за E2EE
**Теза:** серверне сканування контенту структурно несумісне з E2EE; приватнозберігаючі альтернативи (franking, AMF, private membership) можливі, але точкові, класичні й не контекстні.
- `abelson2024bugs` — Abelson et al. (14 авторів), *J. Cybersecurity* 10(1):tyad020, 2024 — критика client-side scanning.
- `ec2022csar` — European Commission COM(2022) 209 (CSAR/«Chat Control») — первинний регуляторний драйвер.
- `schmon2025chatcontrol` — EFF Deeplinks, груд. 2025 — статус законодавчого процесу. *(адвокаційна аналітика — лише для статусу)*
- `grubbs2017franking` — Grubbs, Lu, Ristenpart, CRYPTO 2017, LNCS 10403:66-97 — committing AEAD / message franking.
- `tyagi2019amf` — Tyagi et al., CRYPTO 2019, LNCS 11694:222-250 — asymmetric message franking.
- `kulshrestha2021harmful` — Kulshrestha, Mayer, USENIX Sec 2021:893-910 — private membership (межовий випадок CSS).
- `scheffler2023sok` — Scheffler, Mayer, *PoPETs* 2023(2):403-429 — SoK простору модерації за E2EE.

## 1.4 Недостатність позаконтекстної класифікації
**Теза:** покомпонентна (single-message) класифікація токсичності контекстно-сліпа, упереджена (false positives на identity/reclaimed лексиці), крихка до атак; «додати контекст» наївно не працює — треба stateful моделювання.
- `perspectiveLees2022` — Lees et al., KDD 2022:3197-3207 — Perspective API як де-факто baseline.
- `hosseini2017` — Hosseini et al., arXiv:1702.08138 — змагальна крихкість Perspective.
- `macavaney2019` — MacAvaney et al., *PLOS ONE* 14(8):e0221152, 2019 — межі детекції hate speech.
- `garg2023` — Garg et al., *ACM Comput. Surv.* 55(13s):264, 2023 — упередженість/fairness.
- `pavlopoulos2020` — Pavlopoulos et al., ACL 2020:4296-4305 — «чи важить контекст?» (наївне додавання не покращує).
- `xenos2022` — Xenos et al., *First Monday* 27(5), 2022 — оцінювання контекстної чутливості.

## 1.5 Парольна автентифікація та augmented PAKE
**Теза:** є чітка межа безпеки (offline-словник / pre-computation; звичайний vs **strong** aPAKE) і стандарти (OPAQUE/OPRF/SPAKE2+), але всі — **класичні** й автентифікаційно-центричні.
- `bellovin1992eke` — Bellovin, Merritt, IEEE S&P 1992:72-84 — EKE, витоки PAKE.
- `wu1998srp` — Wu, NDSS 1998:97-111 — SRP (verifier-based, але salt у відкритому).
- `rfc9383spake2plus` — Taubert, Wood, RFC 9383, 2023 — SPAKE2+. ⚠️ **Independent Submission, НЕ CFRG** (виправлено верифікацією; те саме для RFC 9382).
- `jarecki2018opaque` — Jarecki, Krawczyk, Xu, EUROCRYPT 2018, LNCS 10822:456-486 — **strong aPAKE** у UC (ePrint 2018/163).
- `rfc9807opaque` — Bourdrez et al., RFC 9807, 2025 — стандартизація OPAQUE. ⚠️ **IRTF/CFRG Informational, НЕ «IETF standard»**.
- `rfc9497oprf` — Davidson et al., RFC 9497, 2023 — OPRF/VOPRF/POPRF (ядро стійкості до pre-computation).
- `lyu2024kemaepake` — Lyu, Liu, Han, ASIACRYPT 2024 — aPAKE-компілятор з KEM+AE (PQ-напрям, ще не стандарт). *(звірити сторінки за LNCS-томом)*

## 1.6 Постквантовий перехід
**Теза:** примітиви й патерни PQ-переходу стандартизовані/частково розгорнуті (KEM, гібрид, PQ-месенджери), але **PQ-автентифікація учасників** ще дослідницька й неінтегрована на рівні рантайму.
- `mosca2018` — Mosca, *IEEE S&P* 16(5):38-41, 2018 — store-now-decrypt-later, нерівність Моски.
- `fips203` — NIST FIPS 203 (ML-KEM), 2024 — стандарт KEM.
- `fips204` — NIST FIPS 204 (ML-DSA), 2024 — стандарт підпису.
- `bos2018kyber` — Bos et al., EuroS&P 2018:353-367 — CRYSTALS-Kyber.
- `rfc9794` — Driscoll, Parsons, Hale, RFC 9794, 2025 — термінологія PQ/T-гібридів.
- `kret2023pqxdh` — *(reuse 1.1)* — розгорнутий гібрид у месенджері.
- `lyu2024ucpake` — Lyu, Liu, Han, EUROCRYPT 2024, LNCS 14657:120-150 — UC-стійкий ґратковий PAKE (ePrint 2024/374).
- *(згадати окремо як Internet-Draft, не RFC: TLS hybrid `draft-ietf-tls-hybrid-design`, codepoint X25519MLKEM768)*

## 1.7 Системи нагляду/батьківського контролю та приватність
**Теза:** домінантна парадигма нагляду обмінює приватність/E2EE на захист (серверна видимість, без згоди), ще й неефективна та руйнує довіру — звідси потреба **server-blind, consent-gated** нагляду.
- `feal2020angel` — Feal et al., *PoPETs* 2020(2):314-335 — аудит 46 застосунків (72% діляться даними з 3-ми сторонами).
- `ali2020betrayed` — Ali et al., ACSAC 2020:69-83 — TLS-перехоплення, «опікун» як поверхня атаки.
- `ghosh2018safety` — Ghosh et al., CHI 2018, Paper 124 — 736 дитячих відгуків (76% — 1 зірка).
- `wisniewski2017parental` — Wisniewski et al., CSCW 2017:51-69 — моніторинг/обмеження vs самоконтроль.
- `badillourquiola2020beyond` — Badillo-Urquiola et al., *J. Adolescent Research* 35(1), 2020 — value-sensitive design.
- `park2024stillcomplicated` — Park et al., *IEEE S&P* 22(5):52-62, 2024 — зсув до teen-centric/resilience.

## 1.8 Відтворюваність і формальна верифікація
**Теза:** наукова довіра тримається на двох опорах — машинно-перевірена символьна верифікація + відтворювані артефакти — з обов'язковим окресленням межі «модель-реальність».
- `meier2013tamarin` — Meier et al., CAV 2013, LNCS 8044:696-701 — Tamarin.
- `blanchet2016proverif` — Blanchet, *FnT Privacy & Security* 1(1-2), 2016 — ProVerif.
- `blanchet2012symbcomp` — Blanchet, POST 2012, LNCS 7215:3-29 — символьна vs обчислювальна модель (що доводиться, а що ні).
- `cremers2017tls13` — Cremers et al., CCS 2017:1773-1788 — Tamarin-аналіз TLS 1.3 (знайдено аномалію).
- `cohngordon2017signal` — Cohn-Gordon et al., EuroS&P 2017:451-466 — формальний аналіз Signal *(=conf-версія cohngordon2020signal)*.
- `olszewski2025repro` — Olszewski et al., ACM REP 2025:96-107 — 11-річний огляд artifact-evaluation.

## 1.9 Наукова прогалина та постановка задачі *(синтез 1.1–1.8, нових джерел майже немає)*
**Теза:** немає **цілісного приватного рантайму**, що поєднує автентифікацію + PQ-E2EE + контекстну safety так, щоб бути водночас **server-blind** (зберігає приватність) і **accountable** (верифіковні сигнали). Три найсильніші framing-джерела:
- `scheffler2023sok` *(reuse 1.3)* — НАЙСИЛЬНІШЕ: safety як окремий шар у напрузі з E2EE.
- `kamara2021outside` — CDT report, 2021 (arXiv:2202.04617) — server-side найгірше для приватності, user-reporting/metadata — життєздатний шлях. *(=kamara2022e2ee)*
- `abelson2024bugs` *(reuse 1.3)* — серверно-якірна safety структурно ламає приватність.
- `grubbs2017franking` *(reuse 1.3)* — «accountable relay» без серверного plaintext.
- `kret2023pqxdh` *(reuse)* — PQ розв'язано лише на транспортному шарі.
- `rfc9807opaque` *(reuse 1.5)* — автентифікація як ізольований шар.

---

## ⚠️ Claim-застороги для прози (знайдено верифікацією)
1. **RFC 9383 / 9382** — Independent Submission, **не CFRG/IETF**. **RFC 9807 (OPAQUE)** — IRTF/CFRG **Informational**, не «IETF standard».
2. **TLS hybrid** — `draft-ietf-tls-hybrid-design` — **Internet-Draft, не RFC**.
3. Маркувати як **індустріальні/адвокаційні** (не рецензовані): Pew (1.2), EFF (1.3), CDT/Kamara, Apple PQ3 blog, Signal specs (первинні інженерні, але не рецензовані — кожну підкріплено рецензованим аналізом).
4. `vosoughi2018falsenews` — дані з **публічного** Twitter; не екстраполювати прямо на приватні канали.
5. `kulshrestha2021harmful` — технічно приватний, але архітектурно **різновид CSS** → подавати як межовий випадок.
6. Self-harm / fraud сигнали — **операціоналізовані для routing-to-support**, явно зазначати ризики false-positive/stigma/chilling-effect.
7. Сторінкові діапазони LNCS (Lyu ASIACRYPT/EUROCRYPT, AMF) — **звірити за фінальним томом** перед версткою.

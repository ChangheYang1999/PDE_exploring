# Numerical audit cutoff

Frozen 2026-11-04T16:44:17.242097+00:00 through AN964. This is the numerical cutoff note; any subsequent publication review is a dated supplement.

The fixed-parameter stationary IPM existence theorem is **OPEN**. The numerical certificates below have passed the independent checks identified in the current [Part VII numerical report](PART_VII_NUMERICAL_AUDIT_v03.md) and [reading guide](AUDIT_READING_GUIDE_v09.md), with their full hypotheses. They do not supply the six missing Sobolev obligations H-RC, H1, H2, H-BALL, H4-REST and H-N1. The stronger conclusion additionally needs H-REG, and the cited far analytic premises remain in force.

The parameter remains c=4076476460239181/2251799813685248, with q=21/10. The authoritative Candidate007 SHA256 remains ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21. Corrected center013 is unchanged. Its raw correction hash is a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a, canonical correction hash 2531d462643034e1083b40f5e60a6c4b0fa3ba84425cea3cadb68c767847fc33, and complete field hash 3d5f08e06859af2577f6e099374a8ce5e139a0b66280055ada847745943bf8cb.

| Certified numerical input at center013 | Enclosure or bound |
| --- | --- |
| L2 residual | [7.959400186993612e-7,7.961206656880281e-7] |
| Registered P-S1 norm | [0.0035510975483434412497,0.0055545729030073655758] |
| Whole-plane matrix lower | 704955805507/10^12 |
| Whole-plane correction-gradient upper | 1/4 |
| Whole-plane strain upper | 137/125 |

P-S1 is ||J^(21/10)(sqrt(1+4|X|^2) F_*)||_2 on R^2, with J=(1-Delta)^(1/2), using the registered Fourier convention. It is not the separate strong Holder norm S_F. Corrected-center S_F probes, FFT moments and grid agreement remain diagnostics. The complete near derivative inputs are certified, but the resulting closure arithmetic remains conditional.

| Current tuple | Near loss upper | Remaining rate for other H4 terms | Remaining price allowance |
| --- | --- | --- | --- |
| Plan: b0=11/20, mu=72 | 0.152627111489 | 0.002328694018 | 9941475955 |
| Fallback: b0=103/200, mu=68 | 0.180101237602 | 0.009854567905 | 47277952671/5 |

These are budgets, not proofs that the missing terms fit. The fallback kernels are not audited at their new parameters. The matrix loss below0.152070 cannot replace the nonlinear losses bounded above by0.3651689966 and0.3412910741. The CE graph witness must remain strict, and the source, inverse, domain, decay, compactness and localization hypotheses cannot be dropped.

The final numerical report is Part VII version3, SHA256 23b54d0626fb998d50b491ef0cba4213d217b999594233ba27a999024cfa7dcc. The current reading guide is version9, SHA256 2b45f7663d630464ada1c8c2a7deec850d0bc57470d5244b34782356c5640f2e, independently confirmed by AT2961 and AT2962 and adopted at [AN960](../exchange/audit_v960.md). The theory-auditor handoff is version3, adopted at AN957. The coordinator16:24 drafts and static retained-bundle update are confirmed by [AN959](../exchange/audit_v959.md) and by AT2964 to AT2966, whose actual review and completed guard are adopted at [AN961](../exchange/audit_v961.md). The fourteen pinned publication inputs also agree at the dated preflight. These checks leave the six Sobolev obligations and H-REG open.

The final retained-owner observation completed at 2026-11-04T16:43:06.881285+00:00 with 5355 checks in 1.7728945477865636 measured seconds. All five retained owner files have unchanged full content hashes and metadata. All 5294 local symbolic links are relative. The same 14 missing targets remain: 12 historical Source009 aliases and two deliberate negative fixtures. No recovery is claimed; the historical deletion remains procedurally refuted and byte recovery OPEN. See the [dated retention check](../storage/final_retention_v01/verification/check_v03.json), SHA256 beb250de364a0646f9a93c140737bf9d5fbac1cae2df524005d5c7e87f9039fd. Future retention and the relative owner layout remain obligations; this past observation is not a promise about future bytes.

The actual final ledger14 was installed at16:38:17Z, with identical shared and immutable history bytes, SHA256 6413c8897966b392fa72b5288a18ab9dcf7b83cee3bdcf0b27c389dcd57fe461. [AN962](../exchange/audit_v962.md) independently confirms its seven publication and citation changes, complete unchanged mathematical sections and exact budgets. [AN964](../exchange/audit_v964.md) adopts the distinct AT2968 to AT2970 review of the same ledger and actual X13 note; AT2971 leaves existence OPEN. These reviews do not certify the later final report or bundle. The report owner may publish them before18:05:30Z; any such installation needs its own actual observation. This agent stops by17:05:30Z.

The chronological [late verdict excerpt](AUDIT_LEDGER_AN950_AN964.md) records each additional claim, method, result and verdict. Existing immutable reports and failed attempts remain retained. No new field computation is needed or claimed in this cutoff note.

# Exact input archive addendum to economy gate review 001

Written UTC: 2026-10-31T22:18:36.468467+00:00.

The sealed review, original aggregation receipt and original aggregation script remain unchanged. This addendum resolves later changes to the live input files. The recovery manifest records the original byte recovery, and the archive receipt maps each recovered input to a gzip file. The transient uncompressed copies were removed only after successful decompression and exact hash and length checks.

Of the 60 original input files, 59 were recovered exactly: 41,153,219 uncompressed bytes retained as 1,195,179 gzip bytes. All original result JSONL inputs, exact candidate specification files, aggregation code, source notes and supporting policy and engine source inputs are included. The appended `afs6/results.jsonl` was recovered as the original-length prefix, whose SHA256 equals the original review input hash. Neither a current whole-file hash nor an approximate prefix was substituted.

The old full `bot_research/reports/REPORT.md` bytes could not be recovered. Its original recorded size is 184,332 bytes and SHA256 is `99228b17e4dcae1bed283c16ec0ba72dda57951bb4b1b13bf003ba306099cd50`. This input supplied surrounding prose, not numeric aggregation data. The challenged opponent-selection sentence remains quoted in the sealed review. The archive receipt also identifies a separately dated current report snapshot; it is not represented as the old report.

The independent archive recheck decompressed and verified all 59 input hashes, then reconstructed every selected row's candidate and opponent specifications, scenario, seat, WDL, HP difference and round count from the archived original result rows. It verified 3,384 row payload references, including repeated pool memberships, and recomputed all five numerical views: 846 weighted, 804 distinct, 448 additional weighted, 416 additional distinct and 406 disjoint additional conditions. Every count, WDL total and better/worse comparison agrees exactly with the sealed receipt. This count of 3,384 is the four roles times 846 selected memberships; it is different from the sealed receipt's separate source-metadata row count, which includes candidate duplicate records instead of repeated pool memberships.

The gzip archive preserves all bytes required for numeric reconstruction. The complete old report prose is the one explicit unavailable input. No games, policies, engine imports, policy constructors, replay calls or tests were run in this addendum.

Evidence:

- Original recovery manifest: `economy-gate-846-review-001.inputs.json`, SHA256 `08ccc530c0065a04c1cff8eeb25869ec6a6a19dca3c67d39845bea0abfdea85d`.
- Gzip mapping and independent reconstruction receipt: `economy-gate-846-review-001.archive-recheck.json`, SHA256 `5d642288f04f21921718e11b98c0c90f7027cee3bdba4aa5fb83f0915eee24ef`.
- Archive/reconstruction script: `economy_gate_846_archive_recheck_001.py`, SHA256 `18bb2b072852f8b33ab3d1b44f9da2ab9b6e0ae1809a8e7954b21d4a32f3979d`.
- Original aggregation receipt: `economy-gate-846-review-001.json`, SHA256 `d243192a3d235f2c38d4a9707c9ddfd0287fbfd9006dedd616b5daed37d95af7`.

Verdict: CONFIRMED for exact recovery of every numeric input and reproduction of the five tables. OPEN for recovery of the complete old report prose; no full-game replay or broader statistical independence claim follows.

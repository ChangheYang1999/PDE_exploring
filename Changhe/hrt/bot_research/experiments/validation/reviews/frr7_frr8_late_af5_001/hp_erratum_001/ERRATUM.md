# frr8 terminal HP erratum

Prepared 2026-10-31T23:52:43.191940+00:00. Reviewer: GPT-6 Astra. This addendum corrects the original sealed review without replacing its bytes.

**Claim.** [The original review](../REVIEW.md), line 27, says that AF5 beats v48 795:740 in both standard-start frr8 games. **Verdict: REFUTED.** The exact result rows and terminal raw records instead give **AF5 790:735, +55 at round 50 in both physical seats**. My earlier handoff repeated the same error. Both absolute HP values in that prose were too large by 5.

**Method.** Read both frr8 result rows and terminal records from their previously sealed gzip archives, authenticate their original and compressed hashes, and compare them byte for byte with the current original files. The [new evidence](EVIDENCE.json) retains full row identities, terminal snapshot fields and results, and the exact archive edges. The original result rows and `record_audit_final_001.json` already contained 790:735. This was a prose transcription error, not a change in the underlying game evidence.

**Claim.** The g1/frr5 canonical-history comparison remains valid. **Method.** Join the exact opponent specification, standard scenario and physical g1/AF5 seat, taking account of frr5 recording v48 as its candidate. Compare all 102 records in each complete history after removing only match identity metadata and snapshot policy names. All other fields and ordered actions remain. **Result.** Both comparisons are exactly equal, with g1 also finishing 790:735. **Verdict: CONFIRMED for these four retained histories.** This makes no fresh-policy or clock-invariance claim.

The literal-copy search covered original readable review files and gzip-decoded retained inputs. Among original sealed outputs, only `REVIEW.md` contains the wrong pair. The parent's later `root_review_001.py` assertion and its failure transcript also contain that pair as detection evidence; those files are separately identified and preserved. The original review, seal, and every original sealed output remain byte-identical.

The frr8 total of 2W0D0L, +55 margins, round counts, retained-action totals, and finite WDL matrix remain unchanged. The original seal authenticated bytes and numerical artifacts but did not detect this prose defect. Its existence must not be read as certification of the incorrect sentence. The corrected statement and this evidence take precedence for terminal HP reporting. No original sealed file was edited.

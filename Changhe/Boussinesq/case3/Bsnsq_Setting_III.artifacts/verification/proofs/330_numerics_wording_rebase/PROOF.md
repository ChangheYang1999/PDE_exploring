Revised 2026-10-22T09:29:57.527525+00:00, before revised controls. Initial proof retained in verification/proof_before_review.md.

# Preservation criterion for the numerical report wording repairs

## Exact statement and dependencies
This packet prepares a coupled six-file adoption proposal: NUM_REPORT.md, artifacts/consolidated_residuals.md, artifacts/README.md, the code/ and artifacts/ copies of consolidate_audits.py, and artifacts/code_sha256.txt. The unchanged CSV is supplied for comparison only. P313 audited 123 keyed audit entries, 121 forced entries and two manufactured controls, covering 119 distinct coefficient archive hashes. Their evaluation sets have 145, 161, 166, 177 or 189 radii and field-dependent 13630 to 18144 points. P316 independently reconstructed all 5904 CSV rows using the artifact and runs input roots. Those completed data audits are dependencies, not repeated PDE evaluations here.

## Argument
A specified string replacement preserves every other byte if its old string has the recorded occurrence count and its target is exactly the original with those occurrences replaced. Comparing the resulting whole files and exact diffs checks that preservation claim. Replaying the same algorithm checks determinism only; it is not an independent proof of the correctness of the chosen wording. The factual justification instead comes from P313, P316 and inspection of the complete changed passages.

Apply the P313 count and grid repairs to the current frozen report, retaining later unrelated header and chronological-heading cleanup. Apply the P316 command-provenance, control and reconstruction-root repairs to the README; additionally describe its two 123-state counts as audit-entry counts. The new report header uses 123 entries covering 119 distinct hashes. A hash distinction is not a proof of mathematically distinct fields. The earlier 13920-point evaluations retain their own historical grid descriptions.

For both identical generator copies, change four header string literals only. The exact prefix, suffix and AST outside their one header assignment remain identical. Thus numerical loops, data resolution and CSV output instructions are preserved. Static parsing checks syntax without executing the generator. A separate whitelist parser reads only string constants, their concatenations, the explicit REG_NAMES string list and its separator. It rejects every other expression. This decodes the literal header data and proves its byte equality with the proposed Markdown header, including newlines. The reflow relative to the older P313 approved Markdown changes whitespace only.

The manifest proposal changes exactly the generator's one digest line to the hash of the proposed code/ source. Its validity is conditional on adopting that source together with the manifest and preserving all other code files. It is not a checksum assertion about the unchanged current NUM tree. Actual adoption and all current code hashes need a subsequent readback. The existing 08:07 header-update and 07:58 checksum-refresh timestamps are deliberately retained as historical events, not claimed preparation or adoption times. The adopter must record the actual later adoption and checksum refresh; this verifier cannot write that event in advance.

All Markdown table rows, README command lines and CSV bytes are preserved. Old numerical assertions remain refuted until actual adoption is observed. This proposal supplies a concrete repair, not evidence that another lane has applied it.

## Scope
No NUM code is imported or executed. No new inverse, PDE or solver evaluation, continuum accuracy, candidate existence, general nonexistence, completed run or actual adoption is asserted. Write only in verification. No JavaScript/TypeScript, servers/listeners, RLScience cluster, Lean/Lake builds or external posts.

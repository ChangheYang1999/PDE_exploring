# Retained separation-audit input versions

Checked 2026-10-31T19:02:17.945803+00:00.

The stated recovery claim is CONFIRMED for the two completed pool C audits. All 802 distinct input versions were recovered and their compressed and decompressed hashes verified. Seven versions required an older, exactly matching line-boundary prefix of a growing JSONL file. The snapshots contain 199023594 uncompressed bytes in 7979129 compressed bytes.

Five component checks passed: an unchanged file, an appended stream, the empty prefix, a lossless archive, and rejection of a wrong hash. The integration check verifies each input-to-audit association, digest, size and aggregate byte count. Its receipt is verification/checks.json; the snapshot manifest is bot_research/runs/validation/reserved-C-best-v9e-001-separation-inputs-001/manifest.json.

The terminal pipeline now snapshots its separation-audit inputs and verifies those blobs before publication. Its holdout manifest and all previously frozen inputs are unchanged. No candidate or opponent was called. This check preserves audit evidence; it does not expand the original overlap searches, turn known opponent families into unseen families, or create independent statistical samples.

Reproduce the retained-snapshot check with the project environment, disabled bytecode and research-local temporary directory by running `python -B -m bot_research.experiments.validation.check_audit_input_snapshots` on a fresh output copy. The existing result is exclusive and is not overwritten.

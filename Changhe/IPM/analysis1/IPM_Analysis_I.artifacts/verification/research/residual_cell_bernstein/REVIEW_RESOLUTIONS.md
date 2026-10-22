# Review resolutions

The actual claude-opus-5-5 proof review ended normally at2026-10-21T15:22:47.920946Z. Its requests about exact input interpretation, the fixed precision and partition, per-cell tail scaling and the shared Bernstein conversion were resolved in ADDENDUM.md before the range computations.

The code review ended normally at2026-10-21T15:27:42.519142Z, request9f03b8d1-0777-41fb-8aa2-d0c1809c67bb. It accepted the mathematics and code, with input and dimension hardening requested. I checked its points against the actual sources and plan rather than assuming the evidence files were absent or adequate.

1. All six inherited coefficient files, the old output audit and the accepted verdict already occur in the fixed arithmetic_plan file dictionary. The current scripts check every such pin. The separate check_guards.py additionally requires these exact paths explicitly and anchors the old verdict to its accepted literal digest. No running or previously used source is changed.
2. check_guards.py explicitly checks each source has522 modes, degree64 and exactly65 coefficient boxes per mode. The inherited theorem independently supplies the omitted-degree tail. No silently ignored extra residual mode is permitted.
3. The subdivision output already pins the exact file through its own files dictionary, including the primary file path added immediately before output. The separate guard explicitly checks this pin and verifies planUTC < exactUTC < subdivisionUTC < finalauditUTC for all27 chunks. Timestamps supplement byte bindings; they are not proof of correct arithmetic by themselves.
4. audit_output.py explicitly checks every saved ci equals its position. The accepted topic144 label audit already checks all derivative labels and their exact cap bindings. The supplementary guard checks every per-cell order, h and interval is identical and the tail is the per-cell tail. The mathematical semantics remain D_t and D_theta of the same residual modal series as in the inherited proof, not Cartesian derivatives without conversion.
5. A limit on the width of the Arb maximum enclosure is not needed for the bound: the exact rational maxima are used after every coefficient and stream comparison. The widths remain recorded. Wide balls are not clipped.
6. Both methods share the proved power-to-Bernstein formula. The direct method composes locally; the checker composes globally and subdivides. This partial independence is stated explicitly. Exact stream agreement plus Arb enclosure checks are the finite arithmetic evidence; sampled values are not substituted for those checks.

These resolutions do not assert that pending chunks or the completed-output audit have passed. A complete output review and final adjudication are required before acceptance.

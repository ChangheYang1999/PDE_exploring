Reference outputs of FINAL_REPORT section 5 steps 1 and 2 on the candidate (c6g_shape.npz, md5 15f8095f), from the
verifier's evaluator (d_evaluator/code), for comparison with a reproduction. Times are UTC file modification times.

Step 1 (gen_audit.sh; tag c6g, inner radius 7.652e-4, outer radius 7.652e6):
  c6g_N11250_q384_R7.652e6.json/.log   2026-10-18T15:10:47Z
  c6g_N16875_q512_R7.652e6.json/.log   2026-10-18T15:16:22Z
  c6g_N16875_q768_R7.652e6.json/.log   2026-10-18T15:28:16Z
  c6g_N22500_q384_R7.652e6.json/.log   2026-10-18T17:32:20Z
  c6g_N22500_q512_R7.652e6.json/.log   2026-10-18T15:21:33Z
  rssd_N16875_q384_R7.652e6.json/.log  2026-10-19T11:36:07Z. No earlier output exists for this configuration (section 4
                                       does not use it); this file is the output of the memory measurement, tag rssd.
Step 2:
  c6g_extra.log                        extra_checks.sh, 2026-10-18T15:12:32Z
  c6g_zeros.json                       its zeros of W on the axes (vzeros.py), same run
  c6g_vb3ibp.out                       printed output of vb3ibp.py on the traces of that run (run 2026-10-19T11:30:38Z
                                       on the traces of 2026-10-18T15:12Z)
  c6g_N16875_q384_R7.652e6_ax.json     vaxis.py, 2026-10-18T15:16:35Z
  c6g_N16875_q384_R7.652e6_jd2.json    vchar_dense.py, 2026-10-18T15:14:28Z
Step 3: the reference outputs are the candidate's scan files in c_diagnostics (c6g_scan.json, c6g_scan960.json).

A reproduction on 2026-10-19 (11:04Z to 11:43Z, on a fresh copy of the artifacts) gave JSON files equal to these
in every numeric and string leaf except file names and timings, a log of extra_checks.sh equal line by line after
removal of timestamps and the tag, and the same printed output of vb3ibp.py. MD5SUMS lists the md5 of each file here.

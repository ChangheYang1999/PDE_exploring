# S1M4P producer provenance (written 2026-10-28 15:45Z, a session; answers theory author message 47 item 4(a))

- Launch: 2026-10-28T12:42Z, `FSEC_MODE=S1 FSEC_CKPT_SEC=600 python3 -u fsec.py S1M4P 4 60 4 256 all` (pure splines, m = 1, 2, 3, 78 new-basis
  columns, 1569 cells, 4 workers, round-robin assignment sorted(expected)[w::4]), with the fsec.py of 12:41Z. Never resumed; no base_*.npz.
- The 12:41Z fsec.py file was NOT frozen before it was edited; no byte copy of it exists. What is known about it: it computed the cos^4 input
  quotients VM[m] by numpy.linalg.pinv on padded columns (verifier V187: about 1e-7 relative, padding dependent), stored done sets in the parts,
  wrote no cells_expected and no settings record to meta.json (the sidecar cells_expected.json was written 12:48Z; meta.json unchanged since
  12:45Z, SHA256 recorded by the verifier in proofs/198 as 2b430a2e...). The checkpoint/part format is the one of the 12:35Z resume fix.
- Edits of fsec.py after the launch (work log 13:00Z, 13:12Z, 14:58Z): exact integer VM templates Q_j = 2 (-1)^(m-1-j) (2m-2j-1) replacing pinv;
  settings record in meta.json with a producer/VM marker; refusal to resume a run without a settings record (FSEC_FORCE_RESUME=1 overrides).
  Nothing in the cell sampling, node rules, operator image or accumulation was changed. Current fsec.py SHA256 at 15:45Z:
  e9300283cfb0118acba28675fcbdad56fde2ee1cd9ea43cfbd6a6c1c5f3b67fc.
- Consequence: the S1M4P parts carry the pinv input-quotient error in G_Z (input side), directly measurable against the exact V202 Gram
  (gram_compare.py); the output quotients (B_Y) carry an uncontrolled division error (V187/V189). All S1M4P values are FLOATING diagnostics.

# Theory_v03 audit record

Recorded 2026-10-29T04:00:48.631092+00:00.

Read PROOF.md, then verification/result.json. The frozen publication is
source/theory_v03.md; changes.diff compares it with theory_v02.

The scalar check uses previously independently certified mode7 intervals,
not a new candidate field generation. Run from the lane root:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 taskset -c 50,51 nice -n 19 working file python3 (not published) -B audit/theory_audit/research_code/theory_v03_audit/code/check.py
```

PROOF.md SHA256 8fe7d3cf2546f9f709ba7f33c3516f253b078e72bab06e973877c72751ef3dc3
code/check.py SHA256 6dcc3d8d667b8589651da74f714205ee7f7102add8fe13458ebf0744fe62c976
verification/result.json SHA256 ffa1a7d0fb6fba2bd9a9787b9d8e9ff0b084f6b15339f9bdc4aca1002b09910e

T4-214 through219 give separate verdicts. The next theory publication
should repair the listed conditions. Existing strict ball exclusions
are unchanged. No JavaScript/TypeScript, server, cluster, remote compute,
GPU or Lean/Lake execution was used.

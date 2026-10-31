#!/usr/bin/env python
"""D6FP: sha256 of the production source files (the state the gate results and jobs refer to); prints a markdown table."""
import hashlib, os, sys, time
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FILES = ["src/pressure/poisson_sh.py", "src/optimization/problem.py", "src/optimization/lm.py", "src/optimization/param_map.py", "src/equations/fields.py",
         "src/equations/linear_stable.py", "src/equations/residuals.py", "src/bases/radial.py", "src/bases/jets.py", "src/bases/solid_harmonics.py", "src/bases/solid_harmonics_dd.py",
         "src/far_field/correction.py", "src/optimization/tail_constraints.py", "src/validation/spec_diagnostics.py", "scripts/worker_d6.py", "scripts/supervisor.py",
         "scripts/enqueue_d6.py", "validation/gates.py", "validation/g3_addon.py", "validation/g8_controls.py", "validation/g8_tables.py", "validation/far_noise_split.py"]
print(f"| file | sha256 (first 16) | mtime (UTC) |\n|---|---|---|")
for rel in FILES:
    fp = os.path.join(ROOT, rel)
    if not os.path.exists(fp):
        print(f"| {rel} | missing | |"); continue
    h = hashlib.sha256(open(fp, "rb").read()).hexdigest()[:16]
    print(f"| {rel} | {h} | {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(os.path.getmtime(fp)))} |")

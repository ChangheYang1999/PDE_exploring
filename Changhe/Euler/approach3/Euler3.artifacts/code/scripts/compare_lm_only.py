#!/usr/bin/env python
"""Compare two LM-only validation runs (worker cfg lm_only) from the same start: the relative difference of their steps z - z_parent and
of their per-iteration costs (lead 2026-10-25T15:53Z item 2b: first step at most 1e-6 relative, cost decrease within 1 per cent).
Usage: compare_lm_only.py <start A .pt> <start B .pt> <parent start .pt>"""
import sys, torch
A = torch.load(sys.argv[1], map_location="cpu", weights_only=False); B = torch.load(sys.argv[2], map_location="cpu", weights_only=False)
P = torch.load(sys.argv[3], map_location="cpu", weights_only=False)
zp = P["z"].double()
for key in ("z_lm_raw", "z"):
    za, zb = A[key].double(), B[key].double()
    dza, dzb = za - zp, zb - zp
    print(f"{key}: |z_A - z_B| / |z_A - z_parent| = {(za - zb).norm().item() / dza.norm().item():.3e}   (|z_A - z_parent| {dza.norm().item():.3e}, |z_B - z_parent| {dzb.norm().item():.3e}, |z_parent| {zp.norm().item():.3e})")
ca = [h["cost"] for h in A["history"]]; cb = [h["cost"] for h in B["history"]]
c0a = A["meta"].get("cost0"); c0b = B["meta"].get("cost0")
print(f"start cost (meta cost0): A {c0a} B {c0b}")
for i, (x, y) in enumerate(zip(ca, cb)):
    print(f"iteration {i}: cost A {x:.9e} B {y:.9e} relative difference {abs(x - y) / x:.2e}; cost decrease from the start: A {(c0a - x) / c0a:.6e} B {(c0b - y) / c0b:.6e} (relative difference of the decreases {abs((c0a - x) - (c0b - y)) / abs(c0a - x):.2e})")
print("t_jac A", [round(h.get("t_jac", 0), 1) for h in A["history"]], "B", [round(h.get("t_jac", 0), 1) for h in B["history"]])
print("status A", A.get("status"), "B", B.get("status"), "| jtj_blocks A", A["config"].get("jtj_blocks", 1), "B", B["config"].get("jtj_blocks", 1), "| chunk", A["config"].get("chunk"), B["config"].get("chunk"))

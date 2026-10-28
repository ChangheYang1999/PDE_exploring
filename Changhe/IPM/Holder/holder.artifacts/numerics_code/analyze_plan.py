"""Analyse the discrete transport plan (LP row duals) saved by otlp.py: where does mass go?"""
import json, sys, numpy as np
r = json.load(open(sys.argv[1]))
nodes = np.array(r['nodes']); lab = np.array(r['labels']); m = np.array(r['masses']); alpha = r['alpha']
plan = np.array(r['plan'])  # rows: (i, j, dual) for constraint u_i - u_j <= d_ij^alpha
if len(plan) == 0:
    print("no plan saved"); sys.exit()
I = plan[:, 0].astype(int); J = plan[:, 1].astype(int); w = np.abs(plan[:, 2])
d = np.linalg.norm(nodes[I] - nodes[J], axis=1)
cost = np.sum(w*d**alpha)
print(f"V_h = {r['V_h']:.6f}; plan cost sum w d^alpha = {cost:.6f}; pairs {len(w)}; total mass moved {w.sum():.4f} (|m|/2 = {np.abs(m).sum()/2:.4f})")
names = ['near0', 'near1', 'far', 'left']
M = np.zeros((4, 4)); Cc = np.zeros((4, 4))
for a in range(4):
    for b in range(4):
        sel = (lab[I] == a) & (lab[J] == b)
        M[a, b] = w[sel].sum(); Cc[a, b] = np.sum(w[sel]*d[sel]**alpha)
print("mass moved between regions (rows: from i, cols: to j) and cost:")
for a in range(4):
    print(f"  {names[a]:6s} " + " ".join(f"{M[a,b]:7.4f}" for b in range(4)) + "   | cost " + " ".join(f"{Cc[a,b]:7.4f}" for b in range(4)))
# near fields: distance relative to the scale (distance of the pair's midpoint to the pole)
for a, pole in [(0, np.array([0.0, 0.0])), (1, np.array([1.0, 0.0]))]:
    sel = (lab[I] == a) & (lab[J] == a)
    mid = 0.5*(nodes[I[sel]] + nodes[J[sel]]); rho = np.linalg.norm(mid - pole, axis=1)
    ratio = d[sel]/rho
    print(f"  within {names[a]}: pairs {sel.sum()}, d/rho quantiles 10/50/90%: {np.percentile(ratio,[10,50,90]).round(3)}, cost {Cc[a,a]:.4f}")
sel = (lab[I] == 2) & (lab[J] == 2)
mid = 0.5*(nodes[I[sel]] + nodes[J[sel]]); rho = np.linalg.norm(mid - np.array([0.5, 0]), axis=1)
rI = np.linalg.norm(nodes[I[sel]] - [0.5, 0], axis=1); rJ = np.linalg.norm(nodes[J[sel]] - [0.5, 0], axis=1)
print(f"  within far: pairs {sel.sum()}, d/rho quantiles {np.percentile(d[sel]/rho,[10,50,90]).round(3)}, same-shell fraction (|log(rI/rJ)|<0.1): {np.mean(np.abs(np.log(rI/rJ))<0.1):.3f}, cost {Cc[2,2]:.4f}")
# leftover + cross-region pairs: list the biggest by cost
sel = ~(((lab[I] == lab[J]) & (lab[I] != 3)))
idx = np.argsort(-(w*d**alpha)[sel])[:12]
print("  largest cost pairs involving leftover or cross-region:")
for t in idx:
    i, j = I[sel][t], J[sel][t]
    print(f"    {names[lab[i]]:6s} {nodes[i].round(3)} -> {names[lab[j]]:6s} {nodes[j].round(3)}  w={w[sel][t]:.4f} d={d[sel][t]:.3f} cost={w[sel][t]*d[sel][t]**alpha:.4f}")

"""Assemble the fsec.py blocks so that every cell is counted exactly once (v2, 12:40Z; lead note 38 / verifier topic 176: v1 summed
parts + bases + checkpoints and double-counted the checkpointed cells; v1 kept as fsec_assemble_v1.py).
Blocks: base_*.npz (merged earlier checkpoints of a resumed run; carry their done sets), part_<wid>.npz (final accumulator of a worker over
its cells of the CURRENT launch; done set stored since 12:40Z), ckpt_<wid>_<pid>.npz (cumulative checkpoint of a worker of the current launch;
used only for workers WITHOUT a part, i.e. an incomplete run). Coverage: the done sets must be pairwise disjoint and their union must be the
run's cell set; parts without a done set (runs before 12:40Z) are accepted only for a never-resumed completed run (no base files, all workers
present), with sum(diag cells) == number of cells of the cover (1569 for the production cover).
Then: generalized singular values of (B_Y, G_Z) (50-digit solve of the double pair, as s1_robust.py), weakest direction, c[h_0] = 0 values.
Usage: python3 fsec_assemble.py runs/<tag>   (FSEC_PARTIAL=1 allows an explicitly partial diagnostic)"""
import sys, os, json, glob, re
import numpy as np
import mpmath as mp
rundir = sys.argv[1]; NEXP = int(sys.argv[2]) if len(sys.argv) > 2 else 1569
meta = json.load(open(os.path.join(rundir, "meta.json")))
nw = int(meta.get("nworkers", 0)) or None
blocks = []       # (name, GZ, BY, done set or None, ncells from diag)
def load(f):
    z = np.load(f, allow_pickle=True); dj = json.loads(str(z["diag"])); dl = dj if isinstance(dj, list) else [dj]
    nc = sum(int(d.get("cells", 0)) for d in dl); done = set(int(x) for x in z["done"]) if "done" in z.files else None
    return z["GZ"], z["BY"], done, nc, dl
for f in sorted(glob.glob(os.path.join(rundir, "base_*.npz"))):
    GZ, BY, done, nc, dl = load(f); blocks.append((os.path.basename(f), GZ, BY, done, nc, dl))
parts = {int(re.search(r"part_(\d+)\.npz", f).group(1)): f for f in glob.glob(os.path.join(rundir, "part_*.npz"))}
ckpts = {}
for f in glob.glob(os.path.join(rundir, "ckpt_*.npz")):
    wid = int(re.search(r"ckpt_(\d+)_\d+\.npz", f).group(1)); ckpts.setdefault(wid, []).append(f)
for wid in sorted(set(parts) | set(ckpts)):
    if wid in parts: f = parts[wid]
    else: f = max(ckpts[wid], key=os.path.getmtime); print("worker %d has no final part: using its latest checkpoint %s (INCOMPLETE run)" % (wid, os.path.basename(f)))
    GZ, BY, done, nc, dl = load(f); blocks.append((os.path.basename(f), GZ, BY, done, nc, dl))
print("blocks:", [(b[0], b[4], None if b[3] is None else len(b[3])) for b in blocks])
# coverage check against the EXPECTED cell set (v3, 12:50Z, verifier V188: cardinality alone is not enough)
side = os.path.join(rundir, "cells_expected.json")
if "cells_expected" in meta: expected = set(int(i) for i in meta["cells_expected"]); src = "meta.json"
elif os.path.exists(side): expected = set(int(i) for i in json.load(open(side))["cells_expected"]); src = "cells_expected.json (sidecar)"
else: raise SystemExit("no expected cell set (meta.json cells_expected or cells_expected.json): cannot verify coverage")
PARTIAL = os.environ.get("FSEC_PARTIAL") == "1"
have_done = all(b[3] is not None for b in blocks)
if not have_done:
    # legacy parts (before 12:40Z) carry no done sets: reconstruct the deterministic assignment chunks = sorted(expected)[w::nw] of a never-resumed run
    assert not glob.glob(os.path.join(rundir, "base_*.npz")), "parts without done sets in a resumed run: cannot verify coverage"
    nwl = int(meta.get("nworkers", 0)) or len(parts); idx_sorted = sorted(expected); fixed = []
    for b in blocks:
        if b[3] is None:
            wid = int(re.search(r"part_(\d+)\.npz", b[0]).group(1)); dset = set(idx_sorted[wid::nwl])
            assert len(dset) == b[4], "legacy part %s: reconstructed %d cells but diag counts %d" % (b[0], len(dset), b[4])
            fixed.append((b[0], b[1], b[2], dset, b[4], b[5]))
        else: fixed.append(b)
    blocks = fixed; print("legacy parts: cell sets reconstructed from the assignment sorted(expected)[w::%d] (counts match the diag)" % nwl)
allc = set(); tot = 0
for b in blocks:
    assert not (allc & b[3]), "overlapping cell sets in block " + b[0]; allc |= b[3]; tot += len(b[3])
    assert len(b[3]) == b[4], "done set and diag cell count differ in " + b[0]
missing = expected - allc; extra = allc - expected
print("coverage: %d cells in %d disjoint blocks; expected %d (%s); missing %d, extra %d" % (tot, len(blocks), len(expected), src, len(missing), len(extra)))
assert not extra, "blocks contain cells outside the expected set: %s" % sorted(extra)[:10]
if missing:
    if not PARTIAL: raise SystemExit("INCOMPLETE: %d expected cells missing (e.g. %s); set FSEC_PARTIAL=1 for an explicitly partial diagnostic" % (len(missing), sorted(missing)[:10]))
    print("PARTIAL DIAGNOSTIC: %d expected cells missing" % len(missing))
GZ = sum(b[1] for b in blocks); BY = sum(b[2] for b in blocks); GZ = (GZ + GZ.T) / 2; BY = (BY + BY.T) / 2
diags = [d for b in blocks for d in b[5]]
n = GZ.shape[0]; new = meta["new"]; cvec = np.array(meta["cvec"])
wz = np.linalg.eigvalsh(GZ); print("G_Z eig min/max %.3e %.3e cond %.2e" % (wz[0], wz[-1], wz[-1] / wz[0]))
mp.mp.dps = 50
G = mp.matrix(GZ.tolist()); B = mp.matrix(BY.tolist()); L = mp.cholesky(G); Li = mp.inverse(L); Bw = Li * B * Li.T; Bw = (Bw + Bw.T) / 2
# (13:00Z) the whitening L^{-1} B L^{-T} is formed at 50 digits (this is where cond(G_Z) ~ 1e13..1e15 bites); the symmetric eigenproblem of the
# whitened matrix (entries O(1e6), well conditioned) is then solved in double: eigenvalues accurate to about 1e-9 absolute, the mpmath eigsy at
# 50 digits (minutes for n = 84) gave the same digits for S1/S1M3.
Bwf = np.array([[float(Bw[i, j]) for j in range(n)] for i in range(n)]); Bwf = (Bwf + Bwf.T) / 2
ev, Vf = np.linalg.eigh(Bwf); sv = np.sqrt(np.maximum(ev, 0))
print("generalized singular values (50-digit whitening, double eigen-solve; smallest 8): %s ; largest %.4e" % (np.array2string(sv[:8], precision=5), sv[-1]))
Lif = np.array([[float(Li[i, j]) for j in range(n)] for i in range(n)]); x = Lif.T @ Vf[:, 0]; x /= np.linalg.norm(x)   # x = Li^T v
top = np.argsort(-np.abs(x))[:8]; print("weakest direction:", [(new[i][0], new[i][1], new[i][2], round(float(x[i]), 4)) for i in top])
# restriction to c[h_0] = 0 (orthogonal complement of the strain functional in the G_Z metric)
cw = np.array([float(sum(Li[i, j] * cvec[j] for j in range(n))) for i in range(n)])
if np.linalg.norm(cw) > 0:
    u = cw / np.linalg.norm(cw); P = np.eye(n) - np.outer(u, u)
    evc = np.sort(np.linalg.eigvalsh(P @ Bwf @ P)); svc = np.sqrt(np.maximum(evc[1:], 0)); print("on the subspace c[h_0] = 0 (smallest 6): %s" % np.array2string(svc[:6], precision=5))
else: svc = sv
res = dict(tag=meta["tag"], n=n, sigma_all=sv[:8].tolist(), sigma_max=float(sv[-1]), sigma_c0=svc[:8].tolist(), GZ_cond=float(wz[-1] / wz[0]),
           weakest=[(new[i][0], new[i][1], new[i][2], float(x[i])) for i in top], blocks=[(b[0], b[4]) for b in blocks], cells=int(tot), diags=diags,
           NMAX=meta["NMAX"], Mh=meta["Mh"], stride=meta["stride"], assembler="v3 (12:50Z): parts/bases/latest-ckpt, union of done sets == expected cell set (legacy assignment reconstructed); 50-digit solve", expected_cells=len(expected), missing_cells=len(missing), partial=PARTIAL)
json.dump(res, open(os.path.join(rundir, "fsec_result.json"), "w"), indent=1); print("saved", os.path.join(rundir, "fsec_result.json"))

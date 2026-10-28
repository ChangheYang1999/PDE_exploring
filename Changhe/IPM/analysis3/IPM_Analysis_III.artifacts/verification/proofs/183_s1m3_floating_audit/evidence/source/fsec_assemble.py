"""Assemble the fsec.py parts: generalized singular values of L_red : Z_N -> Y in the w_a jet realization (floating point).
Usage: python3 fsec_assemble.py runs/<tag>"""
import sys, os, json, glob
import numpy as np
import scipy.linalg as sla
rundir = sys.argv[1]
meta = json.load(open(os.path.join(rundir, "meta.json")))
GZ = None; BY = None; diags = []
for f in sorted(glob.glob(os.path.join(rundir, "part_*.npz")) + glob.glob(os.path.join(rundir, "base_*.npz")) + glob.glob(os.path.join(rundir, "ckpt_*.npz"))):
    z = np.load(f, allow_pickle=True)
    GZ = z["GZ"] if GZ is None else GZ + z["GZ"]; BY = z["BY"] if BY is None else BY + z["BY"]
    dj = json.loads(str(z["diag"])); diags.extend(dj if isinstance(dj, list) else [dj]); print("  loaded", os.path.basename(f))
GZ = (GZ + GZ.T) / 2; BY = (BY + BY.T) / 2
n = GZ.shape[0]; new = meta["new"]; cvec = np.array(meta["cvec"])
wz = np.linalg.eigvalsh(GZ); print("G_Z eig min/max %.3e %.3e cond %.2e" % (wz[0], wz[-1], wz[-1] / wz[0]))
# whitening by Cholesky of G_Z
R = np.linalg.cholesky(GZ)                # GZ = R R^T
Rinv = np.linalg.inv(R)
Bw = Rinv @ BY @ Rinv.T; Bw = (Bw + Bw.T) / 2
ev, V = np.linalg.eigh(Bw)
sv = np.sqrt(np.maximum(ev, 0))
print("generalized singular values of L_red on Z_N (smallest 6): %s ; largest %.4e" % (np.array2string(sv[:6], precision=5), sv[-1]))
x = Rinv.T @ V[:, 0]; x /= np.linalg.norm(x)
top = np.argsort(-np.abs(x))[:8]
print("weakest direction:", [(new[i][0], new[i][1], new[i][2], round(float(x[i]), 4)) for i in top])
# restriction to c[h_0] = 0: project onto the orthogonal complement (in the G_Z metric) of the strain functional
cw = Rinv @ cvec                        # c(x) = cvec . x = cw . (R^T x)
if np.linalg.norm(cw) > 0:
    u = cw / np.linalg.norm(cw)
    P = np.eye(n) - np.outer(u, u)
    Bc = P @ Bw @ P
    evc = np.linalg.eigvalsh(Bc); evc = np.sort(evc)
    svc = np.sqrt(np.maximum(evc[1:], 0))        # drop the projected-out direction (eigenvalue 0)
    print("on the subspace c[h_0] = 0 (smallest 6): %s" % np.array2string(svc[:6], precision=5))
else:
    svc = sv
# jet-only and remainder-only blocks (diagnostic)
jet = [i for i, (k_, l_, m_) in enumerate(new) if k_ == "jet"]; rem = [i for i, (k_, l_, m_) in enumerate(new) if k_ == "rem"]
for name, idx in (("jet", jet), ("remainder", rem)):
    Gs = GZ[np.ix_(idx, idx)]; Bs = BY[np.ix_(idx, idx)]
    Rs = np.linalg.cholesky(Gs); Ri = np.linalg.inv(Rs); evs = np.linalg.eigvalsh((Ri @ Bs @ Ri.T + (Ri @ Bs @ Ri.T).T) / 2)
    print("  %s block alone: smallest 3 generalized singular values %s" % (name, np.array2string(np.sqrt(np.maximum(evs[:3], 0)), precision=5)))
res = dict(tag=meta["tag"], n=n, sigma_all=sv[:8].tolist(), sigma_max=float(sv[-1]), sigma_c0=svc[:8].tolist(), GZ_cond=float(wz[-1] / wz[0]),
           weakest=[(new[i][0], new[i][1], new[i][2], float(x[i])) for i in top], diags=diags, NMAX=meta["NMAX"], Mh=meta["Mh"], stride=meta["stride"])
json.dump(res, open(os.path.join(rundir, "fsec_result.json"), "w"), indent=1)
print("saved", os.path.join(rundir, "fsec_result.json"))

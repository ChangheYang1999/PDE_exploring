import json, sys
import numpy as np
p = sys.argv[1]
d = np.load(p, allow_pickle=False)
R = d["R"]; n = R.shape[0]
cn = np.linalg.norm(R, axis=0); cs = np.where(cn > 0, cn, 1.0); R = R / cs[None, :]
s = np.linalg.svd(R, compute_uv=False)
rel = s / s[0]
out = {"record": p.rsplit("/", 2)[-2] + "/" + p.rsplit("/", 1)[-1], "s_max": float(s[0]), "zero_columns": int((cn == 0).sum())}
for t in [1e-6, 1e-8, 1e-10, 1e-12]:
    i = int(np.argmin(np.abs(rel - t)))
    out[str(t)] = {"kept": int((rel > t).sum()), "nearest_rel": float(rel[i]), "normalized_margin": float(abs(rel[i] - t))}
print(json.dumps(out, indent=1))

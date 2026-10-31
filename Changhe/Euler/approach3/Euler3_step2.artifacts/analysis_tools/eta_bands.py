"""eta band decomposition (lead diagnostic, information only): for a linearization record (R, Qtr, r_norm2 of the
column-scaled Jacobian), the share of ||r||^2 in left singular directions per band of s/s_max, and the norm of the
undamped Gauss-Newton step restricted to each band (scaled coordinates), plus its parameter part in physical units.
Usage: eta_bands.py record.npz [record.npz ...]"""
import json, sys
import numpy as np
EDGES = [1.0, 1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-8, 1e-10, 1e-12, 0.0]
out = {}
for path in sys.argv[1:]:
    d = np.load(path, allow_pickle=False)
    R = d["R"]; qtr = d["Qtr"]; rr = float(d["r_norm2"]); D = np.array(d["D"], float); n = R.shape[0]
    assert np.array_equal(d["perm"], np.arange(n)) and list(d["param_positions"]) == [n - 2, n - 1]
    cn = np.linalg.norm(R, axis=0); cs = np.where(cn > 0, cn, 1.0); R = R / cs[None, :]; D = D * cs
    chain = np.array([float(d["chain_dcl_dzc"]), float(d["chain_domega_dzw"])])
    U, s, Vt = np.linalg.svd(R)
    c = U.T @ qtr
    rel = s / s[0]
    bands = []
    for hi, lo in zip(EDGES[:-1], EDGES[1:]):
        m = (rel <= hi) & (rel > lo) if lo > 0 else (rel <= hi)
        share = float((c[m] ** 2).sum() / rr)
        with np.errstate(divide="ignore", invalid="ignore"):
            coef = np.where(m & (s > 0), -c / np.where(s > 0, s, 1.0), 0.0)
        step = Vt.T @ coef                       # scaled step x_s; physical parameter step = x_s / D (optimizer coords) * chain
        dz = step[n - 2:] / D[n - 2:]
        bands.append({"band": [hi, lo], "count": int(m.sum()), "eta_share": share,
                      "gn_step_norm_scaled": float(np.linalg.norm(step)),
                      "param_step_physical": [float(dz[0] * chain[0]), float(dz[1] * chain[1])]})
    out[path.rsplit("/", 2)[-2] + "/" + path.rsplit("/", 1)[-1]] = {
        "kind": str(d["jacobian_kind"]), "it": int(d["it"]), "O1": rr / 2, "s_max": float(s[0]),
        "residual_outside_range": float(1 - (c ** 2).sum() / rr), "bands": bands}
print(json.dumps(out, indent=1))

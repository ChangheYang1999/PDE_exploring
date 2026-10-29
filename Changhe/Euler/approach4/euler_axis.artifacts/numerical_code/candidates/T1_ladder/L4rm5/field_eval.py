"""Self-contained numpy evaluator of a candidate (phi, q) from coeffs.npz (SPEC 10). Values only.
Usage: from field_eval import eval_phi_q; phi, q = eval_phi_q(r, z)    (r, z arrays of equal shape)
Definitions: see BASIS.md next to this file. Written by scripts/export_candidate.py of the numerics lane."""
import os, json
import numpy as np
from numpy.polynomial import legendre as _Leg, chebyshev as _Cheb

_HERE = os.path.dirname(os.path.abspath(__file__))
_D = np.load(os.path.join(_HERE, "coeffs.npz"), allow_pickle=False)
_M = json.loads(str(_D["meta_json"]))

def _legendre_matrix(mu, nmax):
    return np.array([_Leg.legval(mu, np.eye(nmax + 1)[n]) for n in range(nmax + 1)]).T          # (npts, nmax+1)

def _jacobi(x, kmax, a, b):
    """P_k^{(a,b)}(x), k = 0..kmax (three-term recurrence); (len(x), kmax+1)."""
    x = np.asarray(x, float); P = np.zeros((x.size, kmax + 1)); P[:, 0] = 1.0
    if kmax >= 1: P[:, 1] = 0.5 * ((a + b + 2) * x + (a - b))
    for k in range(1, kmax):
        c = 2 * k + a + b
        P[:, k + 1] = ((c + 1) * ((c + 2) * c * x + a * a - b * b) * P[:, k] - 2 * (k + a) * (k + b) * (c + 2) * P[:, k - 1]) / (2 * (k + 1) * (k + a + b + 1) * c)
    return P

def _element_basis(el, R, mu):
    """Columns of the element's basis at points (R, mu), in the coefficient order of BASIS.md."""
    nmax = el["nmax"]; P = _legendre_matrix(mu, nmax)
    cols = []
    if el["kind"] == "ball":
        R1 = el["Rhi"]; D = el["D"]; rho = R / R1; x = 2 * rho**2 - 1
        radial = el.get("radial", "cheb")
        for n in range(nmax + 1):
            Kn = (D - n) // 2
            if Kn < 0: continue
            Q = _jacobi(x, Kn, 0.0, n + 0.5) if radial == "jacobi" else None
            for k in range(Kn + 1):
                qk = Q[:, k] if radial == "jacobi" else _Cheb.chebval(x, np.eye(Kn + 1)[k])
                cols.append(P[:, n] * rho**n * qk)
    elif el["kind"] == "shell":
        Rlo, Rhi, K = el["Rlo"], el["Rhi"], el["K"]
        x = 2 * np.log(R / Rlo) / np.log(Rhi / Rlo) - 1
        for n in range(nmax + 1):
            for k in range(K + 1):
                cols.append(P[:, n] * _Cheb.chebval(x, np.eye(K + 1)[k]))
    elif el["kind"] == "exterior":
        Rm = el["Rlo"]
        for n in range(nmax + 1):
            for e in el["exponents"]:
                cols.append(P[:, n] * (R / Rm) ** (-e))
    return np.array(cols).T if cols else np.zeros((len(R), 0))

def eval_phi_q(r, z):
    r = np.asarray(r, float); z = np.asarray(z, float); shp = r.shape
    r = r.ravel(); z = z.ravel()
    R = np.sqrt(r * r + z * z); mu = np.where(R > 0, z / np.where(R > 0, R, 1.0), 1.0)
    phi = np.zeros_like(R); q = np.zeros_like(R)
    els = _M["elements"]
    for i, el in enumerate(els):
        lo = el["Rlo"] if i > 0 else -1.0
        m = (R > lo) & (R <= el["Rhi"]) if el["Rhi"] is not None else (R > lo)
        if not np.any(m): continue
        B = _element_basis(el, R[m], mu[m])
        cphi = _D[f"phi_el{i}"]; cq = _D[f"q_el{i}"]
        Bphi = B[:, el["phi_cols"]]; Bq = B[:, el["q_cols"]]        # column subsets (exponent sets, parity masks)
        phi[m] = Bphi @ cphi; q[m] = Bq @ cq
    return phi.reshape(shp), q.reshape(shp)

if __name__ == "__main__":
    S = np.load(os.path.join(_HERE, "samples.npz"))
    phi, q = eval_phi_q(S["r"], S["z"])
    print("max |phi - samples|:", np.max(np.abs(phi - S["phi"])), " max |q - samples|:", np.max(np.abs(q - S["q"])))

"""Exact Laurent products with a separate angular shift for each branch."""
from pathlib import Path
import sys
import time
from flint import fmpq, fmpq_poly

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research/radial_fourier/code"))
from radial import T, ZERO, put, pshift


def packed_product(C, S, verbose=False):
    start = time.monotonic()
    if not C or not S:
        return {}
    stride = max(P.degree() for P in C.values())+max(P.degree() for P in S.values())+1

    def pack(A, kind):
        groups = {}
        for (j, n), P in A.items():
            groups.setdefault(j, []).append((n, P))
        out = {}
        for j, rows in groups.items():
            center = max(n for n, P in rows)
            coefficients = [fmpq(0)]*(stride*(2*center+1))
            for n, P in rows:
                for k, v in enumerate(P):
                    coefficients[stride*(center+n)+k] += v
                    coefficients[stride*(center-n)+k] += v if kind == "c" else -v
            out[j] = center, fmpq_poly(coefficients)
        return out

    cp, sp = pack(C, "c"), pack(S, "s")
    products = {}
    for i, (ci, P) in sorted(cp.items()):
        for j, (cj, Q) in sorted(sp.items()):
            key = i+j+1, ci+cj
            products[key] = products.get(key, ZERO)+P*Q
        if verbose:
            print("tight branch", i, "seconds", time.monotonic()-start, flush=True)
    out = {}
    for (h, center), P in products.items():
        for n in range(1, center+1):
            value = fmpq_poly([P[stride*(center+n)+k]/2 for k in range(stride)])
            if value:
                out[h, n] = out.get((h, n), ZERO)+value
    return {key: P for key, P in out.items() if P}


def residual_sine(model, verbose=False):
    out = {}
    for (j, n), P in model.rho.items():
        TP = T*P.derivative()
        L = model.c*(2*TP-3*P+2*T*(model.p[j]*P-TP))-P
        put(out, (j, n), pshift(L, 2))
    for C, S in [(model.u1, model.rx), (model.ry, model.u2)]:
        for key, P in packed_product(C, S, verbose).items():
            put(out, key, pshift(P, 4))
    return {key: P for key, P in out.items() if P}

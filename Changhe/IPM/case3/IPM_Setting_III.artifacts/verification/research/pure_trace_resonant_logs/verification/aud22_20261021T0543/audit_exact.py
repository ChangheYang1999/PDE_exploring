"""Independent exact arithmetic for the supplied exterior resonance audit."""

import json
import os
import resource
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path

resource.setrlimit(resource.RLIMIT_AS, (1800000000, 1800000000))
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1")
checks = 0


def check(left, right):
    global checks
    assert left == right, (left, right)
    checks += 1


def clean(a):
    return {n: v for n, v in a.items() if v}


def add(*terms):
    out = defaultdict(F)
    for a in terms:
        for n, v in a.items():
            out[n] += v
    return clean(out)


def scale(a, c):
    return clean({n: c * v for n, v in a.items()})


def sine_add(out, n, c):
    if n > 0:
        out[n] += c
    elif n < 0:
        out[-n] -= c


def sine_source(a, s):
    out = defaultdict(F)
    for n, v in a.items():
        sine_add(out, n + 1, v * (s - n) / 2)
        sine_add(out, n - 1, v * (s + n) / 2)
    return clean(out)


def sine_advection(h, a, si, sj):
    out = defaultdict(F)
    for m, hv in h.items():
        for n, av in a.items():
            sine_add(out, n + m, hv * av * (-m * sj + (si + 1) * n) / 2)
            sine_add(out, n - m, hv * av * (-m * sj - (si + 1) * n) / 2)
    return clean(out)


def to_laurent(a):
    return {key: val for n, v in a.items() for key, val in ((n, -v / 2), (-n, v / 2))}


def shift(a, q, y=False):
    out = defaultdict(F)
    for n, v in a.items():
        out[n + 1] += v * ((n - q) if y else (q - n)) / 2
        out[n - 1] += v * (q + n) / 2
    return clean(out)


def convolution(a, b):
    out = defaultdict(F)
    for m, u in a.items():
        for n, v in b.items():
            out[m + n] += u * v
    return clean(out)


def cartesian_advection(h, a, si, sj):
    return add(
        convolution(shift(h, si + 1, y=True), shift(a, sj)),
        scale(convolution(shift(h, si + 1), shift(a, sj, y=True)), -1),
    )


def negative_laplacian(a, q):
    return add(
        scale(shift(shift(a, q), q - 1), -1),
        shift(shift(a, q, y=True), q - 1, y=True),
    )


def inverse(source, q):
    return {n: v / (n * n - q * q) for n, v in source.items()}


def serial(a):
    return {str(n): str(v) for n, v in sorted(a.items())}


def run_case(ell, K, m, expected):
    p = 1 / ell
    delta = 1 - p
    ss = [p - k * delta for k in range(K + 1)]
    ps = [{1: F(1)}]
    hs = []
    ds = [{1: -F(1, 2), -1: F(1, 2)}]
    streams = []
    records = []
    for k in range(K + 1):
        if k:
            bs = []
            cs = []
            for i in range(k):
                j = k - 1 - i
                b = sine_advection(hs[i], ps[j], ss[i], ss[j])
                c = cartesian_advection(streams[i], ds[j], ss[i], ss[j])
                check(to_laurent(b), c)
                bs.append(b)
                cs.append(c)
            ps.append(scale(add(*bs), 1 / (ell * k * delta)))
            ds.append(scale(add(*cs), 1 / (ell * k * delta)))
        check(to_laurent(ps[k]), ds[k])
        g = sine_source(ps[k], ss[k])
        source = shift(ds[k], ss[k])
        check(to_laurent(g), source)
        record = {"k": k, "s": str(ss[k]), "P": serial(ps[k]), "G": serial(g)}
        if k < K:
            hs.append(inverse(g, ss[k] + 1))
            streams.append(inverse(source, ss[k] + 1))
            check(to_laurent(hs[k]), streams[k])
            check(negative_laplacian(streams[k], ss[k] + 1), source)
            record["H"] = serial(hs[k])
        records.append(record)
    check(g[m], expected)
    check(-2 * source[m], expected)
    check(ss[K], -m - 1)
    check(ps[1], {
        1: -(3 * p + 1) / (4 * ell * delta * (p + 3)),
        3: -1 / (4 * ell * (p + 3)),
    })
    q = expected / (2 * m)
    logforcing = sine_advection({m: q}, {1: F(1)}, -m - 1, p)
    check(logforcing, {m - 1: -expected * delta / 4, m + 1: -expected * (1 + p) / 4})
    check(to_laurent(logforcing), cartesian_advection(to_laurent({m: q}), ds[0], -m - 1, p))
    densitylog = scale(logforcing, 1 / (ell * (m + 2)))
    check(densitylog, {
        m - 1: -expected * delta / (4 * ell * (m + 2)),
        m + 1: -expected * (1 + p) / (4 * ell * (m + 2)),
    })
    check(p - m - 2, p - (K + 1) * delta)
    return {
        "ell": str(ell), "K": K, "m": m, "g": str(g[m]),
        "P1": serial(ps[1]), "density_log": serial(densitylog),
        "records": records,
    }


def check_log_derivatives():
    # Differentiate a Laurent Fourier mode with a polynomial in z=log(r).
    def dx(a, q, y=False):
        out = defaultdict(F)
        for (n, d), v in a.items():
            out[n + 1, d] += v * ((n - q) if y else (q - n)) / 2
            out[n - 1, d] += v * (q + n) / 2
            if d:
                out[n + 1, d - 1] += v * d * (-1 if y else 1) / 2
                out[n - 1, d - 1] += v * d / 2
        return clean(out)
    for m in (2, 4):
        a = {(m, 1): -F(1, 2), (-m, 1): F(1, 2)}
        minuslap = add(
            scale(dx(dx(a, -m), -m - 1), -1),
            dx(dx(a, -m, y=True), -m - 1, y=True),
        )
        check(minuslap, {(m, 0): F(-m), (-m, 0): F(m)})


if __name__ == "__main__":
    cases = [
        run_case(F(3), 5, 2, -F(177047, 301056000000)),
        run_case(F(5, 2), 9, 4, F(
            26243642326438735772269905591088207,
            4898218301752285282303033607434666157015040,
        )),
    ]
    check_log_derivatives()
    result = {"exact_identity_checks": checks, "cases": cases}
    Path("audit_exact_results.json").write_text(json.dumps(result, indent=2) + "\n")
    for case in cases:
        print("ell =", case["ell"], "g =", case["g"], "P1 =", case["P1"])
    print("Exact identity checks:", checks)
    print("Peak resident memory (KiB):", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

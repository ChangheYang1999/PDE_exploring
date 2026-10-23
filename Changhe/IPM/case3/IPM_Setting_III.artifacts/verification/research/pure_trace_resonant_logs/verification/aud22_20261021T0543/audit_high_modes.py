"""Test dependence on an arbitrarily high trace mode, to order epsilon^2."""

import json
from fractions import Fraction as F
from pathlib import Path

from audit_exact import (
    add, scale, sine_source, sine_advection, inverse, to_laurent,
    shift, cartesian_advection, check,
)


def perturb(ell, K, m, N):
    p = 1 / ell
    delta = 1 - p
    ss = [p - k * delta for k in range(K + 1)]
    ps = [[{1: F(1)}, {N: F(1)}, {}]]
    ds = [[to_laurent(a) for a in ps[0]]]
    hs = []
    streams = []
    for k in range(K + 1):
        if k:
            pnext = []
            dnext = []
            for degree in range(3):
                bs = []
                cs = []
                for i in range(k):
                    j = k - 1 - i
                    for a in range(degree + 1):
                        b = degree - a
                        bs.append(sine_advection(hs[i][a], ps[j][b], ss[i], ss[j]))
                        cs.append(cartesian_advection(streams[i][a], ds[j][b], ss[i], ss[j]))
                pnext.append(scale(add(*bs), 1 / (ell * k * delta)))
                dnext.append(scale(add(*cs), 1 / (ell * k * delta)))
                check(to_laurent(pnext[-1]), dnext[-1])
            ps.append(pnext)
            ds.append(dnext)
        gs = [sine_source(a, ss[k]) for a in ps[k]]
        sources = [shift(a, ss[k]) for a in ds[k]]
        for a, b in zip(gs, sources):
            check(to_laurent(a), b)
        if k < K:
            hs.append([inverse(a, ss[k] + 1) for a in gs])
            streams.append([inverse(a, ss[k] + 1) for a in sources])
    values = [a.get(m, F(0)) for a in gs]
    assert values[1] == 0
    assert values[2] != 0
    prime = 1000003
    assert values[2].denominator % prime
    residue = (
        (values[2].numerator % prime)
        * pow(values[2].denominator, -1, prime)
    ) % prime
    return {
        "ell": str(ell), "K": K, "m": m, "N": N,
        "g_epsilon_coefficients_through_degree_2": [str(v) for v in values],
        "epsilon_squared_residue_mod_1000003": residue,
    }


if __name__ == "__main__":
    cases = [
        perturb(F(3), 5, 2, 101),
        perturb(F(5, 2), 9, 4, 101),
    ]
    Path("audit_high_modes_results.json").write_text(json.dumps(cases, indent=2) + "\n")
    for a in cases:
        print("ell =", a["ell"], "N =", a["N"], "epsilon^2 coefficient nonzero;",
              "residue modulo 1000003 =", a["epsilon_squared_residue_mod_1000003"])
    import resource
    print("Peak resident memory (KiB):", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

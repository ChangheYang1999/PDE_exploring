#!/usr/bin/env python3
"""Independent finite Fourier multiplication, recurrence and characteristic checks."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import time
from check_local_two_projection_construction import P

ROOT = Path(__file__).resolve().parents[1]
TOPIC = ROOT / "research/three_projection_disc"
COUNT = 0


def check(value):
    global COUNT
    COUNT += 1
    assert value, COUNT


def determinant(matrix):
    """Sparse Laplace expansion, with no division or symbolic library."""
    n = len(matrix)
    if n == 1:
        return P(matrix[0][0])
    i = min(range(n), key=lambda k: sum(P(x) != 0 for x in matrix[k]))
    answer = P()
    for col, val in enumerate(matrix[i]):
        if P(val) == 0:
            continue
        minor = [[x for k, x in enumerate(row) if k != col]
                 for h, row in enumerate(matrix) if h != i]
        answer += (-1)**(i+col)*P(val)*determinant(minor)
    return answer


def projected(f, g, k, T, S, J, K, L, df, dg, dk, c):
    modes = {1: f, 3: g, 5: k}
    deriv = {1: df, 3: dg, 5: dk}
    stream = {2: (T-J)/2, 4: (S-K)/2, 6: -L/2}
    stream_deriv = {2: (-g-f+4*J)/2, 4: (2*S-k-g+6*K)/2, 6: (-k+8*L)/2}
    out = {n: c*deriv[n]+(c-1)*modes[n] for n in modes}

    def add(n, value):
        if n:
            out[abs(n)] = out.get(abs(n), P())+(1 if n > 0 else -1)*value

    for n, fn in modes.items():
        for m, hm in stream.items():
            q = -m*hm*(fn+deriv[n])/2
            add(n+m, q)
            add(n-m, q)
            q = n*(2*hm+stream_deriv[m])*fn/2
            add(m+n, q)
            add(m-n, q)
    return out


def solve(matrix, right):
    q = [list(map(F, row))+[F(b)] for row, b in zip(matrix, right)]
    for i in range(len(q)):
        pivot = next(j for j in range(i, len(q)) if q[j][i])
        q[i], q[pivot] = q[pivot], q[i]
        divisor = q[i][i]
        q[i] = [x/divisor for x in q[i]]
        for j in range(len(q)):
            if j != i:
                factor = q[j][i]
                q[j] = [a-factor*b for a, b in zip(q[j], q[i])]
    return [row[-1] for row in q]


def scalar(p):
    p = P(p)
    check(not any(p.d.keys()))
    return p.d.get((), F(0))


def matrix_order(c, a, n):
    D = c-1
    return [[(c+1)*n-a/4, D*n+2*D-a/4-a/(2*n), F(0)],
            [D*n-a/4+a/(2*n+4), 2*c*n+D-a/2, (n+3)*(D-a/(4*(n-1)))],
            [F(0), (n-1)*(D-a/(4*(n+3))), 2*c*n+D-a/2]]


def main():
    started = time.monotonic()
    names = ("f", "g", "k", "T", "S", "J", "K", "L")
    f, g, k, T, S, J, K, L = map(P, names)
    a, c, j, z, H = map(P, ("a", "c", "j", "z", "H"))
    df, dg, dk = map(P, ("df", "dg", "dk"))
    D = c-1
    u = (T-J)/2
    B = -u-K+S
    C = K-3*L/2-S
    M = [[c+u, B, C], [B, c-3*L/2, -u], [C, -u, c]]
    fparts = [
        (D+T)*f-f*f/4+f*g/2+(-J+2*K+4*S-2*T)*g+(-4*K+6*L-6*S)*k+g*k/2,
        (J+2*S)*f-f*f/4-f*g/2+(D+3*L)*g+(-2*J-3*T+f+g/2)*k,
        D*k+(2*J+T)*g+2*K*f-f*g-f*k/2-3*g*g/4,
    ]
    direct = projected(f, g, k, T, S, J, K, L, df, dg, dk, c)
    for i, n in enumerate((1, 3, 5)):
        check(direct[n] == sum((M[i][h]*v for h, v in enumerate((df, dg, dk))), P())+fparts[i])
    initial = {"f": a, "g": 0, "k": 0, "T": a/4-D, "S": 0, "J": a/4, "K": 0, "L": 0}
    M0 = [[v.substitute(initial) for v in row] for row in M]
    jac = [[fp.derivative({name: 1}).substitute(initial) for name in names] for fp in fparts]
    h3 = c**3+9*c*c-c-1
    check(8*determinant(M0) == h3)
    for fp in fparts:
        check(fp.substitute(initial) == 0)
    # All parameters remain symbolic in the full characteristic polynomial.
    Q = [[2*j*M0[i][col]+jac[i][col] if col < 3 else jac[i][col]
          for col in range(8)] for i in range(3)]
    Q += [
        [0, F(1, 2), 0, j, 0, 0, 0, 0],
        [0, 0, F(1, 2), 0, j-1, 0, 0, 0],
        [F(-1, 2), 0, 0, 0, 0, j+2, 0, 0],
        [0, F(-1, 2), 0, 0, 0, 0, j+3, 0],
        [0, 0, F(-1, 2), 0, 0, 0, 0, j+4],
    ]
    BC = D*D*j*(j+2)-D*a*(j+1)/2+a*a/16
    VW = D*D*(j+3)*(j-1)-D*a*(j+1)/2+a*a/16
    AJ = (c+1)*j-a/4
    EJ = 2*c*j+D-a/2
    delta = AJ*(EJ*EJ-VW)-BC*EJ
    check(determinant(Q) == j*(j-1)*(j+2)*(j+3)*(j+4)*delta)
    check(delta.coeff("a", 3) == F(-1, 64))
    check(delta.coeff("j", 3) == h3)
    check(all(v.denominator == 1 for v in (64*delta).d.values()))
    # The chosen first jet is an exact eigenvector at the permitted resonance.
    FF = a*a-(4*c+20)*a+128*c-64
    nf = -24*H*a*(a-4*c+4)
    ng = 8*H*a*(a-4*c-4)
    first = [nf, ng, P(0), -ng/2, H*FF, nf/6, ng/8, P(0)]
    for row in Q:
        check(sum((P(val).substitute({"j": 1})*v for val, v in zip(row, first)), P()) == 0)
    check(nf+3*ng == -192*H*a)
    check(nf-ng == -32*H*a*(a-4*c+2))
    # Recompute the recurrence columns from direct signed Fourier products.
    fj, gj, kj = map(P, ("fj", "gj", "kj"))
    for n in range(2, 29):
        sub = initial | {
            "f": a+fj*z**n, "g": gj*z**n, "k": kj*z**n,
            "T": a/4-D-gj*z**n/(2*n), "S": -kj*z**n/(2*n-2),
            "J": a/4+fj*z**n/(2*n+4), "K": gj*z**n/(2*n+6),
            "L": kj*z**n/(2*n+8),
            "df": 2*n*fj*z**n, "dg": 2*n*gj*z**n, "dk": 2*n*kj*z**n,
        }
        mat = matrix_order(c, a, n)
        for row, mode in zip(mat, (1, 3, 5)):
            value = direct[mode].substitute(sub).coeff("z", n)
            check(value == row[0]*fj+row[1]*gj+row[2]*kj)
        check(determinant(mat) == delta.substitute({"j": n}))
    # Independent exact coefficient solving and residual reevaluation.
    examples = []
    order = 7
    for cv, av in ((F(2), F(7001, 7)), (F(3), F(7008, 7)), (F(4), F(7015, 7))):
        hv = F(1)
        dv = cv-1
        ff = av*av-(4*cv+20)*av+128*cv-64
        fs = [av]+[F(0)]*order
        gs = [F(0)]*(order+1)
        ks = [F(0)]*(order+1)
        fs[1] = -24*hv*av*(av-4*cv+4)/ff
        gs[1] = 8*hv*av*(av-4*cv-4)/ff

        def series():
            def pol(v):
                return sum((q*z**n for n, q in enumerate(v)), P())
            tt = P(av/4-dv)-sum((gs[n]*z**n/(2*n) for n in range(1, order+1)), P())
            ss = hv*z-sum((ks[n]*z**n/(2*n-2) for n in range(2, order+1)), P())
            jj = sum((fs[n]*z**n/(2*n+4) for n in range(order+1)), P())
            kk = sum((gs[n]*z**n/(2*n+6) for n in range(order+1)), P())
            ll = sum((ks[n]*z**n/(2*n+8) for n in range(order+1)), P())
            dots = [sum((2*n*q*z**n for n, q in enumerate(vals)), P()) for vals in (fs, gs, ks)]
            return projected(pol(fs), pol(gs), pol(ks), tt, ss, jj, kk, ll, *dots, cv)

        for n in range(2, order+1):
            residual = series()
            rhs = [-scalar(residual[mode].coeff("z", n)) for mode in (1, 3, 5)]
            answer = solve(matrix_order(cv, av, n), rhs)
            fs[n], gs[n], ks[n] = answer
            updated = series()
            for mode in (1, 3, 5):
                for h in range(n+1):
                    check(updated[mode].coeff("z", h) == 0)
        final = series()
        examples.append({
            "c": str(cv), "a": str(av), "H": str(hv),
            "f": list(map(str, fs)), "g": list(map(str, gs)), "k": list(map(str, ks)),
            "residual_unimposed_coefficients": {
                str(mode): {str(n): str(scalar(final[mode].coeff("z", n))) for n in range(1, order+1)}
                for mode in (7, 9, 11)
            },
        })
        check(fs[1]+3*gs[1] < 0)
        check(fs[1]-gs[1] < 0)
    before = json.loads((TOPIC / "verification/proof_before_code.json").read_text())
    check(hashlib.sha256((TOPIC / "PROOF.md").read_bytes()).hexdigest() == before["proof_sha256"])
    result = before | {
        "utc": datetime.now(timezone.utc).isoformat(), "status": "PASS",
        "checks": COUNT, "elapsed_seconds": time.monotonic()-started,
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "delta_times64_coefficients": {",".join(mon): str(v) for mon, v in sorted((64*delta).d.items())},
        "examples": examples,
        "scope": "Exact polynomial identities and finite Taylor checks supplement the standalone analytic proof. No full PDE solution or global projected connection is claimed.",
    }
    (TOPIC / "verification/CHECK.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: result[k] for k in ("utc", "status", "checks", "elapsed_seconds", "proof_sha256", "code_sha256")}))


if __name__ == "__main__":
    main()

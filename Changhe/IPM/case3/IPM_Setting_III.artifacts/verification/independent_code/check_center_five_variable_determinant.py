#!/usr/bin/env python3
"""Exact sparse-polynomial check, independent of the lead's SymPy code."""
from fractions import Fraction as F
from itertools import permutations
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import time
from check_local_two_projection_construction import P

ROOT = Path(__file__).resolve().parents[1]
TOPIC = ROOT / "research/two_projection_extension_audit/linearized_determinant"
COUNT = 0


def check(value):
    global COUNT
    COUNT += 1
    assert value, COUNT


def determinant(matrix):
    n = len(matrix)
    result = P()
    for perm in permutations(range(n)):
        sign = (-1)**sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
        term = P(sign)
        for i, col in enumerate(perm):
            term *= matrix[i][col]
        result += term
    return result


def main():
    started = time.monotonic()
    a, c, j = map(P, ("a", "c", "j"))
    D = c-1
    h = c*c+4*c-1
    names = ("f", "g", "T", "J", "K")
    f, g, T, J, K = map(P, names)
    S = P("S")
    F1 = (D+T)*f-f*f/4+f*g/2+(-J+2*K+4*S-2*T)*g
    F3 = (J+2*S)*f-f*f/4-f*g/2+D*g
    initial = {"f": a, "g": 0, "T": a/4-D, "J": a/4, "K": 0, "S": 0}
    L0 = [[q.derivative({name: 1}).substitute(initial) for name in names]
          for q in (F1, F3)]
    expected = [[-a/4, 2*D-a/4, a, 0, 0], [-a/4, D-a/2, 0, a, 0]]
    for row, target in zip(L0, expected):
        for value, answer in zip(row, target):
            check(value == answer)
    check(F1.substitute(initial) == 0)
    check(F3.substitute(initial) == 0)
    M = [[(c+1)/2, D/2], [D/2, c]]
    check(4*determinant(M) == h)
    # Polynomial matrix obtained by multiplying the first two characteristic
    # rows by 2M. Its determinant equals h det(jI-A).
    Q = [
        [2*j*M[0][0]+L0[0][0], 2*j*M[0][1]+L0[0][1], *L0[0][2:]],
        [2*j*M[1][0]+L0[1][0], 2*j*M[1][1]+L0[1][1], *L0[1][2:]],
        [0, F(1, 2), j, 0, 0],
        [F(-1, 2), 0, 0, j+2, 0],
        [0, F(-1, 2), 0, 0, j+3],
    ]
    I = a*a-4*((c+2)*(2*j)-D)*a+4*h*(2*j)**2-8*D*(c-3)*(2*j)
    check(16*determinant(Q) == j*(j+2)*(j+3)*I)
    # Separate construction: h times the first two rows of jI-A directly,
    # using M^-1 = (4/h) adj(M). Its determinant is h^2 det(jI-A).
    adj = [[M[1][1], -M[0][1]], [-M[1][0], M[0][0]]]
    QQ = [[h*j*(int(i == k))+2*sum((adj[i][l]*L0[l][k] for l in range(2)), P())
           for k in range(5)] for i in range(2)] + Q[2:]
    check(16*determinant(QQ) == h*j*(j+2)*(j+3)*I)
    for cv in (F(10001, 10000), F(3, 2), F(2), F(3), F(1001)):
        for av in (F(-19), F(0), F(10001, 10), F(1000001)):
            for jv in (F(0), F(-2), F(-3), F(1), F(7), F(41)):
                sub = {"c": cv, "a": av, "j": jv}
                qnum = [[p.substitute(sub) if isinstance(p, P) else P(p) for p in row] for row in Q]
                check(16*determinant(qnum) == (j*(j+2)*(j+3)*I).substitute(sub))
    before = json.loads((TOPIC / "verification/proof_before_code.json").read_text())
    check(hashlib.sha256((TOPIC / "PROOF.md").read_bytes()).hexdigest() == before["proof_sha256"])
    result = before | {
        "utc": datetime.now(timezone.utc).isoformat(),
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "checks": COUNT, "status": "PASS",
        "elapsed_seconds": time.monotonic()-started,
        "method": "Direct formal differentiation and two independent five-by-five determinant expansions with rational sparse polynomial arithmetic.",
    }
    (TOPIC / "verification/CHECK.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()

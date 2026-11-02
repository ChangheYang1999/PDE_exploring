"""Max-min mixture of the symmetric W/D/L game of a round-robin results file.

Usage: python3 tmp/rr_nash.py RESULTS.jsonl [SCENARIO] NAME=SUFFIX ...  (the first suffix that ends the spec names it;
SCENARIO is the scenario field, "none" for the standard start). Payoff of row i against column j: +1 if i wins
both seats, -1 if it loses both, else (wins - losses)/2 over the two seats. The LP solution is checked exactly
with fractions after rounding to small denominators.
"""
import json, sys
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog

path = sys.argv[1]
args = sys.argv[2:]
scen = None
if args and "=" not in args[0]:
    scen = None if args[0] == "none" else args[0]
    args = args[1:]
names = [a.split("=", 1)[0] for a in args]
sufs = [a.split("=", 1)[1] for a in args]

def name_of(spec):
    for n, s in zip(names, sufs):
        if spec.endswith(s):
            return n
    return None

n = len(names)
acc = {}
for line in open(path):
    d = json.loads(line)
    if d["scenario"] != scen:
        continue
    a, b = name_of(d["spec_a"]), name_of(d["spec_b"])
    if a is None or b is None:
        continue
    w = d["winner"]
    r = 0 if w not in (0, 1) else (1 if w == 0 else -1)
    acc.setdefault((a, b), []).append(r)
    acc.setdefault((b, a), []).append(-r)
M = [[Fraction(0)] * n for _ in range(n)]
for i, x in enumerate(names):
    for j, y in enumerate(names):
        if i != j:
            v = acc.get((x, y))
            if not v:
                sys.exit(f"missing pair {x} {y}")
            M[i][j] = Fraction(sum(v), len(v))
A = np.array([[float(v) for v in row] for row in M])
# maximise t subject to sum_i p_i A[i][j] >= t for all j, sum p = 1, p >= 0
c = np.zeros(n + 1); c[-1] = -1
A_ub = np.hstack([-A.T, np.ones((n, 1))])
res = linprog(c, A_ub=A_ub, b_ub=np.zeros(n), A_eq=[[1] * n + [0]], b_eq=[1],
              bounds=[(0, None)] * n + [(None, None)], method="highs")
p = [Fraction(x).limit_denominator(60) for x in res.x[:n]]
s = sum(p)
p = [x / s for x in p]
col = [sum(p[i] * M[i][j] for i in range(n)) for j in range(n)]
print("LP value", round(-res.fun, 6))
print("mixture", {names[i]: str(p[i]) for i in range(n) if p[i]})
print("exact column payoffs", {names[j]: str(col[j]) for j in range(n)})
print("min column payoff", min(col))
for i in range(n):
    print(f"{names[i]:>16}", " ".join(f"{str(M[i][j]):>5}" for j in range(n)))
# For each bot: the largest weight it can have in a mixture that is still max-min (all column payoffs >= value).
v = -res.fun
for k in range(n):
    ck = np.zeros(n); ck[k] = -1
    r = linprog(ck, A_ub=-A.T, b_ub=-np.full(n, v - 1e-9), A_eq=[[1] * n], b_eq=[1], bounds=[(0, None)] * n,
                method="highs")
    print(f"max weight of {names[k]} in a max-min mixture: {Fraction(-r.fun).limit_denominator(60)}")
for k in range(n):
    ck = np.zeros(n); ck[k] = 1
    r = linprog(ck, A_ub=-A.T, b_ub=-np.full(n, v - 1e-9), A_eq=[[1] * n], b_eq=[1], bounds=[(0, None)] * n,
                method="highs")
    print(f"min weight of {names[k]} in a max-min mixture: {Fraction(r.fun).limit_denominator(60)}")

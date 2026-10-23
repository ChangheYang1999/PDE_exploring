"""Independent exact certificate check. No producer elimination code is imported."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
from datetime import datetime, timezone
import hashlib
import json
import sympy as S

R = Path("research/degree13_grouped_moment_obstruction")
V = R / "verification"
cert = json.loads((V / "certificate.json").read_text())
checks = []


def check(name, passed, evidence=None):
    checks.append(dict(name=name, passed=bool(passed), evidence=evidence))


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def peval(a, x):
    v = 0
    for c in reversed(a):
        v = v * x + c
    return v


def specialize(terms, z, degree):
    a = [0] * (degree + 1)
    for (i, j), c in terms:
        a[i] += int(c) * z**j
    return a


def sylvester(a, b):
    m, n = len(a) - 1, len(b) - 1
    out = []
    for k in range(n):
        out.append([0] * k + a[::-1] + [0] * (n - 1 - k))
    for k in range(m):
        out.append([0] * k + b[::-1] + [0] * (m - 1 - k))
    return out


def bareiss(matrix):
    a = [row[:] for row in matrix]
    n, previous, sign, divisions = len(a), 1, 1, 0
    for k in range(n - 1):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return 0, divisions
        if pivot != k:
            a[pivot], a[k] = a[k], a[pivot]
            sign = -sign
        q = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * q - a[i][k] * a[k][j]
                value, remainder = divmod(numerator, previous)
                if remainder:
                    raise ArithmeticError("Bareiss division not exact")
                a[i][j] = value
                divisions += 1
            a[i][k] = 0
        previous = q
    return sign * a[-1][-1], divisions


def fraction_determinant(matrix):
    """Ordinary rational Gaussian elimination, separately from Bareiss."""
    a = [[F(x) for x in row] for row in matrix]
    result = F(1)
    for k in range(len(a)):
        pivot = next((i for i in range(k, len(a)) if a[i][k]), None)
        if pivot is None:
            return F(0)
        if pivot != k:
            a[pivot], a[k] = a[k], a[pivot]
            result = -result
        value = a[k][k]
        result *= value
        for j in range(k, len(a)):
            a[k][j] /= value
        for i in range(k + 1, len(a)):
            q = a[i][k]
            for j in range(k, len(a)):
                a[i][j] -= q * a[k][j]
    return result


s, t, h, j, z, v = S.symbols("s t h j z v")
PS = lambda a, b: [2, a, a*a - 2*b, a**3 - 3*a*b,
                   a**4 - 4*a*a*b + 2*b*b]
pu, pw = PS(s, t), PS(h, j)
moments = [1 + 4*pu[k] + 2*pw[k] for k in range(1, 5)]
H = -S.Rational(1, 2) - 2*s
J = S.Rational(3, 8) + s + 3*s*s - 2*t
sub = {h: H, j: J}
check("M1 reduction", S.expand(moments[0].subs(sub)) == 0)
check("M2 reduction", S.expand(moments[1].subs(sub)) == 0)
M3 = S.expand(moments[2].subs(sub))
expected = 24*s**3 + 9*s*s + S.Rational(9, 2)*s + S.Rational(15, 8) - (36*s + 6)*t
check("M3 exact identity", S.expand(M3 - expected) == 0)
check("exceptional divisor impossible", M3.subs(s, -S.Rational(1, 6)) == S.Rational(91, 72))
T = (64*s**3 + 24*s*s + 12*s + 5) / (16*(6*s+1))
check("T solves M3", S.cancel(M3.subs(t, T)) == 0)
pi = (v*v - s*v + t)*(v*v - h*v + j)
araw = S.diff(pi, v).subs(v, z).subs(sub).subs(t, T)
braw = (z*moments[3] + 13*t*j).subs(sub).subs(t, T)
ap = sum(S.Integer(c)*s**a*z**b for (a, b), c in cert["A"])
bp = sum(S.Integer(c)*s**a*z**b for (a, b), c in cert["B"])
check("A clearing identity", S.cancel(ap + 32*(6*s+1)*araw) == 0)
check("B clearing identity", S.cancel(bp + 64*(6*s+1)**2*braw) == 0)
check("A s degree", S.degree(ap, s) == 4)
check("A z degree", S.degree(ap, z) == 3)
check("B s degree", S.degree(bp, s) == 6)
check("B z degree", S.degree(bp, z) == 1)
check("determinant degree bound", 6*3 + 4*1 == 22)
for label, expression in [("A", ap), ("B", bp)]:
    poly = S.Poly(expression, s, z)
    check(label + " primitive", S.gcd_list(poly.coeffs()) == 1)
    check(label + " positive lexicographic leading coefficient", poly.LC() > 0)

rc = [int(x) for x in reversed(cert["R"])]
check("claimed R degree", len(rc) - 1 == 22 and rc[-1] != 0)
factors = [[int(x) for x in reversed(f["coefficients"])]
           for f in cert["factors"]]
check("exactly four factors", len(factors) == 4)
check("all multiplicities exactly1",
      [f["multiplicity"] for f in cert["factors"]] == [1, 1, 1, 1])
check("factor degrees in stated order",
      [len(f) - 1 for f in factors] == [3, 3, 6, 10])
product = [int(cert["constant_factor"])]
for f, fc in zip(cert["factors"], factors):
    for _ in range(f["multiplicity"]):
        product = mul(product, fc)
check("full factor product", product == rc)
check("constant factor", int(cert["constant_factor"]) == -35566624178176)
points = list(range(-11, 12))
check("23 distinct certificate points", len(set(points)) == 23)
for point in points + [12]:
    matrix = sylvester(specialize(cert["A"], point, 4),
                       specialize(cert["B"], point, 6))
    determinant, divisions = bareiss(matrix)
    check("Sylvester integer identity z=" + str(point),
          determinant == peval(rc, point),
          dict(z=point, determinant=str(determinant), exact_divisions=divisions))
for point in [F(0), F(1), F(15, 14)]:
    matrix = sylvester(specialize(cert["A"], point, 4),
                       specialize(cert["B"], point, 6))
    determinant = fraction_determinant(matrix)
    check("separate Gaussian identity z=" + str(point),
          determinant == peval(rc, point), str(determinant))

for k, fc in enumerate(factors[:3]):
    check("positive coefficient factor " + str(k), all(c > 0 for c in fc))
    check("factor upper endpoint " + str(k),
          peval(fc, F(15, 14)) == F(cert["factors"][k]["at_upper"]))

fc = factors[3]
qc = [0] * 11
for k, c in enumerate(fc):
    a = [comb(k, l)*15**l for l in range(k+1)]
    b = [comb(10-k, l)*14**l for l in range(11-k)]
    for l, x in enumerate(mul(a, b)):
        qc[l] += c*x
check("exact integer Mobius coefficients",
      qc == [int(x) for x in cert["degree10_positive_transform"]["coefficients_ascending"]])
for k, c in enumerate(qc):
    check("positive transform coefficient " + str(k), c > 0, str(c))
check("degree10 at1", peval(fc, F(1)) == 273273)
check("degree10 upper exact", peval(fc, F(15, 14)) == F(169230287405, 282475249))
check("degree10 upper positive", peval(fc, F(15, 14)) > 0)
q = S.symbols("q", positive=True)
mapz = (1+15*q)/(1+14*q)
check("Mobius map increasing", S.cancel(S.diff(mapz, q) - 1/(1+14*q)**2) == 0)
check("Mobius inverse", S.cancel((z-1)/(15-14*z)).subs(z, mapz).simplify() == q)
check("Mobius upper gap", S.cancel(S.Rational(15, 14)-mapz-1/(14*(1+14*q))) == 0)
n = S.symbols("n", positive=True)
zn = (13+2*n)/(12+2*n)
check("n lower endpoint", zn.subs(n, 1) == S.Rational(15, 14))
check("z decreases with n", S.cancel(S.diff(zn, n) + 2/(12+2*n)**2) == 0)
check("z strictly greater1 identity", S.cancel(zn-1-1/(12+2*n)) == 0)
for number, digest in [
    ("253", "0ecb179f081fbc490fdc36fb16f459ffe9a1aa0fa38976c43b406b97b23b79b9"),
    ("258", "dfff98196c5240b36b64c9f3a1ab8fdef3269cd6c7514dcc52b8d354b63b6566"),
    ("261", "3f8a8104118003a14a217d03a5f4b3bcaba38b61df8dbfb697c7f210948b1378"),
]:
    check("frozen dependency " + number,
          hashlib.sha256((V / f"dependency{number}.md").read_bytes()).hexdigest() == digest)
check("fixed reviewed proof",
      hashlib.sha256((R / "PROOF.md").read_bytes()).hexdigest()
      == "b435ff3df9591fa912a903420c4cd38e0f6a4a4fce955a056dfa40198afb5590")
check("fixed reviewed certificate",
      hashlib.sha256((V / "certificate.json").read_bytes()).hexdigest()
      == "9ffa448f6860d77d70813eadf9fa2ac244af56815a0d16bbe55cb29d86e744ea")

result = dict(status="PASS" if all(c["passed"] for c in checks) else "FAIL",
              count=len(checks), finished_utc=datetime.now(timezone.utc).isoformat(),
              checks=checks,
              proof_sha256=hashlib.sha256((R / "PROOF.md").read_bytes()).hexdigest(),
              certificate_sha256=hashlib.sha256((V / "certificate.json").read_bytes()).hexdigest(),
              driver_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              interpretation="Exact finite polynomial identity and positivity certificate; no full-plane endpoint.")
(V / "CHECKS.json").write_text(json.dumps(result, indent=2) + "\n")
print(result["status"], result["count"], flush=True)
for c in checks:
    if not c["passed"]:
        print("FAIL", c, flush=True)
if result["status"] != "PASS":
    raise SystemExit(1)

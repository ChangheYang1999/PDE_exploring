"""Independent check of c1-t4 T4-459 (H18 finite registry and whole-family coverage; TEAM_NOTE_v235), the parts
that c1-t4 asked c1-t2 to review: the finite composition (24 strict weak floors at 1/1000) and the scalar, original
graded and trans/statL radius ceilings.

Run from artifacts/:  python3 -B -u arith/review_t4_459.py
Takes no arguments. Needs python-flint (arb). Reads, read only, in place:
  ../../c1-t4/research/h18_coverage_audit/{PROOF.md, verification/result.json, data/coverage.json,
      data/families.json, code/check.py, source/results/NNN.json} (PROOF.md and result.json sha256 asserted as
      printed in TEAM_NOTE_v235; the others recorded),
  every *.json under ../../c1-t4/research outside h18_coverage_audit with the same byte size as a copied result
      (to locate the original of each copy by sha256),
  ../../c1-t4/research/transient_low_closure/PROOF.md (T4-051), .../source/T1_check_T4051.py,
  ../../c1-t4/research/stationary_resolvent_audit/PROOF.md (T4-059),
  ../reviews/REVIEW_T4_019.md, ../reviews/REVIEW_R1_004_GRADED.md, data/family_ceilings_exact_results.json.
Own code: the enclosure parser, the weak-floor arithmetic and the radius bounds are written here, not imported.
Output: stdout (logs/review_t4_459.log by the README command), data/review_t4_459_results.json.
Revision 2 (after c1-n4 N4-390): revision 1 displayed the root lower bounds and stored lower ends with %.12g and %.10g
of a float, so nine of the 24 root displays (004, 006, 010, 015, 017, 018, 021, 025, 026) rounded above the exact
rational bound, and the scalar ceilings with %.6e. All displays are now directed: lower bounds rounded down, upper
bounds rounded up, from the exact rationals (dfloor, dceil_sqrt); the exact rational root lower bound is stored as
root_lower_exact. No check, comparison or verdict changed.
"""
import hashlib
import json
import math
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

from flint import arb, ctx

if len(sys.argv) != 1:
    sys.exit("usage: review_t4_459.py (no arguments)")
t0 = time.time()
ctx.prec = 256
HERE = Path(__file__).resolve().parents[1]
LANE = HERE.parent
T4 = LANE.parent / "c1-t4"
AUD = T4 / "research/h18_coverage_audit"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
N_, FAILS = [0], []
OUT = {"inputs": {}}


def check(name, ok):
    N_[0] += 1
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILS.append(name)


def rel(p):
    return str(Path(p).relative_to(LANE.parent))


# ---------------------------------------------------------------- (A) inputs
PIN = {AUD / "PROOF.md": "353fc1575bccca1927be976d646b9ff886ee5fb87c99a090c8fce0c0b3d9f650",
       AUD / "verification/result.json": "3b433eb41a607839e3e4a9140fae9acaace1ed6ea46a50149d840d112c84d8c5",
       T4 / "research/transient_low_closure/PROOF.md": "85a6f3eecbf3388e9f793da5af1c536f9f0f2df39a28a1e6c0419ff89e88617a",
       T4 / "research/stationary_resolvent_audit/PROOF.md": "daa55c5868d689186fbe67b7afc5bea1f85b7bb27d82b97ef0830c8695e89d02",
       HERE / "data/family_ceilings_exact_results.json": "b1fea0a74af0a7729b38a27f1796deea0b3597b4ca9549ba235e9131af3b98a7"}
for p, h in PIN.items():
    OUT["inputs"][rel(p)] = sha(p)
    check("(A) sha256 of %s is %s...%s" % (rel(p), h[:8], h[-8:]), sha(p) == h)
for p in (AUD / "data/coverage.json", AUD / "data/families.json", AUD / "code/check.py",
          T4 / "research/transient_low_closure/source/T1_check_T4051.py", LANE / "reviews/REVIEW_T4_019.md",
          LANE / "reviews/REVIEW_R1_004_GRADED.md", T4 / "TEAM_NOTE_v235.md"):
    OUT["inputs"][rel(p)] = sha(p)
RES = json.loads((AUD / "verification/result.json").read_text())
COV = json.loads((AUD / "data/coverage.json").read_text())
FAM = json.loads((AUD / "data/families.json").read_text())
check("(A) T4-459 result.json reports 806 checks passed (TEAM_NOTE_v235)", RES["checks_passed"] == 806)
nums = [r["number"] for r in COV["rows"]]
check("(A) coverage.json lists the 24 snapshots 002 to 026 except 011", nums == [i for i in range(2, 27) if i != 11])


# ---------------------------------------------------------------- (B) the 24 weak floors
def encl(sv):
    """exact rational interval of an Arb string '[m +/- r]' or of an exact decimal or rational."""
    sv = str(sv).strip()
    if sv.startswith("["):
        body = sv[1:-1]
        if "+/-" in body:
            m, r = body.split("+/-")
            m, r = Fr(m.strip()), Fr(r.strip())
        else:
            m, r = Fr(body.strip()), Fr(0)
        assert r >= 0
        return m - r, m + r
    q = Fr(sv)
    return q, q


def absl(iv):
    lo, hi = iv
    return lo if lo > 0 else (-hi if hi < 0 else Fr(0))


def dfloor(x, n):
    """decimal string of x > 0 (a Fraction) rounded down to n significant digits"""
    e = math.floor(math.log10(float(x)))
    m = math.floor(x * Fr(10) ** (n - 1 - e))
    if m >= 10**n:
        m, e = m // 10, e + 1
    elif m < 10**(n - 1):
        e -= 1
        m = math.floor(x * Fr(10) ** (n - 1 - e))
    assert 10**(n - 1) <= m < 10**n and Fr(m) * Fr(10) ** (e - n + 1) <= x
    return "%s.%se%+03d" % (str(m)[0], str(m)[1:], e)


def dceil_sqrt(q, n):
    """decimal string of sqrt(q) (q > 0 a Fraction) rounded up to n significant digits"""
    e = math.floor(math.log10(math.sqrt(float(q))))
    for _ in range(3):
        t = q * Fr(10) ** (2 * (n - 1 - e))
        m = math.isqrt(t.numerator // t.denominator)
        while m * m < t:
            m += 1
        if m > 10**n:
            e += 1
        elif m < 10**(n - 1):
            e -= 1
        else:
            break
    assert m * m >= t and (m - 1)**2 < t and 10**(n - 1) <= m <= 10**n
    if m == 10**n:
        m, e = 10**(n - 1), e + 1
    return "%s.%se%+03d" % (str(m)[0], str(m)[1:], e)


def root_lower(I, D, H, bits=200):
    """a rational lower bound of the positive root m* of H m^2 + D m = I (I, D, H > 0), via 2^-bits floors."""
    S = 2**bits
    disc = (D * D + 4 * H * I) * S * S
    sq = math.isqrt(disc.numerator // disc.denominator)  # floor(sqrt(disc)) <= sqrt(disc)
    return (Fr(sq, S) - D) / (2 * H)


# originals: index c1-t4 json files outside the audit folder by size, hash only same-size files
sizes = {}
copies = {r["number"]: AUD / r["result"] for r in COV["rows"]}
want = {p.stat().st_size for p in copies.values()}
for p in (T4 / "research").rglob("*.json"):
    if AUD in p.parents:
        continue
    try:
        sz = p.stat().st_size
    except OSError:
        continue
    if sz in want:
        sizes.setdefault(sz, []).append(p)
FLOOR = Fr(1, 1000)
rows_out, mins = [], []
RESROWS = {r["number"]: r for r in RES["weak_candidates"]}
for r in COV["rows"]:
    n, p = r["number"], copies[r["number"]]
    hp = sha(p)
    check("(B) %03d: copied result sha256 equals coverage.json" % n, hp == r["result_sha256"])
    orig = [str(q.relative_to(T4)) for q in sizes.get(p.stat().st_size, []) if sha(q) == hp]
    check("(B) %03d: an identical original exists elsewhere in c1-t4/research (%s)" % (n, orig[0] if orig else "none"),
          len(orig) >= 1)
    d = json.loads(p.read_text())
    if "rows" in d:
        cand = [x for x in d["rows"] if x["k"] == r["probe_k"]]
        assert len(cand) == 1
        v = cand[0]
        I = absl(encl(v["pairing"]))
        D = encl(v["D"])[1]
        H = encl(v["gradient_sup_upper_ball"])[1]
        stored = encl(v["L2_radius_lower"])[0]
        kind = "localized probe k = %s" % r["probe_k"]
    else:
        I = absl(encl(d["pairing"]))
        if "D" in d:
            D = encl(d["D"])[1]
            if "M" in d and "C" in d:
                check("(B) %03d: D upper end >= M upper + C upper - 1e-90 (D is M + C)" % n,
                      D >= encl(d["M"])[1] + encl(d["C"])[1] - Fr(1, 10**90))
        else:
            D = encl(d["M"])[1] + encl(d["C"])[1]
        cert = d.get("sup_certificate", d.get("gradient_certificate"))
        H = Fr(cert["H_upper_exact"])
        stored = Fr(d["strict_lower_exact"]) if "strict_lower_exact" in d else encl(d["radius"])[0]
        kind = "angular probe"
    gap = I - D * FLOOR - H * FLOOR**2
    ml = root_lower(I, D, H)
    check("(B) %03d: I_lower - D_upper/1000 - H_upper/10^6 > 0 (own parser)" % n, I > 0 and D > 0 and H > 0 and gap > 0)
    mine = (str(I), str(D), str(H), str(gap))
    theirs = tuple(RESROWS[n][k] for k in ("I_lower_exact", "D_upper_exact", "H_upper_exact", "positive_gap_exact"))
    check("(B) %03d: I, D, H and the gap equal T4-459's exact values" % n, mine == theirs)
    # the stored distance is a lower end of the same root, so it must not exceed the root computed here (+ slack)
    check("(B) %03d: stored distance lower end %s <= own root lower bound %s (+1e-30) (both rounded down)"
          % (n, dfloor(stored, 10), dfloor(ml, 10)), stored <= ml + Fr(1, 10**30))
    mins.append((ml, n))
    rows_out.append({"number": n, "kind": kind, "I_lower": float(I), "D_upper": float(D), "H_upper": float(H),
                     "gap_at_1e-3": float(gap), "root_lower": dfloor(ml, 12), "root_lower_exact": str(ml),
                     "stored_lower": dfloor(stored, 12), "original": orig})
    print("    %03d (%s): root m* >= %s, stored lower end >= %s" % (n, kind, dfloor(ml, 10), dfloor(stored, 10)))
mn = min(mins)
check("(B) the least own root lower bound over the 24 is above %s (snapshot %03d), above 1/1000" % (dfloor(mn[0], 10), mn[1]),
      mn[0] > FLOOR)
OUT["B"] = {"display_rounding": "root_lower and stored_lower are rounded down to 12 significant digits from the exact "
                                "rationals; root_lower_exact is the exact rational lower bound of the root",
            "rows": rows_out, "least_root": [dfloor(mn[0], 12), mn[1]]}

# ---------------------------------------------------------------- (C) scalar ceilings
MINE = json.loads((HERE / "data/family_ceilings_exact_results.json").read_text())["ceilings"]
s019 = (LANE / "reviews/REVIEW_T4_019.md").read_text()
OUT["C"] = {}
COMMON = Fr(3793, 10**9)
for row in FAM["rows"]:
    mu, C, cU, sw = Fr(row["mu"]), Fr(row["C"]), Fr(row["cU"]), Fr(row["sqrtW2"])
    if row["name"] in MINE:
        m = MINE[row["name"]]
        check("(C) %s: tuple (mu, C, c_U, sqrt W2) equals c1-t2 family_ceilings_exact" % row["name"],
              (Fr(m["mu0"]), Fr(m["C"]), Fr(m["c_U"]), Fr(m["sqrt_W2"])) == (mu, C, cU, sw))
    else:
        check("(C) %s: tuple (1/4, 4800, 5, 512) matches REVIEW_T4_019 (G entry 1/4 after -(1/4)E^2, row sums below "
              "4800, A_s + B_s < 5, weights 128 and 512)" % row["name"],
              (mu, C, cU, sw) == (Fr(1, 4), 4800, 5, 512) and "G = [[1/4, -347/10, -5]" in s019
              and "are below 4800" in s019 and "4.5449 < 5" in s019 and "the outputs P, 128a, 512b" in s019)
    b2 = 4 * mu**3 / (27 * C * cU**2 * sw**2)
    # sup_s sqrt(s)(mu - C s) at s = mu/(3C): the cubic optimum
    s_ = mu / (3 * C)
    check("(C) %s: sqrt(s)(mu - C s) squared at s = mu/(3C) equals 4 mu^3/(27 C) exactly" % row["name"],
          s_ * (mu - C * s_)**2 == 4 * mu**3 / (27 * C))
    check("(C) %s: b^2 < (3793/10^9)^2" % row["name"], b2 < COMMON**2)
    OUT["C"][row["name"]] = dceil_sqrt(b2, 7)                  # rounded up: these are upper bounds

# ---------------------------------------------------------------- (D) original graded
sG = (LANE / "reviews/REVIEW_R1_004_GRADED.md").read_text()
check("(D) REVIEW_R1_004_GRADED: 'm2 = 1/2 - 4708 s - (A_s + B_s) nu with A_s + B_s = 217/50 + (1049/5) s'",
      "m2 = 1/2 - 4708 s - (A_s + B_s) nu with A_s + B_s = 217/50 + (1049/5) s (sympy)" in sG)
sm = Fr(1, 28248)
check("(D) max of sqrt(s)(1/2 - 4708 s) is at s = 1/28248, value squared 1/(9 * 28248)",
      Fr(1, 2) - 3 * 4708 * sm == 0 and sm * (Fr(1, 2) - 4708 * sm)**2 == Fr(1, 9 * 28248))
check("(D) 168^2 < 28248 and (50/217)(1/3)(1/168) = 25/54684 < 1/1000", 168**2 < 28248
      and Fr(50, 217) * Fr(1, 3) * Fr(1, 168) == Fr(25, 54684) and Fr(25, 54684) < FLOOR)
check("(D) (50/(651 sqrt 28248))^2 = 625/2992882662 (families.json)", Fr(2500, 651**2 * 28248) == Fr(FAM["graded_square_exact"]))

# ---------------------------------------------------------------- (E) trans / statL
s051 = (T4 / "research/transient_low_closure/PROOF.md").read_text()
s059 = (T4 / "research/stationary_resolvent_audit/PROOF.md").read_text()
s1c = (T4 / "research/transient_low_closure/source/T1_check_T4051.py").read_text()
Q051 = ["nu=R/sqrt(s),", "A_s=127/50+(653/5)s,  B_s=(9/5)(1+44s),", "m2=1/2-4708s-(A_s+B_s)nu,",
        "P <= (f2+k1 G1+2v1 f0)/m2+sqrt(40/m2)G1=:G2.", "X_s(h)<=sqrt(G2^2+2^14G1^2+2^18G0^2)",
        "b_s:=||J^s h||2 <= b+s a,"]
for q in Q051:
    check("(E) T4-051 PROOF.md quote '%s'" % q, q in s051)
check("(E) T4-059 (statL) needs m2 > 0: 'CONFIRMED under its stated positive alpha,m2'",
      "TP-1 is therefore CONFIRMED under its stated positive alpha,m2" in s059)
check("(E) T1_check_T4051.py asserts m2 > 0 at every statL row: 'assert pp[\"alpha\"] > 0 and pp[\"m2\"] > 0'",
      'assert pp["alpha"] > 0 and pp["m2"] > 0' in s1c)
# A_s + B_s = 217/50 + (1049/5) s as polynomials in s (compare at three points)
check("(E) A_s + B_s = 217/50 + (1049/5) s identically (T4-051 formulas)",
      all(Fr(127, 50) + Fr(653, 5) * t + Fr(9, 5) * (1 + 44 * t) == Fr(217, 50) + Fr(1049, 5) * t for t in (0, 1, 2)))
# registered instances satisfy m2 > 0 (consistency) and lie below the uniform X_s ceiling
inst = [("trans", arb(2)**(-17), arb(2)**(-14))] + [("statL n_s %d" % k, arb(1) / (k * k), arb(21) / 10**5)
                                                    for k in (225, 227, 228, 229)]
for lab, s_a, R_a in inst:
    m2 = arb(1) / 2 - 4708 * s_a - (arb(217) / 50 + arb(1049) / 5 * s_a) * R_a / s_a.sqrt()
    check("(E) %s: m2 = %s > 0 and R < 25/54684" % (lab, m2.str(6)), m2 > 0 and R_a < arb(25) / 54684)
check("(E) X_s >= 512 ||J^s h||_2 >= 512 ||h||_2, so ||h||_2 < 25/(54684 * 512) = %.6e < 3793/10^9"
      % float(Fr(25, 54684 * 512)), Fr(25, 54684 * 512) < COMMON and Fr(FAM["scalar_upper_exact"]) == COMMON)
OUT["E"] = {"trans_statL_L2_upper": str(Fr(25, 54684 * 512)), "graded_upper": "25/54684"}
OUT["checks"], OUT["fails"], OUT["elapsed_s"] = N_[0], FAILS, round(time.time() - t0, 3)
(HERE / "data/review_t4_459_results.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("checks: %d, failed: %d (%s); elapsed %.3f s" % (N_[0], len(FAILS), "; ".join(FAILS), OUT["elapsed_s"]))
sys.exit(1 if FAILS else 0)

"""N4 Cartesian reconstruction and exact Bernstein audit of T4's frozen probe."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from math import comb
import json
import sys
import time
from flint import fmpq as Q, fmpq_poly as Poly, arb, arb_poly, ctx

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "research/optimized_probe_audit"
NAME = "C1-N1-007-d2w-j7-e2bal"
sys.path.insert(0, str(ROOT / "research/projected_residual/code"))
from build import candidate_source, read_projection, destination
sys.path.insert(0, str(ROOT / "research/localized_weak_probe/code"))
from beta_scale import integral, ap, ar, Radial, U
from radial import T, pshift
sys.set_int_max_str_digits(0)


def digest(path):
    return sha256(Path(path).read_bytes()).hexdigest()


def put(out, ell, kind, n, P):
    if n == 0 and kind == "s":
        return
    if n < 0:
        n = -n
        if kind == "s":
            P = -P
    key = (ell, kind, n)
    out[key] = out.get(key, Poly([]))+P


def construct(model, P):
    B = U*P.derivative()-2*P
    X = T*B
    M, Cx, Cy = {}, {}, {}
    put(M, 0, "s", 1, (3*model.c+1)*P+2*model.c*X)
    for (j, n), V in model.u1.items():
        G = pshift(V, 2)*X/2
        put(M, j+1, "s", 2+n, G)
        put(M, j+1, "s", 2-n, G)
    for (j, n), V in model.u2.items():
        G = pshift(V, 2)
        put(M, j+1, "s", n, G*(P+X))
        put(M, j+1, "s", n+2, -G*X/2)
        put(M, j+1, "s", n-2, -G*X/2)
    for (j, n), V in model.rx.items():
        G = pshift(V, 2)*P/2
        put(Cx, j+1, "c", n-1, G)
        put(Cx, j+1, "c", n+1, -G)
    for (j, n), V in model.ry.items():
        G = pshift(V, 2)*P/2
        put(Cy, j+1, "s", 1+n, G)
        put(Cy, j+1, "s", 1-n, G)
    return [{k: v for k, v in Z.items() if v} for Z in [M, Cx, Cy]]


def energy(fields, delta):
    totals = {}
    pairs = 0
    for field in fields:
        bymode = {}
        for (ell, kind, n), P in field.items():
            assert n > 0 and n % 2 == 1
            bymode.setdefault((kind, n), []).append((ell, ap(P(U))))
        for rows in bymode.values():
            for i, (ell, P) in enumerate(rows):
                for j in range(i, len(rows)):
                    ell2, P2 = rows[j]
                    key = ell+ell2
                    totals[key] = totals.get(key, arb_poly([]))+P*P2*(1 if i == j else 2)
                    pairs += 1
    result = arb.pi()/2*sum((integral(P, 1+ell*delta/2, 1)
                            for ell, P in totals.items()), arb(0))
    assert result > 0 and result.rel_accuracy_bits() > 150
    return result, pairs


def evaluate(field, model, x, y):
    from flint import acb
    r2 = x*x+y*y
    r = r2.sqrt()
    v = 1/(1+r2)
    t = r2/(1+r2)
    z = acb(x/r, y/r)
    powers = [acb(1)]
    for _ in range(max(n for ell, kind, n in field)):
        powers.append(powers[-1]*z)
    result = arb(0)
    for (ell, kind, n), P in field.items():
        tr = powers[n].real if kind == "c" else powers[n].imag
        result += v**ar(ell*model.delta/2)*ap(P)(t)*tr
    return r*v*v*result


def bernstein(P):
    n = max(P.degree(), 0)
    return [sum((P[j]*Q(comb(k, j), comb(n, j)) for j in range(k+1)), Q(0))
            for k in range(n+1)]


def halves(values):
    triangle = list(values)
    left, right = [triangle[0]], [triangle[-1]]
    while len(triangle) > 1:
        triangle = [(a+b)/2 for a, b in zip(triangle[:-1], triangle[1:])]
        left.append(triangle[0])
        right.append(triangle[-1])
    return left, right[::-1]


def bound_gradient(P, target):
    # Exact degree-independent Bernstein conversion and subdivision fixtures.
    assert bernstein(Poly([3])) == [Q(3)]
    assert bernstein(Poly([0, 1])) == [Q(0), Q(1)]
    assert bernstein(Poly([0, 0, 1])) == [Q(0), Q(0), Q(1)]
    assert halves([Q(0), Q(0), Q(1)]) == (
        [Q(0), Q(0), Q(1, 4)], [Q(1, 4), Q(1, 2), Q(1)])
    radial = (1-4*T)*P+2*T*U*P.derivative()
    root = [bernstein(U*U*Z) for Z in [P, radial]]
    pending = [(Q(0), Q(1), root)]
    leaves = []
    while pending:
        lo, hi, controls = pending.pop()
        upper = max(abs(c) for cs in controls for c in cs)
        if upper < target:
            leaves.append({"left": str(lo), "right": str(hi),
                           "exact_upper": str(upper)})
        else:
            assert hi-lo > Q(1, 2**32)
            mid = (lo+hi)/2
            lr = [halves(cs) for cs in controls]
            pending.append((mid, hi, [h[1] for h in lr]))
            pending.append((lo, mid, [h[0] for h in lr]))
        assert len(leaves)+len(pending) < 100000
    leaves.sort(key=lambda leaf: Q(leaf["left"]))
    assert Q(leaves[0]["left"]) == 0 and Q(leaves[-1]["right"]) == 1
    assert all(Q(a["right"]) == Q(b["left"]) for a, b in zip(leaves[:-1], leaves[1:]))
    assert all(Q(leaf["exact_upper"]) < target for leaf in leaves)
    return leaves


def main():
    start = time.monotonic()
    ctx.prec = 2048
    peerpath = BASE/"source/T4_a0.json"
    peer = json.loads(peerpath.read_text())
    assert digest(peerpath) == "b5b510bbabe556d2e07008473d9d92eb7098bac38cc36955cac0799bd0de425e"
    src = candidate_source(NAME)
    assert peer["input_sha256"] == digest(src)
    assert Q(peer["a"]) == 0 and Q(peer["C_U_exact"]) == 1
    P = Poly([])
    for k, v in peer["probe_coefficients"].items():
        P += Q(v)*T**int(k)
    H = Q(peer["H_upper_exact"])
    leaves = bound_gradient(P, H)
    print("Bernstein cover", len(leaves), "seconds", time.monotonic()-start, flush=True)
    model = Radial(src)
    Mfield, Cx, Cy = construct(model, P)
    print("constructed", [len(f) for f in [Mfield, Cx, Cy]],
          "seconds", time.monotonic()-start, flush=True)
    pointchecks = []
    for xs, ys in [("1/2", "1/2"), ("3", "4"), ("6", "8")]:
        x, y = ar(Q(xs)), ar(Q(ys))
        vals = model.evaluate(xs, ys)
        r2 = x*x+y*y
        v, t = 1/(1+r2), r2/(1+r2)
        value, derivative = ap(P)(t), ap(P.derivative())(t)
        B = v*derivative-2*value
        phi = y*v*v*value
        px = 2*x*y*v**3*B
        py = v*v*value+2*y*y*v**3*B
        expected = [(2*ar(model.c)+1)*phi+(ar(model.c)*x+vals["u1"])*px
                    +(ar(model.c)*y+vals["u2"])*py,
                    phi*vals["rho_x"], phi*vals["rho_y"]]
        comparisons = [bool(evaluate(f, model, x, y).overlaps(value))
                       for f, value in zip([Mfield, Cx, Cy], expected)]
        assert all(comparisons)
        pointchecks.append({"x": xs, "y": ys, "M_Cx_Cy_overlap": comparisons})
    M2, mpairs = energy([Mfield], model.delta)
    C2, cpairs = energy([Cx, Cy], model.delta)
    projected, metadata = read_projection(NAME)
    pairing = arb.pi()/2*sum((integral(ap((F*P)(U)), ell*model.delta/2-1, 1)
                              for ell, F in projected.items()), arb(0))
    assert pairing.rel_accuracy_bits() > 150
    M, C = M2.sqrt(), C2.sqrt()
    comparisons = {key: bool(value.overlaps(arb(peer[key])))
                   for key, value in [("pairing", pairing), ("M", M), ("C", C)]}
    assert all(comparisons.values()), comparisons
    radius = 2*abs(pairing)/(M+C+((M+C)**2+4*ar(H)*abs(pairing)).sqrt())
    floor = Q(peer["strict_lower_exact"])
    assert radius > ar(floor) and radius.overlaps(arb(peer["radius"]))
    opuspath = BASE/"source/T1_check.json"
    opus = json.loads(opuspath.read_text())
    opuschecks = {key: bool(value.overlaps(arb(opus[key])))
                 for key, value in [("pairing", pairing), ("M", M), ("C", C),
                                    ("radius", radius)]}
    assert all(opuschecks.values())
    paths = [src, destination(NAME), peerpath, opuspath, Path(__file__), BASE/"PROOF.md",
             BASE/"source/MANIFEST.json", ROOT/"research/radial_fourier/code/radial.py",
             ROOT/"research/projected_residual/code/build.py",
             ROOT/"research/localized_weak_probe/code/beta_scale.py",
             ROOT/"research/localized_weak_probe/code/evaluate.py"]
    out = {
        "utc": datetime.now(timezone.utc).isoformat(), "candidate": NAME,
        "bits": ctx.prec, "method": "Cartesian products, full angular norms, exact Bernstein H",
        "inputs": {str(p.relative_to(ROOT)): digest(p) for p in paths},
        "pairing": pairing.str(100), "M": M.str(100), "C": C.str(100),
        "H_upper_exact": str(H), "H_cover": leaves, "H_cover_tiles_unit_interval": True,
        "H_cover_max_exact": str(max(Q(leaf["exact_upper"]) for leaf in leaves)),
        "point_checks": pointchecks, "M_radial_pairs": mpairs, "C_radial_pairs": cpairs,
        "T4_comparisons": comparisons, "Opus_R1_021_comparisons": opuschecks,
        "radius": radius.str(100), "strict_lower_exact": str(floor),
        "strict_floor_verified": True, "elapsed_seconds": time.monotonic()-start,
        "status": "CONFIRMED conditional fixed-c L2 correction-distance certificate",
    }
    with (BASE/"verification/candidate007.json").open("x") as f:
        json.dump(out, f, indent=2)
        f.write("\n")
    print("DONE", out["elapsed_seconds"], "radius", out["radius"], flush=True)


if __name__ == "__main__":
    main()

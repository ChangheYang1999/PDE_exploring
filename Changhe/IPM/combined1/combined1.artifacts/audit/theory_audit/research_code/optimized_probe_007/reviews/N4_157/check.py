"""Independent Cartesian and Bernstein reproduction of the frozen mode7 probe."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import importlib.util
import json
import sys
import time
from flint import fmpq as Q, fmpq_poly as Poly, arb, ctx, acb

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT/"research/angular_probe_audit"
NAME = "C1-N1-007-d2w-j7-e2bal"
HELPER = ROOT/"research/optimized_probe_audit/code/check.py"
spec = importlib.util.spec_from_file_location("n4_first_mode_helpers", HELPER)
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
put, energy, evaluate = helper.put, helper.energy, helper.evaluate
bernstein, halves = helper.bernstein, helper.halves
T, U, ap, ar, pshift = helper.T, helper.U, helper.ap, helper.ar, helper.pshift
Radial, integral = helper.Radial, helper.integral
sys.path.insert(0, str(ROOT/"research/whole_plane_norms/code"))
from pipeline import load, source, DATA
sys.set_int_max_str_digits(0)


def digest(path):
    h = sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def construct(model, P, n):
    radial = (1-4*T)*P+2*T*U*P.derivative()
    px = [(n+1, (radial-n*P)/2), (n-1, (radial+n*P)/2)]
    py = [(n-1, (radial+n*P)/2), (n+1, (n*P-radial)/2)]
    M, Cx, Cy = {}, {}, {}
    put(M, 0, "s", n, (2*model.c+1)*P+model.c*radial)
    for (j, l), V in model.u1.items():
        for freq, W in px:
            G = pshift(V, 2)*W/2
            put(M, j+1, "s", freq+l, G)
            put(M, j+1, "s", freq-l, G)
    for (j, l), V in model.u2.items():
        for freq, W in py:
            G = pshift(V, 2)*W/2
            put(M, j+1, "s", l+freq, G)
            put(M, j+1, "s", l-freq, G)
    for (j, l), V in model.rx.items():
        G = pshift(V, 2)*P/2
        put(Cx, j+1, "c", n-l, G)
        put(Cx, j+1, "c", n+l, -G)
    for (j, l), V in model.ry.items():
        G = pshift(V, 2)*P/2
        put(Cy, j+1, "s", n+l, G)
        put(Cy, j+1, "s", n-l, G)
    return [{key: value for key, value in field.items() if value}
            for field in [M, Cx, Cy]]


def gradient_cover(P, n, target):
    assert bernstein(Poly([3])) == [Q(3)]
    assert halves([Q(0), Q(0), Q(1)]) == (
        [Q(0), Q(0), Q(1, 4)], [Q(1, 4), Q(1, 2), Q(1)])
    radial = (1-4*T)*P+2*T*U*P.derivative()
    pending = [(Q(0), Q(1), [bernstein(U*U*Z) for Z in [n*P, radial]])]
    leaves = []
    while pending:
        lo, hi, controls = pending.pop()
        upper = max(abs(x) for cs in controls for x in cs)
        if upper < target:
            leaves.append({"left": str(lo), "right": str(hi),
                           "exact_upper": str(upper)})
        else:
            assert hi-lo > Q(1, 2**32)
            mid = (lo+hi)/2
            lr = [halves(cs) for cs in controls]
            pending.extend([(mid, hi, [z[1] for z in lr]),
                            (lo, mid, [z[0] for z in lr])])
        assert len(leaves)+len(pending) < 100000
    leaves.sort(key=lambda leaf: Q(leaf["left"]))
    assert Q(leaves[0]["left"]) == 0 and Q(leaves[-1]["right"]) == 1
    assert all(Q(a["right"]) == Q(b["left"]) for a, b in zip(leaves[:-1], leaves[1:]))
    assert all(Q(leaf["exact_upper"]) < target for leaf in leaves)
    return leaves


def main():
    start = time.monotonic()
    ctx.prec = 2048
    peerpath = BASE/"source/T4_n7_a0.json"
    assert digest(peerpath) == "2a268c62e9e45096d2b745679a49adeee0cb9a3da532a06e4b89faaffdb3ef1f"
    peer = json.loads(peerpath.read_text())
    n = peer["angular_mode"]
    assert n == 7 and Q(peer["a"]) == 0 and Q(peer["C_U_exact"]) == 1
    src = source(NAME)
    cache = DATA/f"{NAME}_D0.json.gz"
    ass_path = ROOT/f"research/whole_plane_norms/verification/{NAME}_assembly.json"
    assembly = json.loads(ass_path.read_text())
    assert peer["input_sha256"] == digest(src) == assembly["source_sha256"]
    assert digest(cache) == assembly["polynomial_sha256"]
    P = Poly([])
    for k, value in peer["probe_coefficients"].items():
        assert int(k) >= (n-1)//2
        P += Q(value)*T**int(k)
    assert not any(P[k] for k in range((n-1)//2))
    H = Q(peer["H_upper_exact"])
    leaves = gradient_cover(P, n, H)
    print("Bernstein cover", len(leaves), "seconds", time.monotonic()-start, flush=True)
    model = Radial(src)
    calibration = Poly([1, 1])
    assert construct(model, calibration, 1) == helper.construct(model, calibration)
    fields = construct(model, P, n)
    print("constructed", [len(f) for f in fields], time.monotonic()-start, flush=True)
    pointchecks = []
    for xs, ys in [("1/2", "1/2"), ("3", "4"), ("6", "8")]:
        x, y = ar(Q(xs)), ar(Q(ys))
        vals = model.evaluate(xs, ys)
        r2 = x*x+y*y
        r = r2.sqrt()
        v, t = 1/(1+r2), r2/(1+r2)
        z = acb(x/r, y/r)**n
        value = ap(P)(t)
        radial = (1-4*t)*value+2*t*v*ap(P.derivative())(t)
        pr, pt = v*v*radial*z.imag, n*v*v*value*z.real
        px, py = x/r*pr-y/r*pt, y/r*pr+x/r*pt
        phi = r*v*v*value*z.imag
        expected = [(2*ar(model.c)+1)*phi
                    +(ar(model.c)*x+vals["u1"])*px
                    +(ar(model.c)*y+vals["u2"])*py,
                    phi*vals["rho_x"], phi*vals["rho_y"]]
        checks = [evaluate(f, model, x, y).overlaps(e)
                  for f, e in zip(fields, expected)]
        assert all(checks), (xs, ys, checks)
        pointchecks.append({"x": xs, "y": ys, "M_Cx_Cy_overlap": checks})
    M2, mpairs = energy(fields[:1], model.delta)
    C2, cpairs = energy(fields[1:], model.delta)
    print("energies complete", time.monotonic()-start, flush=True)
    raw = load(NAME, 0)[0, 0]
    assert sorted({freq for ell, kind, freq in raw}) == list(range(1, 320, 2))
    terms = [(ell, poly) for (ell, kind, freq), poly in raw.items()
             if kind == "s" and freq == n]
    assert terms
    pairing = arb.pi()/2*sum(
        (integral(ap((poly*P)(U)), ell*model.delta/2-1, 1)
         for ell, poly in terms), arb(0))
    assert pairing.rel_accuracy_bits() > 150
    M, C = M2.sqrt(), C2.sqrt()
    comparisons = {key: value.overlaps(arb(peer[key]))
                   for key, value in [("pairing", pairing), ("M", M), ("C", C)]}
    assert all(comparisons.values()), comparisons
    radius = 2*abs(pairing)/(M+C+((M+C)**2+4*ar(H)*abs(pairing)).sqrt())
    floor = Q(peer["strict_lower_exact"])
    assert radius > ar(floor) and radius.overlaps(arb(peer["radius"]))
    paths = [src, cache, ass_path, peerpath, Path(__file__), BASE/"PROOF.md",
             BASE/"source/MANIFEST.json", HELPER,
             ROOT/"research/radial_fourier/code/radial.py",
             ROOT/"research/whole_plane_norms/code/pipeline.py",
             ROOT/"research/localized_weak_probe/code/beta_scale.py",
             ROOT/"research/localized_weak_probe/code/evaluate.py"]
    out = {
        "utc": datetime.now(timezone.utc).isoformat(), "candidate": NAME,
        "angular_mode": n, "bits": ctx.prec,
        "method": "Cartesian field products, complete mode7 residual, exact Bernstein H",
        "inputs": {str(p.relative_to(ROOT)): digest(p) for p in paths},
        "pairing": pairing.str(100), "M": M.str(100), "C": C.str(100),
        "H_upper_exact": str(H), "H_cover": leaves,
        "H_cover_tiles_unit_interval": True,
        "H_cover_max_exact": str(max(Q(leaf["exact_upper"]) for leaf in leaves)),
        "point_checks": pointchecks, "M_radial_pairs": mpairs, "C_radial_pairs": cpairs,
        "n1_exact_field_specialization": True,
        "residual_mode7_components": len(terms), "T4_comparisons": comparisons,
        "radius": radius.str(100), "strict_lower_exact": str(floor),
        "strict_floor_verified": True, "elapsed_seconds": time.monotonic()-start,
        "status": "CONFIRMED conditional fixed-c L2 correction-distance certificate",
    }
    with (BASE/"verification/candidate007_n7.json").open("x") as f:
        json.dump(out, f, indent=2)
        f.write("\n")
    print("DONE", out["elapsed_seconds"], "radius", out["radius"], flush=True)


if __name__ == "__main__":
    main()

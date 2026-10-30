"""Two independent whole-plane pairings for frozen rational weak probes."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import argparse
import importlib.util
import json
import sys
import time
from flint import fmpq as Q, fmpq_poly as Poly, arb, arb_poly, acb, ctx

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "research/successor_weak_probes"
HELPER = ROOT / "research/angular_probe_audit/code/check.py"
spec = importlib.util.spec_from_file_location("n4_angular_helpers", HELPER)
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
T, U, ap, ar = helper.T, helper.U, helper.ap, helper.ar
Radial, pshift, integral = helper.Radial, helper.pshift, helper.integral
sys.set_int_max_str_digits(0)

PROBES = {
    1: ("research/optimized_probe_audit/source/T4_a0.json",
        "b5b510bbabe556d2e07008473d9d92eb7098bac38cc36955cac0799bd0de425e",
        "research/optimized_probe_audit/verification/candidate007.json"),
    7: ("research/angular_probe_audit/source/T4_n7_a0.json",
        "2a268c62e9e45096d2b745679a49adeee0cb9a3da532a06e4b89faaffdb3ef1f",
        "research/angular_probe_audit/verification/candidate007_n7.json"),
}


def digest(path):
    h = sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def poly_hash(items):
    """Unambiguous canonical hash without storing a large new coefficient file."""
    h = sha256()
    for key, P in sorted(items.items()):
        record = [key, [str(z) for z in P.numer()], str(P.denom())]
        h.update((json.dumps(record, separators=(",", ":")) + "\n").encode())
    return h.hexdigest()


def add(out, key, value):
    if value:
        out[key] = out.get(key, Poly([])) + value


def project(model, target):
    """Build one exact residual frequency directly from Cartesian derivatives."""
    result = {}
    for (j, n), P in model.rho.items():
        if n == target:
            TP = T * P.derivative()
            L = model.c * (2*TP - 3*P + 2*T*(model.p[j]*P - TP)) - P
            add(result, j+1, pshift(L, 2))
    quadratic = {}
    counts = []
    for C, S in [(model.u1, model.rx), (model.ry, model.u2)]:
        count = 0
        for (i, n), P in C.items():
            for (j, m), W in S.items():
                twice = (int(m+n == target) + int(m-n == target)
                         - int(m-n == -target))
                if twice:
                    add(quadratic, i+j+2, P*W*Q(twice, 2))
                    count += 1
        counts.append(count)
    for ell, P in quadratic.items():
        add(result, ell, pshift(P, 4))
    return {ell: P for ell, P in result.items() if P}, counts


def pairing_direct(model, projection, P):
    return arb.pi()/2 * sum(
        (integral(ap((A*P)(U)), ell*model.delta/2-1, 1)
         for ell, A in projection.items()), arb(0))


def pairing_parts(model, Mfield):
    """Integrate -rho Mfield. No residual or density gradient is assembled here."""
    rho = {}
    for (j, n), P in model.rho.items():
        rho.setdefault(n, []).append((j+1, ap(pshift(P, 2)(U))))
    products = {}
    pairs = 0
    for (ell, kind, n), P in Mfield.items():
        assert kind == "s"
        W = ap(P(U))
        for ell2, R in rho.get(n, []):
            key = ell+ell2
            products[key] = products.get(key, arb_poly([])) + R*W
            pairs += 1
    answer = -arb.pi()/2 * sum(
        (integral(P, ell*model.delta/2-1, 1)
         for ell, P in products.items()), arb(0))
    return answer, pairs


def point_checks(model, P, n, fields):
    checks = []
    for xs, ys in [("1/2", "1/2"), ("3", "4"), ("6", "8")]:
        x, y = ar(Q(xs)), ar(Q(ys))
        vals = model.evaluate(xs, ys)
        r2 = x*x+y*y
        r = r2.sqrt()
        v, t = 1/(1+r2), r2/(1+r2)
        z = acb(x/r, y/r)**n
        value = ap(P)(t)
        radial = (1-4*t)*value + 2*t*v*ap(P.derivative())(t)
        pr, pt = v*v*radial*z.imag, n*v*v*value*z.real
        px, py = x/r*pr-y/r*pt, y/r*pr+x/r*pt
        phi = r*v*v*value*z.imag
        expected = [
            (2*ar(model.c)+1)*phi
            + (ar(model.c)*x+vals["u1"])*px
            + (ar(model.c)*y+vals["u2"])*py,
            phi*vals["rho_x"], phi*vals["rho_y"],
        ]
        overlap = [helper.evaluate(f, model, x, y).overlaps(e)
                   for f, e in zip(fields, expected)]
        assert all(overlap), (xs, ys, overlap)
        checks.append({"x": xs, "y": ys, "M_Cx_Cy_overlap": overlap})
    return checks


def strict_floor(value):
    # Binary64 only proposes a rational; the rigorous Arb inequality decides.
    proposal = Q(int(float(value)*10**12)-1, 10**12)
    assert proposal > 0 and value > ar(proposal)
    return proposal


def run(name, modes, bits):
    start = time.monotonic()
    ctx.prec = bits
    src = ROOT/f"research/candidate_audits/data/{name}/canonical.json"
    audit_path = ROOT/f"research/candidate_audits/verification/{name}.json"
    audit = json.loads(audit_path.read_text())
    src_sha = digest(src)
    assert audit["canonical_sha256"] == src_sha
    assert audit["all_forbidden_zero"] and audit["snapshot_hashes_confirmed"]
    model = Radial(src)
    assert model.state["source_sha256"] == audit["generator_sha256"]
    assert model.c > 1
    print("prepared", name, "seconds", time.monotonic()-start, flush=True)
    for n in modes:
        tick = time.monotonic()
        dest = BASE/f"verification/{name}_n{n}.json"
        assert not dest.exists(), dest
        probe_rel, probe_sha, calibration_rel = PROBES[n]
        probe_path = ROOT/probe_rel
        assert digest(probe_path) == probe_sha
        frozen = json.loads(probe_path.read_text())
        assert Q(frozen["a"]) == 0 and Q(frozen["C_U_exact"]) == 1
        P = Poly([])
        for k, value in frozen["probe_coefficients"].items():
            assert int(k) >= (n-1)//2
            P += Q(value)*T**int(k)
        assert not any(P[k] for k in range((n-1)//2))
        H = Q(frozen["H_upper_exact"])
        cover = helper.gradient_cover(P, n, H)
        fields = helper.construct(model, P, n)
        if n == 1:
            assert fields == helper.helper.construct(model, P)
        print("constructed n", n, [len(f) for f in fields],
              "seconds", time.monotonic()-tick, flush=True)
        points = point_checks(model, P, n, fields)
        Iparts, parts_pairs = pairing_parts(model, fields[0])
        projection, projection_pairs = project(model, n)
        Idirect = pairing_direct(model, projection, P)
        assert Idirect.rel_accuracy_bits() > 150
        assert Iparts.rel_accuracy_bits() > 150
        assert Idirect.overlaps(Iparts), (n, Idirect, Iparts)
        print("pairings agree", n, Idirect.str(20),
              "seconds", time.monotonic()-tick, flush=True)
        M2, mpairs = helper.energy(fields[:1], model.delta)
        C2, cpairs = helper.energy(fields[1:], model.delta)
        M, C = M2.sqrt(), C2.sqrt()
        radius = 2*abs(Idirect)/(M+C+((M+C)**2+4*ar(H)*abs(Idirect)).sqrt())
        newton = abs(Idirect)/(M+C)
        floor, newton_floor = strict_floor(radius), strict_floor(newton)
        calibration = {}
        if name.startswith("C1-N1-007-"):
            previous = json.loads((ROOT/calibration_rel).read_text())
            calibration = {
                key: value.overlaps(arb(previous[key]))
                for key, value in [("pairing", Idirect), ("M", M),
                                   ("C", C), ("radius", radius)]
            }
            calibration["parts_pairing"] = Iparts.overlaps(arb(previous["pairing"]))
            assert all(calibration.values()), calibration
        paths = [src, audit_path, probe_path, Path(__file__), BASE/"PROOF.md",
                 HELPER, ROOT/"research/optimized_probe_audit/code/check.py",
                 ROOT/"research/radial_fourier/code/radial.py",
                 ROOT/"research/localized_weak_probe/code/beta_scale.py",
                 ROOT/"research/localized_weak_probe/code/evaluate.py"]
        if calibration:
            paths.append(ROOT/calibration_rel)
        result = {
            "utc": datetime.now(timezone.utc).isoformat(),
            "candidate": name, "angular_mode": n, "bits": ctx.prec,
            "method": "Cartesian weak fields; direct residual projection and integration by parts; complete beta moments",
            "inputs": {str(p.relative_to(ROOT)): digest(p) for p in paths},
            "generator_sha256": model.state["source_sha256"],
            "canonical_sha256": src_sha, "c_exact": str(model.c),
            "pairing": Idirect.str(100), "pairing_parts": Iparts.str(100),
            "pairing_paths_overlap": True,
            "pairing_accuracy_bits": [Idirect.rel_accuracy_bits(), Iparts.rel_accuracy_bits()],
            "M": M.str(100), "C": C.str(100),
            "H_upper_exact": str(H), "H_cover": cover,
            "H_cover_tiles_unit_interval": True,
            "H_cover_max_exact": str(max(Q(z["exact_upper"]) for z in cover)),
            "point_checks": points,
            "projection_radial_branches": len(projection),
            "projection_pairs": projection_pairs,
            "projection_sha256": poly_hash(projection),
            "parts_radial_pairs": parts_pairs,
            "field_counts": [len(f) for f in fields],
            "field_sha256": [poly_hash(f) for f in fields],
            "M_radial_pairs": mpairs, "C_radial_pairs": cpairs,
            "radius": radius.str(100), "strict_lower_exact": str(floor),
            "newton_radius": newton.str(100),
            "newton_strict_lower_exact": str(newton_floor),
            "strict_floors_verified": True,
            "candidate007_calibration": calibration,
            "elapsed_seconds": time.monotonic()-tick,
            "candidate_elapsed_seconds": time.monotonic()-start,
            "status": "OPEN independent peer reproduction of successor result",
        }
        dest.parent.mkdir(parents=True, exist_ok=True)
        with dest.open("x") as out:
            json.dump(result, out, indent=2)
            out.write("\n")
        print("DONE", name, "n", n, "radius", radius.str(22),
              "floor", str(floor), "seconds", result["elapsed_seconds"], flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate", nargs="+")
    parser.add_argument("--modes", type=int, nargs="+", default=[7, 1])
    parser.add_argument("--bits", type=int, default=2048)
    args = parser.parse_args()
    assert all(n in PROBES for n in args.modes)
    assert args.bits >= 1024
    for name in args.candidate:
        run(name, args.modes, args.bits)

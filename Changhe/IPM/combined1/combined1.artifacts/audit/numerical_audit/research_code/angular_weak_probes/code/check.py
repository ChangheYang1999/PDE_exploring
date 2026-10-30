"""Complete-plane higher angular weak tests with rigorous radial bounds."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import argparse
import json
import sys
import time
from flint import arb, arb_poly, fmpq as Q, ctx

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "research/angular_weak_probes"
NAME = "C1-N1-007-d2w-j7-e2bal"
NS = list(range(1, 32, 2))
OFFSETS = [0, 8, 32, 128, 512]
sys.path.insert(0, str(ROOT / "research/localized_weak_probe/code"))
from beta_scale import integral, groups, ap, ar, Radial, U, load, source, DATA
sys.set_int_max_str_digits(0)


def digest(path):
    h = sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def new(path, obj):
    with path.open("x") as f:
        json.dump(obj, f, indent=2)
        f.write("\n")


def now():
    return datetime.now(timezone.utc).isoformat()


def zpower(x, y, n):
    a, b = Q(1), Q(0)
    for _ in range(n):
        a, b = a*x-b*y, a*y+b*x
    return a, b


def derivative_fixtures():
    rows = []
    for n, k in [(1, 0), (3, 1), (21, 10), (31, 20)]:
        m = (n-1)//2
        for x, y in [(Q(1, 2), Q(1, 2)), (Q(3), Q(4))]:
            s = x*x+y*y
            re, im = zpower(x, y, n)
            re0, im0 = zpower(x, y, n-1)
            w = s**(k-m)/(1+s)**(k+2)
            dw = w*(Q(k-m)/s-Q(k+2)/(1+s))
            dx = n*im0*w+im*dw*2*x
            dy = n*re0*w+im*dw*2*y
            r = ar(s).sqrt()
            v, t = ar(1/(1+s)), ar(s/(1+s))
            sn, cn = ar(im)/r**n, ar(re)/r**n
            radial = v**2*t**k*((2*k+1)-(2*k+4)*t)*sn
            angular = n*v**2*t**k*cn
            computed = [ar(x)/r*radial-ar(y)/r*angular,
                        ar(y)/r*radial+ar(x)/r*angular]
            checks = [computed[0].overlaps(ar(dx)), computed[1].overlaps(ar(dy))]
            assert all(checks)
            rows.append({"n": n, "K": k, "x": str(x), "y": str(y),
                         "Cartesian_polar_derivative_overlap": checks})
    # B(3/2,2)=4/15 and B(1,2)=1/2.
    assert integral(arb_poly([1]), Q(1, 2), 1).overlaps(ar(Q(4, 15)))
    assert integral(arb_poly([1]), Q(0), 1).overlaps(ar(Q(1, 2)))
    return rows


def main(seconds):
    start = time.monotonic()
    ctx.prec = 2048
    fixtures = derivative_fixtures()
    src = source(NAME)
    assert digest(src) == "153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316"
    cache = DATA/f"{NAME}_D0.json.gz"
    assembly = ROOT/f"research/whole_plane_norms/verification/{NAME}_assembly.json"
    ass = json.loads(assembly.read_text())
    assert ass["source_sha256"] == digest(src)
    assert ass["polynomial_sha256"] == digest(cache)
    refpath = ROOT/"research/extended_weak_probes/verification/candidate007.json"
    refs = {row["k"]: row["exact_balls"]
            for row in json.loads(refpath.read_text())["rows"]}
    paths = [src, cache, assembly, refpath, Path(__file__), BASE/"PROOF.md",
             ROOT/"research/localized_weak_probe/code/beta_scale.py",
             ROOT/"research/localized_weak_probe/code/evaluate.py",
             ROOT/"research/radial_fourier/code/radial.py",
             ROOT/"research/whole_plane_norms/code/pipeline.py"]
    inputs = {str(p.relative_to(ROOT)): digest(p) for p in paths}
    tests = [(n, (n-1)//2+offset) for n in NS for offset in OFFSETS]
    manifest = {"candidate": NAME, "bits": ctx.prec, "tests": tests, "inputs": inputs}
    mp = BASE/"verification/manifest.json"
    if mp.exists():
        assert json.loads(mp.read_text()) == json.loads(json.dumps(manifest))
    else:
        new(mp, manifest)
    model = Radial(src)
    bg = groups(model, ["u1", "u2"])
    cg = groups(model, ["rho_x", "rho_y"])
    raw = load(NAME, 0)[0, 0]
    assert sorted({n for ell, kind, n in raw}) == list(range(1, 320, 2))
    projections = {n: [] for n in NS}
    for (ell, kind, n), poly in raw.items():
        assert kind == "s" and n > 0 and n % 2
        if n in projections:
            assert ell*model.delta/2-1 > -1
            projections[n].append((ell, ap(poly(U))))
    del raw
    print("prepared", len(tests), "tests", time.monotonic()-start, flush=True)
    radial = {}
    records = []
    for n, k in tests:
        dest = BASE/f"verification/n{n:03d}_K{k:05d}.json"
        if dest.exists():
            row = json.loads(dest.read_text())
            assert row["manifest_sha256"] == digest(mp)
            records.append(row)
            continue
        if time.monotonic()-start > seconds:
            break
        tick = time.monotonic()
        if k not in radial:
            dpoly = arb_poly([-3, 2*k+4])
            bg0 = arb.pi()/2*sum((integral(p, b, 2*k+1)
                                  for b, p in bg.items()), arb(0))
            bgd = arb.pi()/2*sum((integral(p*dpoly*dpoly, b, 2*k+1)
                                  for b, p in bg.items()), arb(0))
            cc = arb.pi()/2*sum((integral(p, b, 2*k+1)
                                 for b, p in cg.items()), arb(0))
            a = Q(2*k+2)
            l0, l1 = 3*model.c+1+2*model.c*k, 2*model.c*(k+2)
            aa = arb.pi()/2*ar(
                (l0*l0-2*l0*l1*a/(a+2)
                 +l1*l1*a*(a+1)/((a+2)*(a+3)))/(a*(a+1)))
            assert all(z > 0 and z.rel_accuracy_bits() > 150
                       for z in [bg0, bgd, cc, aa])
            radial[k] = (bg0, bgd, cc, aa)
        bg0, bgd, cc, aa = radial[k]
        A, B, C = aa.sqrt(), (bgd+n*n*bg0).sqrt(), cc.sqrt()
        D = A+B+C
        Hq = Q(max(2*k+1, 3))*(
            Q(k**k*4, (k+2)**(k+2)) if k else Q(1))
        H = ar(Hq)
        pairing = arb.pi()/2*sum(
            (integral(p, ell*model.delta/2-1, k+1)
             for ell, p in projections[n]), arb(0))
        I = abs(pairing)
        assert I > 0 and pairing.rel_accuracy_bits() > 150
        m = 2*I/(D+(D*D+4*H*I).sqrt())
        comparisons = {}
        if k in refs:
            comparisons["A"] = A.overlaps(arb(refs[k]["A"]))
            comparisons["C"] = C.overlaps(arb(refs[k]["C"]))
            if n == 1:
                comparisons["pairing"] = pairing.overlaps(arb(refs[k]["pairing"]))
            assert all(comparisons.values()), (n, k, comparisons)
        row = {
            "utc": now(), "n": n, "K": k, "candidate": NAME,
            "manifest_sha256": digest(mp),
            "pairing": pairing.str(80), "A": A.str(80), "B_upper": B.str(80),
            "C_upper": C.str(80), "D_upper": D.str(80),
            "H_upper_exact": str(Hq), "L2_radius_lower": m.str(80),
            "prior_component_checks": comparisons,
            "elapsed_seconds": time.monotonic()-tick,
        }
        new(dest, row)
        records.append(row)
        print("n", n, "K", k, "radius", m.str(24),
              "seconds", row["elapsed_seconds"], flush=True)
    complete = len(records) == len(tests)
    best = max(records, key=lambda row: float(arb(row["L2_radius_lower"]).mid()))
    bestball = arb(best["L2_radius_lower"])
    assert all(bestball > arb(row["L2_radius_lower"])
               for row in records if (row["n"], row["K"]) != (best["n"], best["K"]))
    out = {
        "utc": now(), "candidate": NAME, "manifest_sha256": digest(mp),
        "complete": complete, "tested": len(records), "expected": len(tests),
        "best_n_K": [best["n"], best["K"]],
        "best_radius_lower": best["L2_radius_lower"],
        "strict_finite_list_ordering": True, "fixtures": fixtures,
        "rows": records, "elapsed_seconds": time.monotonic()-start,
        "status": "N4-origin OPEN independent proof and numerical review",
    }
    if complete:
        new(BASE/"verification/full.json", out)
    else:
        (BASE/"verification/progress.json").write_text(json.dumps(out, indent=2)+"\n")
    print("DONE", len(records), "/", len(tests), "best", best["n"], best["K"],
          best["L2_radius_lower"], flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=float, default=430)
    main(parser.parse_args().seconds)

"""Independent elementary and panel calibrations for pole reduction."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import importlib.util
import json
import time
from flint import arb, ctx, fmpq as Q, fmpq_poly as Poly
from moments import integral, ar, V

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "research/rational_pole_moments"
PANEL = ROOT / "research/multiscale_moments/code/moments.py"
spec = importlib.util.spec_from_file_location("own_panel_moments", PANEL)
panel = importlib.util.module_from_spec(spec)
spec.loader.exec_module(panel)
H = lambda p: sha256(Path(p).read_bytes()).hexdigest()


def elementary(b, a, k):
    a = Q(a)
    if b == 0:
        return (1+ar(a)).log()/ar(a) if k == 1 else ar((1-(1+a)**(1-k))/(a*(k-1)))
    root = ar(a).sqrt()
    quotient = root.atan()/root
    if b == Q(-1, 2):
        return {
            1: 2*quotient,
            2: quotient+ar(1/(1+a)),
            3: 3*quotient/4+ar(Q(3, 4)/(1+a)+Q(1, 2)/(1+a)**2),
        }[k]
    assert b == Q(1, 2) and k == 1
    return 2*(1-quotient)/ar(a)


def main():
    ctx.prec = 2048
    start = time.monotonic()
    rows = []
    fixtures = []
    for a in [Q(1, 3), Q(99), Q(9999)]:
        for b, powers in [(Q(0), [1, 2, 7, 18]),
                          (Q(-1, 2), [1, 2, 3]), (Q(1, 2), [1])]:
            for k in powers:
                fixtures.append((f"one_{a}_{b}_{k}", b, Poly([1]), [(a, k)],
                                 elementary(b, a, k)))
    a, d = Q(99), Q(9999)
    for b in [Q(0), Q(-1, 2)]:
        value = (ar(a)*elementary(b, a, 1)-ar(d)*elementary(b, d, 1))/ar(a-d)
        fixtures.append((f"two_simple_{b}", b, Poly([1]), [(a, 1), (d, 1)], value))
    D = (1+a*V)**4*(1+d*V)**7
    P = Poly([1, -2, 1])
    b = Q(3, 7)
    target = ar(1/(b+1)-2/(b+2)+1/(b+3))
    fixtures.append(("exact_cancel", b, D*P, [(a, 4), (d, 7)], target))
    fixtures.append(("no_poles", b, P, [], target))
    for name, b, numerator, factors, target in fixtures:
        tick = time.monotonic()
        result, record = integral(b, numerator, factors)
        assert result.overlaps(target), (name, result, target)
        assert result.rel_accuracy_bits() > 300
        record.update({
            "name": name, "numerator": [str(c) for c in numerator],
            "value": result.str(100), "independent_value": target.str(100),
            "comparison": "independent elementary closed form",
            "overlap": True, "elapsed_seconds": time.monotonic()-tick,
        })
        rows.append(record)
        print(name, "passed", "seconds", record["elapsed_seconds"], flush=True)
    for name, b, numerator, factors in [
        ("two_signed", Q(2, 7), Poly([1, -3, 2]), [(a, 2), (d, 3)]),
        ("two_endpoint", Q(-3, 5), (1-V)**12, [(a, 4), (d, 7)]),
        ("merged_scale", Q(5, 9), Poly([2, -1, 4]), [(a, 1), (a, 2), (d, 2)]),
    ]:
        tick = time.monotonic()
        result, record = integral(b, numerator, factors)
        independent = panel.integral(b, numerator, factors, tolerance=Q(1, 2**300))
        enclosure = independent["lower"].union(independent["upper"])
        assert result.overlaps(enclosure), (name, result, enclosure)
        assert result.rel_accuracy_bits() > 300
        assert enclosure.rel_accuracy_bits() > 80
        record.update({
            "name": name, "numerator": [str(c) for c in numerator],
            "value": result.str(100), "independent_value": enclosure.str(100),
            "comparison": "independent rational panel method with explicit remainder",
            "independent_remainder": independent["remainder"].str(80),
            "panel_count": len(independent["panels"]),
            "overlap": True, "elapsed_seconds": time.monotonic()-tick,
        })
        rows.append(record)
        print(name, "passed", "seconds", record["elapsed_seconds"], flush=True)
    out = {
        "utc": datetime.now(timezone.utc).isoformat(), "precision_bits": ctx.prec,
        "proof_sha256": H(BASE/"PROOF.md"), "code_sha256": H(BASE/"code/moments.py"),
        "checker_sha256": H(__file__), "panel_code_sha256": H(PANEL),
        "fixtures": rows, "all_passed": True,
        "elapsed_seconds": time.monotonic()-start,
        "status": "OPEN independent peer; scalar primitive only",
    }
    (BASE/"verification").mkdir(exist_ok=True)
    with (BASE/"verification/result.json").open("x") as stream:
        json.dump(out, stream, indent=2)
        stream.write("\n")
    print("DONE", len(rows), "fixtures", out["elapsed_seconds"], flush=True)


if __name__ == "__main__":
    main()

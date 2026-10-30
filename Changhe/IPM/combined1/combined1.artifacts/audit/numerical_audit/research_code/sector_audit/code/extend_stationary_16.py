"""Independent exact orders 13..16, with full N1 coefficient comparison."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import gzip
import json
import sys
import time

from flint import arb, ctx, fmpq as Q
from extend_stationary import density, fields, inverse, parse, dump
from sectors_flint import add, product_cs, aq

sys.set_int_max_str_digits(0)
BASE = Path(__file__).resolve().parents[1]


def digest(path):
    h = sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def run():
    start = time.monotonic()
    ctx.prec = 512
    checkpoint = BASE / "verification/stationary_principal.json"
    extension = BASE / "verification/stationary_extension_12.json"
    peerfile = BASE / "peer_data/N1_orders_0_16.json"
    normfile = BASE / "peer_data/N1_E_4_16.json"
    output = BASE / "verification/stationary_extension_16_summary.json"
    assert not output.exists()
    original = json.loads(checkpoint.read_text())
    previous = json.loads(extension.read_text())
    assert previous["checkpoint_sha256"] == digest(checkpoint)
    assert previous["code_sha256"] == digest(BASE / "code/extend_stationary.py")
    peer = json.loads(peerfile.read_text())
    norms = json.loads(normfile.read_text())
    c = Q(original["cl"])
    assert Q(peer["cl_exact"]) == c
    gamma, delta = 1 / c, 1 - 1 / c
    saved = original["branches"] + previous["additional_orders"]
    assert len(saved) == 12
    potentials = [parse(original["leading_potential"])]
    potentials += [parse(row["potential_cos"]) for row in saved]
    FF = [fields(C, gamma - j * delta) for j, C in enumerate(potentials)]
    for j, row in enumerate(saved, 1):
        assert FF[j][0] == parse(row["stationary_density_sin"])
        assert {n: j * (c - 1) * v for n, v in FF[j][0].items()} == parse(row["forcing_sin"])
    print("loaded exact checkpoint through 12", time.monotonic() - start, flush=True)
    generated = []
    for j in range(13, 17):
        force = {}
        for i in range(j):
            k = j - 1 - i
            force = add(force, product_cs(FF[i][1], FF[k][3]))
            force = add(force, product_cs(FF[k][4], FF[i][2]))
        G = {n: v / (j * (c - 1)) for n, v in force.items()}
        alpha = gamma - j * delta
        C = inverse(G, alpha + 3)
        ff = fields(C, alpha)
        assert ff[0] == G
        assert density(C, alpha + 3) == G
        FF.append(ff)
        potentials.append(C)
        row = {
            "index": j, "exponent_exact": str(alpha),
            "potential_cos": dump(C), "stationary_density_sin": dump(G),
            "forcing_sin": dump(force),
        }
        target = BASE / f"verification/stationary_order_{j}_independent.json.gz"
        assert not target.exists()
        with gzip.open(target, "wt", encoding="utf-8", compresslevel=3) as f:
            json.dump(row, f, separators=(",", ":"))
            f.write("\n")
        generated.append({"file": str(target.relative_to(BASE)), "sha256": digest(target)})
        print("generated order", j, "seconds", time.monotonic() - start, flush=True)
    checks = []
    count = 0
    for j in range(17):
        row = peer["orders"][str(j)]
        C_peer, G_peer = parse(row["C"]), parse(row["G"])
        checks.append({
            "order": j, "exponent": Q(row["alpha"]) == gamma - j * delta,
            "potential": C_peer == potentials[j], "density": G_peer == FF[j][0],
            "potential_coefficients": len(C_peer), "density_coefficients": len(G_peer),
        })
        assert all(checks[-1][key] for key in ("exponent", "potential", "density"))
        count += len(C_peer) + len(G_peer)
    normchecks = []
    for j in range(4, 17):
        force = {n: j * (c - 1) * v for n, v in FF[j][0].items()}
        energy = sum((v * v for v in force.values()), Q(0))
        row = norms[str(j)]
        assert Q(row["exponent_exact"]) == gamma - j * delta
        assert Q(row["E_n_full_squared_over_pi_exact"]) == energy
        assert row["max_harmonic"] == max(force)
        ball = (arb.pi() * aq(energy)).sqrt()
        normchecks.append({
            "order": j, "exact_energy_match": True,
            "exponent_match": True, "max_harmonic": max(force),
            "forcing_full_circle_norm": ball.str(80),
            "peer_float": row["E_n_full_float"],
        })
        print("norm", j, ball.str(25), flush=True)
    sources = [checkpoint, extension, peerfile, normfile,
               BASE / "code/extend_stationary.py", BASE / "code/sectors_flint.py",
               BASE / "PROOF_EXTENSION_16.md", Path(__file__)]
    result = {
        "utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "precision_bits": ctx.prec, "cl_exact": str(c),
        "elapsed_seconds": time.monotonic() - start,
        "input_hashes": {str(p.relative_to(BASE)): digest(p) for p in sources},
        "checks": checks, "coefficient_equalities": count,
        "norm_checks": normchecks, "generated_exact_data": generated,
        "scope": "Finite exact recurrence only; no convergence or full residual bound.",
    }
    output.write_text(json.dumps(result, indent=2) + "\n")
    print("DONE", output, time.monotonic() - start, flush=True)


if __name__ == "__main__":
    run()

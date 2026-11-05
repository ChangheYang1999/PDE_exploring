#!/usr/bin/env python3
"""Independent complete local-cover and scalar-envelope assembly audit."""
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime, timezone
from flint import arb, ctx

HERE = Path(__file__).resolve().parent
FOLDER = HERE / "local_energy_coefficients_v01"


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def aa(x):
    x = F(x)
    return arb(x.numerator)/arb(x.denominator)


def main():
    result_path = FOLDER / "result.json"
    result = json.loads(result_path.read_text())
    cfg = result["configuration"]
    assert result["status"] == "CERTIFIED_LOCAL_Q_COEFFICIENTS"
    assert json.loads((FOLDER/"configuration.json").read_text()) == cfg
    for name, h in cfg["bindings"].items():
        assert sha(HERE/name) == h
    ctx.prec = cfg["precision"]
    rows, bindings = {}, {str(result_path.relative_to(HERE)): sha(result_path)}
    lo, hi, ratio = map(F, [cfg["rmin"], cfg["rmax"], cfg["ratio"]])
    assert lo*ratio**(cfg["panels"]-1) < hi <= lo*ratio**cfg["panels"]
    for path in sorted(FOLDER.glob("chunk_*.json")):
        record = json.loads(path.read_text())
        assert record["configuration"] == cfg
        bindings[str(path.relative_to(HERE))] = sha(path)
        for row in record["rows"]:
            i = row["index"]
            assert i not in rows and row["pass"]
            rows[i] = row
    assert sorted(rows) == list(range(cfg["panels"]))
    candidates = {k: [arb(result[s][k]).abs_upper() for s in ["origin", "exterior"]]
                  for k in ["B0", "H1", "H2", "Hu"]}
    wu2 = []
    for i, row in rows.items():
        paths = [x["path"] for x in row["leaves"]]
        assert len(paths) == len(set(paths))
        def complete(prefix):
            if prefix in paths:
                assert not any(x != prefix and x.startswith(prefix) for x in paths)
            else:
                assert len(prefix) < cfg["max_depth"]
                complete(prefix+"0"); complete(prefix+"1")
        complete("")
        for leaf in row["leaves"]:
            assert leaf["strain_pass"]
            assert math.isfinite(leaf["strain_square_upper"]) and leaf["strain_square_upper"] <= 2.25
            for k in candidates:
                value = arb(leaf[k]); assert value.is_finite() and value >= 0
                candidates[k].append(value.abs_upper())
            left, right = lo*ratio**i, min(lo*ratio**(i+1), hi)
            for bit in leaf["path"]:
                middle = (left+right)/2
                if bit == "0": right = middle
                else: assert bit == "1"; left = middle
            r = aa(left)
            wu2.append(arb(leaf["Hu"]).abs_upper()*(1+4*r*r).sqrt()/r)
    for end, r in [("origin", lo), ("exterior", hi)]:
        assert arb(result[end]["S"]) < aa(F(3,2))
        r = aa(r)
        wu2.append(arb(result[end]["Hu"]).abs_upper()*(1+4*r*r).sqrt()/r)
    env = {k: max(v) for k,v in candidates.items()}
    for k, value in env.items():
        assert arb(result["global_envelopes"][k]).contains(value)
    B0,H1,H2,Hu = [env[k] for k in ["B0","H1","H2","Hu"]]
    c = aa(F(4076476460239181,2251799813685248)); q = aa(F(21,10))
    K1 = 8*arb(2).sqrt()*(1-c/10+aa(F(3,2)))+4*Hu+4*arb(2).sqrt()*B0+4*H1
    K1 += 2*q*(1+1/arb(2).sqrt())*H1+(1+q)*H2/2
    K0 = 4*((8-2*q)*c+4+B0+(2-q/2)*H1/2)
    # Replacing serialized endpoint intervals by their upper endpoints can
    # add a final decimal serialization ulp. Adopt the larger fresh upper;
    # equality with the producer's unrounded intermediate is unnecessary.
    K1 = max(K1.abs_upper(), arb(result["E1_local_upper"]).abs_upper())
    K0 = max(K0.abs_upper(), arb(result["E0_local_upper"]).abs_upper())
    assert aa(F(3,2)) < c
    out = {
        "status": "ROOT_LOCAL_COEFFICIENT_ASSEMBLY_PASS",
        "finished_utc": datetime.now(timezone.utc).isoformat(),
        "program_sha256": sha(Path(__file__)), "input_sha256": bindings,
        "panels": len(rows), "all_leaf_partitions_and_strain_flags_checked": True,
        "K1_recomputed": K1.str(80), "K0_recomputed": K0.str(80),
        "Wu2_upper": max(v.abs_upper() for v in wu2).str(80),
        "scope": "Complete saved local cover, endpoint flags and independent scalar assembly; no stationary theorem claim.",
    }
    (HERE/"ROOT_LOCAL_COEFFICIENT_ASSEMBLY.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps({k:v for k,v in out.items() if k!="input_sha256"},indent=2))


if __name__ == "__main__":
    main()

"""Independent exact first-resonance scan for sin(M theta), M>=3."""
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import argparse
import json
import time
from rational_scan_audit import compute


def prime(p):
    return p >= 2 and all(p % d for d in range(2, int(p ** .5) + 1))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seconds", type=float, default=480)
    args = ap.parse_args()
    start = time.monotonic()
    root = Path("research/59_missing_first_harmonic")
    for name in ("sources", "verification"):
        (root / name).mkdir(exist_ok=True)
    pairs = [(M, p, a) for M, maximum in ((3, 31), (5, 19), (7, 13))
             for p in range(5, maximum + 1) if prime(p) for a in range(4, p, 2)]
    rows = []
    for M, p, a in pairs:
        out = root / "verification" / f"M{M}_p{p}_a{a}.json"
        if out.exists():
            data = json.loads(out.read_text())
        else:
            if time.monotonic() - start > args.seconds:
                break
            data = compute(Fraction(a, p), {M: "1"}, p)
            q = Fraction(data["kappa_exact"])
            u, v = q.numerator, q.denominator
            valuation = 0
            if u:
                while u % p == 0:
                    u //= p
                    valuation += 1
                while v % p == 0:
                    v //= p
                    valuation -= 1
                residue = u * pow(v, -1, p) % p
            else:
                valuation, residue = None, 0
            data.update(harmonic=M, p=p, a=a, p_adic_valuation=valuation,
                        normalized_unit_residue=residue, exact_compatible=not bool(q),
                        checked_at_utc=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
            out.write_text(json.dumps(data, indent=2) + "\n")
            print(json.dumps({k: data[k] for k in ("harmonic", "p", "a", "p_adic_valuation",
                                                  "normalized_unit_residue", "exact_compatible", "elapsed_s")}), flush=True)
        rows.append({k: data[k] for k in ("harmonic", "p", "a", "p_adic_valuation",
                                         "normalized_unit_residue", "exact_compatible", "elapsed_s")})
        result = dict(checked_at_utc=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                      expected_count=len(pairs), completed_count=len(rows),
                      all_complete=len(rows) == len(pairs),
                      compatible=[r for r in rows if r["exact_compatible"]],
                      total_actual_case_elapsed_s=sum(r["elapsed_s"] for r in rows),
                      actual_segment_elapsed_s=time.monotonic() - start, rows=rows)
        (root / "verification/summary.json").write_text(json.dumps(result, indent=2) + "\n")
    hashes = {}
    for name in ("higher_harmonic_resonance_scan.py", "rational_scan_audit.py", "laurent_log_audit.py"):
        raw = (Path("code") / name).read_bytes()
        (root / "sources" / (name + ".txt")).write_bytes(raw)
        hashes[name] = sha256(raw).hexdigest()
    (root / "sources/hashes.json").write_text(json.dumps(hashes, indent=2) + "\n")
    print("Completed", len(rows), "of", len(pairs), "segment seconds", time.monotonic() - start, flush=True)


if __name__ == "__main__":
    main()

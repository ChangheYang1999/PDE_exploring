"""Check the peer certificate's identities and closed-rectangle partition."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime, timezone
import json
import time
from flint import arb, ctx

BASE = Path(__file__).resolve().parents[1]
PEER = BASE/"peer_review"


def sha(p):
    return sha256(p.read_bytes()).hexdigest()


def rectangle(path):
    x0, x1, y0, y1 = Q(0), Q(1), Q(-1), Q(1)
    for symbol in path:
        if symbol == "t":
            x1 = (x0+x1)/2
        elif symbol == "T":
            x0 = (x0+x1)/2
        elif symbol == "z":
            y1 = (y0+y1)/2
        elif symbol == "Z":
            y0 = (y0+y1)/2
        else:
            raise ValueError(symbol)
    return x0, x1, y0, y1


start = time.monotonic()
ctx.prec = 512
cover = json.loads((PEER/"T4_global_cover.json").read_text())
summary = json.loads((PEER/"T4_global_summary.json").read_text())
gradient = json.loads((PEER/"T4_global_gradient.json").read_text())
identities = {
    "cover_code": cover["code_sha256"] == sha(PEER/"T4_global_certify.py"),
    "cover_proof": cover["proof_sha256"] == sha(PEER/"T4_global_PROOF.md"),
    "cover_reconstruction": cover["reconstruction_sha256"] == sha(PEER/"T4_global_gradient.json"),
    "cover_N4_target": cover["N4_cover_sha256"] == sha(BASE/"verification/d2_L2_768.json"),
    "summary_cover": summary["cover_sha256"] == sha(PEER/"T4_global_cover.json"),
    "summary_code": summary["code_sha256"] == sha(PEER/"T4_global_finish.py"),
    "gradient_coefficients": gradient["all_gradient_coefficients_match"],
    "gradient_code": gradient["code_sha256"] == sha(PEER/"T4_global_certify.py"),
}
assert all(identities.values()), identities
assert not cover["pending"] and cover["all_pass"] and cover["complete_partition"]
cells = [rectangle(row["path"]) for row in cover["accepted"]]
assert len(set(cells)) == len(cells) == summary["accepted_cells"]
assert all(row["pass"] and arb(row["schur_lower"]) > 0 for row in cover["accepted"])
area = sum(((b-a)*(d-c) for a, b, c, d in cells), Q(0))
assert area == 2
pairs = 0
for i, (a, b, c, d) in enumerate(cells):
    for aa, bb, cc, dd in cells[i+1:]:
        assert min(b, bb) <= max(a, aa) or min(d, dd) <= max(c, cc)
        pairs += 1
assert arb(summary["signed_L2_rate_lower"]) > arb("2.0199")
out = {
    "utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    "target": "N4-051, d2 theta<=2/25",
    "peer_audit": "T4-053",
    "hash_and_identity_checks": identities,
    "cells": len(cells),
    "area_exact": str(area),
    "disjoint_interior_pairs_checked": pairs,
    "all_schur_margins_positive": True,
    "signed_L2_rate_lower": summary["signed_L2_rate_lower"],
    "peer_cover_sha256": sha(PEER/"T4_global_cover.json"),
    "peer_summary_sha256": sha(PEER/"T4_global_summary.json"),
    "review_sha256": sha(BASE/"REVIEW_T4_GLOBAL.md"),
    "code_sha256": sha(Path(__file__)),
    "elapsed_seconds": time.monotonic()-start,
}
(BASE/"verification/T4_global_confirmation.json").write_text(json.dumps(out, indent=2)+"\n")
print(json.dumps(out, indent=2))

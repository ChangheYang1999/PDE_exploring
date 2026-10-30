"""Rigorous point values of the fields of an exact candidate at rational points (lane c1-n3): rho, rho_x, rho_y, U_1, U_2,
V = c X + U, F, and theta_X = (|grad rho| - rho_y)/2, by direct Taylor jets of the exact potential at 640 bits
(the jet evaluator of certification/audit_e2norms.py, independent of the compactified polynomials)."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import json, sys, hashlib
from flint import arb, ctx
sys.path.insert(0, str(Path(__file__).resolve().parent))
import e2norms as E, audit_e2norms as AU

def fields_at(A, c, xq, yq):
    x = AU.aq(xq); y = AU.aq(yq)
    chi = AU.direct_chi(A, c, x, y)
    rho = -chi[2, 1] - chi[0, 3]
    rho_x = -chi[3, 1] - chi[1, 3]; rho_y = -chi[2, 2] - chi[0, 4]
    u1 = -chi[1, 2]; u2 = chi[2, 1]
    V1 = AU.aq(c) * x + u1; V2 = AU.aq(c) * y + u2
    F = V1 * rho_x + V2 * rho_y - rho
    grad = (rho_x ** 2 + rho_y ** 2).sqrt()
    theta_X = (grad - rho_y) / 2
    return {'rho': rho, 'rho_x': rho_x, 'rho_y': rho_y, 'U1': u1, 'U2': u2, 'V_abs': (V1 ** 2 + V2 ** 2).sqrt(), 'grad_rho_abs': grad, 'F': F, 'theta_X': theta_X}

def run(source, ID, points, outdir):
    ctx.prec = 640
    c, A, src_sha, can_sha, meta = E.load_reference(source)
    rows = []
    for xs, ys in points:
        v = fields_at(A, c, Q(xs), Q(ys))
        rows.append({'point': [xs, ys], **{k: val.str(30) for k, val in v.items()}})
        print(ID, (xs, ys), 'F =', v['F'].str(20), 'theta_X =', v['theta_X'].str(15), '|V| =', v['V_abs'].str(12), 'rho_y =', v['rho_y'].str(15), flush=True)
    out = {'utc': datetime.now(timezone.utc).isoformat(timespec='seconds'), 'id': ID, 'source_sha256': src_sha, 'canonical_sha256': can_sha,
           'method': 'direct Taylor jets of the exact potential at 640 bits (balls); theta_X = (|grad rho| - rho_y)/2', 'points': rows,
           'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(outdir, f'{ID}_point_fields.json').write_text(json.dumps(out, indent=1) + '\n')

if __name__ == '__main__':
    source, ID, outdir = sys.argv[1:4]; pts = [p.split(',') for p in sys.argv[4:]]
    run(source, ID, pts, outdir)

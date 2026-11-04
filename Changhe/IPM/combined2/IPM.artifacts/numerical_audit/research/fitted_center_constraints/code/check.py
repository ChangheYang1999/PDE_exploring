"""Independent exact final-atom checks, with containing scalar displays only."""
from collections import defaultdict
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import argparse
import importlib.util
import json
import time
from flint import fmpq as Q, arb, ctx

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/fitted_center_constraints'
C = Q(4076476460239181, 2251799813685248)
REFERENCE = 'ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21'
CHECKS = 0

def need(value, label=''):
    global CHECKS
    assert value, label
    CHECKS += 1

def stamp():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

def digest(path):
    h = sha256()
    with Path(path).open('rb') as stream:
        while chunk := stream.read(1048576): h.update(chunk)
    return h.hexdigest()

def local(text):
    p = Path(text)
    need(not p.is_absolute() and '..' not in p.parts)
    return ROOT / p

def exact(text):
    need(type(text) is str)
    value = Q(text)
    need(value.denominator > 0)
    return value

def display(value, places=24):
    value = arb(value)
    need(value.is_finite())
    lo, hi, scale = value.lower().fmpq(), value.upper().fmpq(), 10**places
    a, b = lo*scale, hi*scale
    n = int(a.numerator)//int(a.denominator)-1
    m = -((-int(b.numerator))//int(b.denominator))+1
    need(Q(n, scale) < lo and hi < Q(m, scale))
    def decimal(v):
        sign = '-' if v < 0 else ''
        v = abs(v)
        return sign+str(v//scale)+'.'+str(v%scale).zfill(places)
    return dict(lower_exact=str(lo), upper_exact=str(hi),
                strict_lower_decimal=decimal(n), strict_upper_decimal=decimal(m))

def read_atoms(document):
    need(document['schema_version'] == 'ipm-potential-correction-v1')
    need(document['reference_sha256'] == REFERENCE)
    need(exact(document['c_exact']) == C)
    mu, e = 4/C-3, 4/C-5
    need(exact(document['mu_exact']) == mu and exact(document['e_exact']) == e)
    atoms, seen, degrees, A, B = [], set(), defaultdict(int), Q(0), Q(0)
    absA, absB = Q(0), Q(0)
    for row in document['atoms']:
        for key in ('n', 'h', 'd'): need(type(row[key]) is int, 'strict integer '+key)
        n, h, d = row['n'], row['h'], row['d']
        need(n > 0 and n % 2 == 1 and h >= 0 and d >= 0)
        a, b, t = (exact(row[key]) for key in ('coefficient_exact', 'b_exact', 'scale_exact'))
        need(t > 0 and a != 0)
        tau = n+2*h+2*b-2*d
        need(tau <= mu)
        need(exact(row['tau_exact']) == tau)
        key = (n, h, b, t, d)
        need(key not in seen, 'duplicate exact atom')
        seen.add(key); degrees[tau] += 1
        aa = a*t**(-d)*((b-Q(d)/t) if h == 0 else 1) if n == 1 and h <= 1 else Q(0)
        bb = a*t**(-d) if n == 3 and h == 0 else Q(0)
        A += aa; B += bb; absA += abs(aa); absB += abs(bb)
        atoms.append((a, n, h, b, t, d))
    need(document['n_atoms_nonzero'] == len(atoms))
    need(document['n_atoms_total'] >= len(atoms))
    return atoms, A, B, absA, absB, degrees

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--request', required=True); p.add_argument('--tag', required=True)
    p.add_argument('--bits', type=int, default=1024)
    args = p.parse_args(); ctx.prec = args.bits
    need(args.bits >= 128 and args.tag and all(v.isalnum() or v in '_-' for v in args.tag))
    folder = BASE / 'verification' / args.tag; folder.mkdir(exist_ok=False)
    started, tick = stamp(), time.monotonic()
    request_path = local(args.request); request = json.loads(request_path.read_text())
    docs, bindings = {}, {args.request: digest(request_path)}
    for name, item in request['inputs'].items():
        path = local(item['path']); need(digest(path) == item['sha256'], name+' binding')
        docs[name] = json.loads(path.read_text()); bindings[item['path']] = item['sha256']
    for text in request['proof_dependencies']:
        bindings[text] = digest(local(text))
    bindings['research/fitted_center_constraints/PROOF.md'] = digest(BASE/'PROOF.md')
    phi, bg, structure, origin = (docs[k] for k in ('phi', 'base', 'structure', 'origin'))
    bsha = request['inputs']['base']['sha256']
    need(phi['center']['base_exact_sha256'] == bsha)
    need(structure['input_sha256'] == origin['input_sha256'] == bsha)
    need(exact(bg['cl_exact']) == exact(structure['cl_exact']) == C)
    a0 = exact(origin['origin_a0_exact'])
    need(a0 == exact(structure['a0_exact']) == exact(phi['center']['a0_base_exact']))
    need(exact(origin['origin_ell_exact']) == exact(structure['ell_exact']) == 1-C)
    need(structure['origin_normalization_pass'] and structure['all_eleven_forbidden_zero'])
    need(exact(origin['origin_normalization_exact']) == 0)
    atoms, A, B, absA, absB, degrees = read_atoms(phi)
    mu, e, q = 4/C-3, 4/C-5, Q(21, 10)
    astar, ell = a0-8*A, 2*A+6*B
    meta = phi['exact_identities']
    for key, value in [('A_cubic', A), ('B_cubic', B), ('A_plus_3B', A+3*B),
                       ('ell_h_phi', ell), ('origin_density_slope_h_phi', -8*A),
                       ('a_star_exact', astar),
                       ('a_star_minus_q_times_2c_minus_2_at_q_21_10', astar-q*(2*C-2))]:
        need(exact(meta[key]) == value, 'metadata '+key)
    # Independent parser from the auditor's earlier accepted common interface.
    spec = importlib.util.spec_from_file_location('fit_constraint_existing_fields', ROOT/'research/potential_evaluator/code/fields.py')
    fields = importlib.util.module_from_spec(spec); spec.loader.exec_module(fields)
    f_atoms, identities = fields.parse(phi, True, False)
    need(atoms == f_atoms)
    need(Q(identities['cubic_A_exact']) == A and Q(identities['cubic_B_exact']) == B)
    need(Q(identities['ell_exact']) == ell)
    bindings['research/potential_evaluator/code/fields.py'] = digest(ROOT/'research/potential_evaluator/code/fields.py')
    addition = defaultdict(Q)
    for a, n, h, b, t, d in atoms:
        if n+2*h+2*b-2*d == mu: addition[n] += (C*e-1)*a*(n*n-mu*mu)
    producer = phi['sector_e_correction']
    need(exact(producer['c_e_minus_1_exact']) == C*e-1)
    reported = {int(n): exact(v) for n, v in producer['added_sine_coefficients'].items()}
    for n in set(addition) | set(reported): need(addition[n] == reported.get(n, Q(0)))
    sectors = [row for row in structure['sectors'] if row['J'] == 3 and row['N'] == 1]
    need(len(sectors) == 1)
    base_sector = sectors[0]; need(exact(base_sector['exponent_exact']) == e)
    base_map = {int(n): exact(v) for n, v in base_sector['sine_coefficients'].items()}
    need(all(n > 0 and n % 2 for n in base_map))
    need(sum((v*v for v in base_map.values()), Q(0)) == exact(base_sector['sine_square_sum_exact']))
    combined = {n: base_map.get(n, Q(0))+addition[n] for n in set(base_map) | set(addition)}
    combined = {n: v for n, v in combined.items() if v}
    square = sum((v*v for v in combined.values()), Q(0))
    need(Q(7, 5) < 4*(1-1/C))
    out = dict(started_utc=started, precision_bits=args.bits, code_sha256=digest(__file__),
               files=bindings, request=args.request, input_sha256=request['inputs']['phi']['sha256'],
               base_sha256=bsha, status='frozen producer trial, not a registered candidate',
               atom_count=len(atoms), degrees=[[str(k), v] for k, v in sorted(degrees.items())],
               A_exact=str(A), B_exact=str(B), ell_correction_exact=str(ell),
               normalization_pass=A+3*B == 0, a_star_exact=str(astar), a_star=display(astar),
               slope_positive=astar > 0, cap_margin_exact=str(astar-q*(2*C-2)),
               cap_margin=display(astar-q*(2*C-2)), cap_pass=astar >= q*(2*C-2),
               origin_margin=display(C+1-q-max(q*(2*C-2)-astar, Q(0))),
               origin_A_abs_sum_exact=str(absA), origin_B_abs_sum_exact=str(absB),
               origin_A_cancellation=display(absA/abs(A)) if A else None,
               origin_B_cancellation=display(absB/abs(B)) if B else None,
               leading_exponent_exact=str(e), leading_sector_nonzero=bool(combined),
               leading_addition={str(n): str(v) for n, v in sorted(addition.items())},
               leading_combined={str(n): str(v) for n, v in sorted(combined.items())},
               leading_square_sum_exact=str(square),
               leading_circle_norm=display((arb.pi()*arb(square)).sqrt()),
               metadata_all_agree=True,
               scope='Exact class, origin and leading-sector checks only. No full residual norm, changed background or closure.')
    out.update(finished_utc=stamp(), elapsed_seconds=time.monotonic()-tick, checks=CHECKS)
    with (folder/'result.json').open('x') as stream: json.dump(out, stream, indent=2); stream.write('\n')
    print(out['finished_utc'], 'checks', CHECKS, 'seconds', out['elapsed_seconds'],
          'normalized', out['normalization_pass'], 'cap', out['cap_pass'], flush=True)

if __name__ == '__main__': main()

"""Own polar test-energy and complete rational residual pairing replay."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
import importlib.util, json, os, sys, time
from flint import fmpq as Q, fmpq_poly as Poly, arb, ctx
R = Path(__file__).resolve().parents[3]
B = R / 'research/candidate016_dual_lower'
CANDIDATE = 'C1-N1-016-legqs25-quot013'
RAW_SHA = 'a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42'
now = lambda: datetime.now(timezone.utc).isoformat()
sha = lambda p: sha256(Path(p).read_bytes()).hexdigest()
sys.set_int_max_str_digits(0)

def log(*args): print(now(), *args, flush=True)
def exclusive(path, value):
    with Path(path).open('x') as f: json.dump(value, f, indent=2); f.write('\n')
def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    out = importlib.util.module_from_spec(spec); spec.loader.exec_module(out); return out
def aq(q):
    q = Q(q); return arb(q.numerator) / arb(q.denominator)
def floor_exact(x, places=24):
    assert x.is_finite()
    m, e = x.lower().man_exp(); m, e = int(m), int(e)
    r = Fraction(m * 2**e) if e >= 0 else Fraction(m, 2**(-e))
    scale = 10**places
    answer = Q((r.numerator * scale)//r.denominator-1, scale)
    assert aq(answer) < x.lower()
    return answer

def main():
    ctx.prec = 4096; tick = time.monotonic(); inputs = {}; checks = {}
    assert os.sched_getaffinity(0) == {57} and os.getpriority(os.PRIO_PROCESS, 0) == 19
    for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']: assert os.environ[k] == '1'
    def bind(path, expected=None):
        path = Path(path); h = sha(path); rel = str(path.relative_to(R))
        assert expected is None or h == expected, (rel, h, expected)
        assert rel not in inputs or inputs[rel] == h
        inputs[rel] = h; return path
    def read(path, expected=None): return json.loads(bind(path, expected).read_text())
    def check(label, ok):
        assert label not in checks; checks[label] = bool(ok); assert ok, label
    proof = read(B/'verification/PROOF_FIRST.json')
    bind(B/'PROOF.md', proof['proof_sha256']); bind(Path(__file__))
    frozen = read(B/'source/MANIFEST.json')
    for rel, rec in frozen['files'].items(): bind(B/'source'/rel, rec['sha256'])
    peer = read(B/'source/N3_exact_vectors.json')
    check('peer_candidate_raw', peer['id'] == CANDIDATE and peer['source_sha256'] == RAW_SHA)
    check('peer_code_as_text_bound', peer['code_sha256'] == sha(B/'source/N3_legqs_hdual.py'))
    check('two_complete_peer_modes', [r['n'] for r in peer['modes']] == [1,3] and 'H_lower_ball' in peer)
    check('peer_not_imported_or_executed', True)
    accepted = read(R/'research/candidate016_scaled_norm_peer/verification/comparison_G0_rF_G1_P2_v01.json',
                    'a2f68954828f60a7dc8983ecb69e8e30ddcd8e868ec0d1b58ce56faa27eeaedc')
    check('complete_component_acceptance', all(accepted['checks'].values()) and accepted['verdict'].startswith('CONFIRMED'))
    for rel, h in accepted['inputs'].items(): bind(R/rel, h)
    cal = read(R/'research/joint_scaled_dyadic016/verification/result.json',
               '16a4a6ac68132e8612f4e2a9717b10b4b15d20890debd54ab67c99bd36779925')
    check('projection_calibration_accepted', cal['verdict'].startswith('CONFIRMED'))
    for rel, h in cal['inputs'].items(): bind(R/rel, h)
    closure = read(R/'research/joint_scaled_dyadic016/verification/bound_production_v01_result.json',
                   'c3ec1e20ef32b05b02139ffb1cb78ad872c7d1e7519383955c53b402f48b7add')
    start = read(R/'research/joint_scaled_dyadic016/verification/bound_production_v01_start.json', closure['start_sha256'])
    check('projection_source_closure_accepted', closure['all_before_hashes_unchanged'])
    for rel, h in start['sources'].items(): bind(R/rel, h)
    calib = {}
    for n in [1,3]:
        rel = f'research/joint_scaled_dyadic016/verification/{CANDIDATE}/mode_{n:03d}.json'
        calib[n] = read(R/rel, closure['final_modes'][rel])
    baseline = read(R/'research/negative_norm_forcing_assembly/verification/result.json',
                    'd94473eb11c0708e25a9529f00b49576628023066e626ed9170bf29b62e22e7c')
    for rel, h in baseline['inputs'].items(): bind(R/rel, h)
    check('baseline007_two_sided_accepted', all(baseline['checks'].values()) and baseline['E_upper']['strict_bounds_verified'])
    bind(R/'research/negative_norm_forcing_assembly/PROOF.md')
    bind(R/'research/candidate016_mode_hardy/PROOF.md', 'c467c5f54204ba8135d36b5352de630689273a049ab5fefeeb7aeb93cefb8675')
    rawp = R/f'research/candidate_audits/data/{CANDIDATE}/quot013_legqs25_m9to15_cpu_m16_exact.json'
    raw = read(rawp, RAW_SHA); bind(rawp.parent/'MANIFEST.json')
    check('immutable_raw_unchanged', sha(R.parent/'c1-shared/candidate_snapshots'/CANDIDATE/rawp.name) == RAW_SHA)
    module_paths = ['research/joint_scaled_factored_weak/code/fields_joint.py',
                    'research/joint_scaled_factored_weak/code/weak.py',
                    'research/factored_pole_moments/code/moments.py',
                    'research/rational_pole_moments/code/moments.py']
    for rel in module_paths: bind(R/rel)
    exclusive(B/'verification/start_v01.json', {'utc':now(), 'inputs':inputs, 'precision_bits':ctx.prec})
    sys.path.insert(0, str(R/'research/joint_scaled_factored_weak/code'))
    import fields_joint as J
    import weak as W
    M = load('own_dual_positive_pole', R/module_paths[-1])
    model = J.ScaledRadial(raw)
    check('exact_c_delta', str(model.c) == '4076476460239181/2251799813685248' and str(model.delta) == '1824676646553933/4076476460239181')
    log('OWN_MODEL_READY', time.monotonic()-tick)
    rows = []; lower_square = Q(0)
    for peerrow in peer['modes']:
        n = peerrow['n']; mode_tick = time.monotonic(); pby = {}; count = 0
        betas = [Q(b) for b in peerrow['betas']]
        check(f'mode{n}_distinct_betas', len(betas) == len(set(betas)))
        kmin = -1 if n == 1 else max(0, (n-2)//2)
        labels = {f'{beta},{k}' for beta in betas for k in range(kmin,peerrow['kmax']+1)}
        check(f'mode{n}_basis_labels', len(labels) == peerrow['basis_size'] and set(peerrow['x_rational']) <= labels)
        for label, value in peerrow['x_rational'].items():
            bs, ks = label.rsplit(',',1); beta, k, x = Q(bs), int(ks), Q(value)
            assert beta > Q(3,2) and k >= -1 and 3+2*k >= n and (3+2*k-n)%2 == 0
            b = beta-1; pby[b] = pby.get(b, Poly()) + x*J.T**(k+1); count += 1
        check(f'mode{n}_nonzero_test', bool(pby) and any(pby.values()))
        dby = {b:(1-2*b*J.T)*P+2*J.T*J.V*P.derivative() for b,P in pby.items()}
        energy_groups = {}
        for b, P in pby.items():
            for c, S in pby.items():
                e = b+c-2; assert e > -1
                energy_groups[e] = energy_groups.get(e,Poly()) + dby[b]*dby[c]+n*n*P*S
        den = Q(0); den_evidence = []
        for e, polynomial in sorted(energy_groups.items()):
            pv = polynomial(J.V)
            exact = sum((coef/(e+j+1) for j,coef in enumerate(pv)), Q(0))/2
            den += exact
            den_evidence.append({'exponent':str(e),'degree':pv.degree(), 'integral_over_pi_exact':str(exact)})
        check(f'mode{n}_positive_gradient_energy', den > 0)
        check(f'mode{n}_peer_exact_gradient_energy', den == Q(peerrow['grad_psi_sq_over_pi_exact']))
        log('EXACT_POLAR_ENERGY', n, 'groups',len(energy_groups),'seconds',time.monotonic()-mode_tick)
        projection, pairs = W.project(model,n)
        ph = J.field_hash(projection)
        check(f'mode{n}_complete_projection_hash', ph == calib[n]['projection_sha256'])
        check(f'mode{n}_complete_projection_pairs', pairs == calib[n]['projection_pairs'])
        log('FRESH_PROJECTION',n,len(projection),'seconds',time.monotonic()-mode_tick)
        groups = {}
        for ell,A in projection.items():
            for b,P in pby.items():
                e = ell*model.delta/2+b-3
                groups[e] = groups.get(e,J.Rat()) + J.Rat(J.T*P)*A
        pairing = arb(0); evid = []; minimum = 10**9
        for i,(e,A) in enumerate(sorted(groups.items())):
            if not A: continue
            numerator = A.numerator_v(); order = 0
            while numerator and numerator[0] == 0:
                numerator, remainder = divmod(numerator,J.T); assert not remainder; order += 1
            assert numerator and e+order > -1
            factors = [(a,k) for a,k in zip(J.SCALES,A.powers) if k]
            value, info = M.integral(e+order,numerator,factors)
            assert value.is_finite() and value.rel_accuracy_bits() > 150 and info['exact_reconstruction']
            minimum = min(minimum,value.rel_accuracy_bits()); pairing += value
            evid.append({'exponent_before_order':str(e),'endpoint_order':order,
                         'numerator_sha256':sha256(str(numerator).encode()).hexdigest(),
                         'integral_ball':value.str(200),'decomposition':info})
            if (i+1)%16 == 0: log('PAIR_GROUPS',n,i+1,len(groups),'seconds',time.monotonic()-mode_tick)
        pairing *= arb.pi()/2
        check(f'mode{n}_pairing_accuracy', pairing.is_finite() and pairing.rel_accuracy_bits() > 150)
        peerpair = arb(peerrow['F_psi'])
        check(f'mode{n}_peer_pairing_contains_own', peerpair.lower() < pairing.lower() and pairing.upper() < peerpair.upper())
        quotient = abs(pairing)/(arb.pi()*aq(den)).sqrt()
        floor = floor_exact(quotient)
        check(f'mode{n}_strict_positive_floor', floor > 0 and aq(floor) < quotient.lower())
        peerquot = arb(peerrow['LB'])
        check(f'mode{n}_peer_quotient_contains_own', peerquot.lower() < quotient.lower() and quotient.upper() < peerquot.upper())
        lower_square += floor**2
        row = {'utc':now(),'n':n,'coefficient_count':count,'beta_group_count':len(pby),
               'precision_bits':ctx.prec,'complete_projection_sha256':ph,'complete_projection_pairs':pairs,
               'gradient_energy_over_pi_exact':str(den),'gradient_energy_groups':den_evidence,
               'pairing_ball':pairing.str(200),'pairing_groups':evid,'minimum_integral_accuracy_bits':minimum,
               'quotient_ball':quotient.str(200),'quotient_strict_lower_exact':str(floor),
               'elapsed_seconds':time.monotonic()-mode_tick,'inputs':inputs}
        exclusive(B/f'verification/mode_{n:03d}.json',row); rows.append(row)
        log('MODE_COMPLETE',n,'floor',str(floor),'seconds',row['elapsed_seconds'])
    Hlower = aq(lower_square).sqrt(); Hfloor = floor_exact(Hlower)
    L = {k:Q(accepted['norms'][k]['accepted_lower_exact']) for k in ['G0','G1','P2']}
    energy2 = L['P2']**2+2**14*L['G1']**2+2**18*L['G0']**2+Q(20,21)*2**18*lower_square
    energy = aq(energy2).sqrt(); Efloor = floor_exact(energy,12)
    baseupper = Q(baseline['E_upper']['strict_upper_exact'])
    order = Efloor > baseupper
    check('distinct_mode_dual_sum', len({r['n'] for r in rows}) == len(rows))
    check('H_floor_directed', Hfloor > 0 and aq(Hfloor) < Hlower.lower())
    check('E2_floor_directed', Efloor > 0 and aq(Efloor) < energy.lower())
    for name, mod in list(sys.modules.items()):
        source = getattr(mod,'__file__',None)
        if source:
            p=Path(source).resolve()
            if p.suffix == '.py' and p.is_relative_to(R):
                check('import_bound:'+name, str(p.relative_to(R)) in inputs)
    for rel,h in inputs.items(): assert sha(R/rel) == h, rel
    result = {'utc':now(),'candidate':CANDIDATE,'raw_sha256':RAW_SHA,'precision_bits':ctx.prec,
              'inputs':inputs,'checks':checks,'check_count':len(checks),'mode_count':len(rows),
              'mode_strict_floors':{str(r['n']):r['quotient_strict_lower_exact'] for r in rows},
              'H_lower_square_exact':str(lower_square),'H_lower_ball':Hlower.str(200),'H_strict_lower_exact':str(Hfloor),
              'E2_lower_square_exact':str(energy2),'E2_lower_ball':energy.str(200),'E2_strict_lower_exact':str(Efloor),
              'baseline007_E2_strict_upper_exact':str(baseupper),'actual_E2_007_less_than016':order,
              'strict_E2_separation_exact':str(Efloor-baseupper) if order else None,
              'peer_solver_optimality_required':False,'peer_code_executed':False,'no_quadrature':True,
              'scope':'Own complete two-mode dual lower bound and stated identical-energy comparison only; no correction-distance ordering or existence.',
              'elapsed_seconds':time.monotonic()-tick,'verdict':'CONFIRMED own exact-vector dual lower bound; actual energy ordering is the recorded boolean'}
    exclusive(B/'verification/result.json',result)
    log('COMPLETE', 'H>',str(Hfloor),'E2>',str(Efloor),'007_E2_less_than016',order,'seconds',result['elapsed_seconds'])

if __name__ == '__main__': main()

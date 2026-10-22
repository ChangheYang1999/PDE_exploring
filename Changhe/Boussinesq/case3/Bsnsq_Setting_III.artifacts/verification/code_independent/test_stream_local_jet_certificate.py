"""Independent exact polynomial controls of packet118, not mirrored formulas."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import copy, hashlib, json, random, time
from stream_local_jet_certificate import checks, make, verify, parse
import exact_bivariate as P

start = time.monotonic()
root = Path('research/118_exact_local_stream_residual/verification')
root.mkdir(exist_ok=True)
rng = random.Random(421118)
rows = []
for beta in [Q(21,10), Q(5,2), Q(3), Q(4), Q(9)]:
    labels = [(i, j, d) for d in (0, 1) for i in range(4) for j in range(6)]
    cases = []
    # Each basis separately and three mixed streams/temperatures.
    for key in [0, 1, 6, 9, 19, 26, 29, 40, 47]:
        cs, ds = [Q(0)]*len(labels), [Q(0)]*len(labels)
        cs[key], ds[key] = Q(3,7), Q(-2,11)
        cases.append((cs, ds))
    for k in range(3):
        cases.append(([Q(rng.randint(-4,4),13) for _ in labels],
                      [Q(rng.randint(-4,4),17) for _ in labels]))
    for number, (C,D) in enumerate(cases):
        data = {'beta': str(beta), 'labels': list(map(list, labels)),
                'C': list(map(str, C)), 'D': list(map(str, D))}
        ck = checks(data)
        psi, theta = P.ordinary_stream_jet(beta, labels, C, D, 4)
        ft, go = P.pde(beta, psi, theta, 4)
        for name, residual in [('f0',ft),('f1',ft),('g0',go),('g1',go)]:
            computed = residual.get(tuple(ck['monomials'][name]),Q(0))
            assert computed == Q(ck['residual_coefficients'][name]), (beta,number,name)
        omega = P.scale(P.lap(psi), -1)
        direct = {'a0': theta.get((2,0),0), 'a1': theta.get((2,1),0),
                  'c0': psi.get((1,1),0), 'c1': 2*psi.get((1,2),0),
                  'b0': omega.get((1,0),0), 'b1': omega.get((1,1),0)}
        assert all(v == Q(ck['moments'][k]) for k,v in direct.items())
        rows.append({'beta':str(beta),'case':number,'exact_moments_and_residuals':True})
# Full polynomial PDE control, deliberately not an admissible slow-tail field.
controls=[]
for beta,a0 in [(Q(5,2),Q(1)),(Q(4),Q(-2)),(Q(9),Q(3,7))]:
    c0,b0=1+beta/2,4*a0/beta
    psi={(1,1):c0,(3,0):-b0/6};theta={(2,0):a0}
    ft,go=P.pde(beta,psi,theta,8)
    assert not ft and not go
    controls.append({'beta':str(beta),'a0':str(a0),'both_polynomial_residuals_zero':True,
                     'outside_class':'velocity quadratic; vorticity linear'})
# Strict parsing and certificate reload/tamper rejection.
path=root/'manufactured_input.json';path.write_text(json.dumps(data,indent=2)+'\n')
certpath=root/'manufactured_certificate.json';make(path,certpath);assert verify(path,certpath)
rejects=[]
for name,mutate in [
    ('length',lambda d:d['C'].pop()),
    ('duplicate',lambda d:d['labels'].__setitem__(1,d['labels'][0])),
    ('shift',lambda d:d['labels'].__setitem__(1,[0,1,2])),
    ('boolean_index',lambda d:d['labels'].__setitem__(1,[False,1,0])),
    ('beta',lambda d:d.__setitem__('beta','2'))]:
    bad=copy.deepcopy(data);mutate(bad)
    try:parse(bad)
    except ValueError:rejects.append(name)
    else:raise AssertionError(name)
cert=json.loads(certpath.read_text());cert['residual_coefficients']['f1']=str(Q(cert['residual_coefficients']['f1'])+1)
badpath=root/'tampered_certificate.json';badpath.write_text(json.dumps(cert)+'\n')
try:verify(path,badpath)
except ValueError:rejects.append('certificate_value')
else:raise AssertionError('tampered certificate accepted')
cert=json.loads(certpath.read_text());cert['source_sha256']='0'*64
badpath.write_text(json.dumps(cert)+'\n')
try:verify(path,badpath)
except ValueError:rejects.append('input_digest')
else:raise AssertionError('tampered digest accepted')
badpath.unlink()
out={'created_utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED',
     'elapsed_seconds':time.monotonic()-start,'exact_cases':rows,'polynomial_controls':controls,
     'rejections':rejects,'code_hashes':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in
       [Path(__file__),Path(__file__).with_name('stream_local_jet_certificate.py'),
        Path(__file__).with_name('exact_bivariate.py')]}}
(root/'tests.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'elapsed_seconds':out['elapsed_seconds'],
                  'exact_cases':len(rows),'polynomial_controls':len(controls),'rejections':rejects},indent=2))

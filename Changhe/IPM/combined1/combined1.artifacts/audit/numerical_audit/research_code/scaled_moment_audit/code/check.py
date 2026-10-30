"""Independent analytic fixtures for the copied finite-scale moment engine."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
from math import factorial
import importlib.util,json,time
from flint import fmpq as Q,arb,ctx
BASE=Path(__file__).resolve().parents[1]
path=BASE/'source/T4_moments.py'
spec=importlib.util.spec_from_file_location('frozen_moments',path)
engine=importlib.util.module_from_spec(spec);spec.loader.exec_module(engine)
ar=engine.ar
def digest(p):return sha256(p.read_bytes()).hexdigest()
def halfbeta(m,n):
    return arb.pi()*ar(Q(factorial(2*m)*factorial(2*n),
        4**(m+n)*factorial(m)*factorial(n)*factorial(m+n)))
def exact_original(case):
    label=case['exact'];factors=[(Q(z),Q(nu)) for z,nu in case['factors']]
    if label=='single_elementary':
        z,nu=factors[0]
        if nu==1:return -(1-ar(z)).log()/ar(z)
        return (1-ar(1-z)**ar(1-nu))/ar(z*(1-nu))
    if label=='two_logs':
        (z,_),(w,_)=factors
        return ((1-ar(w)).log()-(1-ar(z)).log())/ar(z-w)
    return ar(Q(label))
def run():
    start=time.monotonic();ctx.prec=1024;N=224
    old=json.loads((BASE/'source/T4_results.json').read_text())
    assert old['proof_sha256']==digest(BASE/'source/T4_PROOF.md')
    assert old['code_sha256']==digest(path)
    assert old['check_sha256']==digest(BASE/'source/T4_check.py')
    assert old['input_sha256']==digest(BASE/'source/T4_manufactured.json')
    original=json.loads((BASE/'source/T4_manufactured.json').read_text())['cases']
    fixtures=[]
    for case in original:
        fixtures.append((case['name'],Q(case['alpha']),Q(case['beta']),
                         [(Q(z),Q(nu)) for z,nu in case['factors']],
                         exact_original(case)))
    z,w=Q(255,256),Q(3,4)
    J=lambda z:arb.pi()/ar(1-z).sqrt()
    fixtures.extend([
        ('arcsine_pole',Q(-1,2),Q(-1,2),[(z,Q(1))],J(z)),
        ('arcsine_double_pole',Q(-1,2),Q(-1,2),[(z,Q(2))],
         arb.pi()*ar(2-z)/(2*ar(1-z)**ar(Q(3,2)))),
        ('arcsine_two_scales',Q(-1,2),Q(-1,2),[(z,Q(1)),(w,Q(1))],
         (ar(z)*J(z)-ar(w)*J(w))/ar(z-w)),
        ('half_beta_polynomial',Q(1,2),Q(3,2),[(Q(1,3),Q(-2))],
         halfbeta(1,2)-ar(Q(2,3))*halfbeta(2,2)+ar(Q(1,9))*halfbeta(3,2)),
        ('near_integrability_endpoint',Q(-999,1000),Q(0),[],arb(1000)),
    ])
    rows=[]
    for name,alpha,beta,factors,target in fixtures:
        tick=time.monotonic()
        value,details=engine.integral(alpha,beta,factors,N)
        assert value.contains(target),(name,value,target)
        for cell in details:
            assert all(abs(Q(q))<=Q(1,2) for q,e in cell['analytic_factors'])
            assert Q(cell['error_upper_exact'])>=0
        assert details[0]['interval'][0]=='0' and details[-1]['interval'][1]=='1'
        assert all(x['interval'][1]==y['interval'][0] for x,y in zip(details,details[1:]))
        prior=next((r for r in old['cases'] if r['name']==name),None)
        overlaps=bool(value.overlaps(arb(prior['enclosure']))) if prior else None
        assert overlaps is not False
        rows.append({'name':name,'alpha':str(alpha),'beta':str(beta),
                     'factors':[[str(z),str(nu)] for z,nu in factors],
                     'enclosure':value.str(90),'independent_closed_form':target.str(90),
                     'contains_closed_form':True,'peer_interval_overlap':overlaps,
                     'relative_radius':(value.rad()/abs(target)).str(30),
                     'partition_cells':len(details),'elapsed_seconds':time.monotonic()-tick})
        print(name,'passed',value.str(28),flush=True)
    out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
         'degree':N,'precision_bits':ctx.prec,'proof_sha256':digest(BASE/'PROOF.md'),
         'checker_sha256':digest(Path(__file__)),'copied_engine_sha256':digest(path),
         'peer_result_sha256':digest(BASE/'source/T4_results.json'),'rows':rows,
         'elapsed_seconds':time.monotonic()-start}
    dest=BASE/'verification/results.json';assert not dest.exists()
    dest.write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run()

"""Exact affine Taylor lift and whole-plane perturbation estimate for frozen007."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
from hashlib import sha256
from datetime import datetime, timezone
import importlib.util, json, sys, time
from flint import arb, ctx
sys.set_int_max_str_digits(0)
ctx.prec=512
BASE=Path(__file__).resolve().parents[1]
ROOT=BASE.parents[1]
H=lambda p:sha256(Path(p).read_bytes()).hexdigest()
JPATH=ROOT/'research/taylor_projection/code/jets.py'
spec=importlib.util.spec_from_file_location('own_jets',JPATH)
J=importlib.util.module_from_spec(spec);spec.loader.exec_module(J)

def main():
    start=time.monotonic(); stamp=datetime.now(timezone.utc).isoformat()
    rawpath=ROOT/'research/taylor_projection/source/canonical007.json'
    parpath=ROOT/'research/taylor_projection/verification/parameters.json'
    normpath=ROOT/'research/taylor_projection/verification/result.json'
    membpath=ROOT/'research/taylor_projection/source/constraint_result.json'
    raw=json.loads(rawpath.read_text());par=json.loads(parpath.read_text())
    norms=json.loads(normpath.read_text());memb=json.loads(membpath.read_text())
    assert par['source_canonical_sha256']==H(rawpath)
    assert norms['parameters_file_sha256']==H(parpath)
    c=Q(raw['cl']);assert c==J.c and c>1
    phi=J.add(*(J.scale(J.canonical_jet(*idx),Q(v)) for idx,v in zip(raw['order'],raw['coefficients']) if idx[2]<=4))
    eta=J.add(*(J.scale(J.canonical_jet(*x['index']),Q(x['coefficient'])) for x in par['canonical_changes'] if x['index'][2]<=4))
    ts={tuple(x['pair']):Q(x['coefficient']) for x in par['parameters']}
    alpha,beta=ts[2,1],ts[0,3]
    a=J.fields(phi)[0][0,0];K=60*(a-8*c+4)
    assert a-4*c+2 and K and alpha
    corr={(3,1):-192*alpha**2/K,(1,3):18*alpha*beta/c}
    corr[0,4]=(a-4)*corr[1,3]/112
    # These three directions start at degree eight, so their jets are monomials.
    tau={ij:t for ij,t in corr.items() if t}
    z=J.add(eta,tau)
    defect={(2,0):192*alpha**2,(1,1):8640*alpha*beta}
    assert J.add(J.residual(phi),J.linear(phi,eta))==defect
    assert J.linear(phi,tau)==J.scale(defect,-1)
    assert J.add(J.residual(phi),J.linear(phi,z))=={}
    assert J.residual(J.add(phi,z))==J.scale(defect,-1)
    assert J.residual(J.add(phi,eta))=={}
    # Construct all frozen canonical changes independently from membership rows.
    tau_changes=defaultdict(Q)
    for ij,t in corr.items():
        rows=next(row['membership'] for row in memb['directions'] if (row['a'],row['b'])==ij)
        for row in rows:
            m=int(row['m'])
            for w,v in row['polynomial'].items():tau_changes[0,m,m+int(w)]+=t*Q(v)
    tau_changes={k:v for k,v in tau_changes.items() if v}
    own_order={tuple(x) for x in raw['order']}
    assert set(tau_changes)<=own_order
    tau_canonical=J.add(*(J.scale(J.canonical_jet(*idx),v) for idx,v in tau_changes.items() if idx[2]<=4))
    assert tau_canonical==tau
    z_changes=defaultdict(Q,tau_changes)
    for x in par['canonical_changes']:z_changes[tuple(x['index'])]+=Q(x['coefficient'])
    z_changes={k:v for k,v in z_changes.items() if v}
    z_canonical=J.add(*(J.scale(J.canonical_jet(*idx),v) for idx,v in z_changes.items() if idx[2]<=4))
    assert z_canonical==z
    p=(3+1/c)/2
    for changes in [tau_changes,z_changes]:
        assert set(changes)<=own_order
        for m in {idx[1] for idx in changes}:
            vals=[(idx[2],v) for idx,v in changes.items() if idx[1]==m]
            assert sum((v for k,v in vals),Q(0))==0
            assert sum(((p-k)*v for k,v in vals),Q(0))==0
    original_origin=[f.get((0,0),Q(0)) for f in J.fields(phi)]
    assert original_origin[0]==Q(raw['a0'])
    assert original_origin[2]==1-c
    for h in [tau,z]:
        assert [f.get((0,0),Q(0)) for f in J.fields(J.add(phi,h))]==original_origin
    def ar(q):return arb(q.numerator)/arb(q.denominator)
    bn={tuple(x['pair']):(arb.pi()*ar(Q(x['squared_L2_over_pi']))).sqrt() for x in norms['direction_norms']}
    tau_bound=sum((ar(abs(t))*bn[ij] for ij,t in corr.items()),arb(0))
    z_bound=sum((ar(abs(ts[ij]+corr.get(ij,Q(0))))*bn[ij] for ij in ts),arb(0))
    assert tau_bound<arb('1e-24') and z_bound<arb('3.424e-12')
    pars={'format':'Exact affine Taylor lift in the frozen007 span, not a registered candidate',
          'source_canonical_sha256':H(rawpath),'nonlinear_repair_parameters_sha256':H(parpath),
          'c':str(c),'a0':str(a),
          'tau_parameters':[{'pair':list(ij),'coefficient':str(t),'ball':ar(t).str(65)} for ij,t in corr.items()],
          'affine_parameters':[{'pair':list(ij),'coefficient':str(t+corr.get(ij,Q(0)))} for ij,t in ts.items()],
          'canonical_tau_changes':[{'index':list(k),'coefficient':str(v)} for k,v in sorted(tau_changes.items())],
          'canonical_affine_changes':[{'index':list(k),'coefficient':str(v)} for k,v in sorted(z_changes.items())]}
    parout=BASE/'verification/parameters.json'
    with parout.open('x') as f:json.dump(pars,f,indent=2);f.write('\n')
    out={'start_utc':stamp,'finish_utc':datetime.now(timezone.utc).isoformat(),
         'elapsed_seconds':time.monotonic()-start,'proof_sha256':H(BASE/'PROOF.md'),'code_sha256':H(__file__),
         'input_sha256':{str(p.relative_to(ROOT)):H(p) for p in [rawpath,parpath,normpath,membpath,JPATH]},
         'parameters_sha256':H(parout),'five_affine_constraints_exactly_zero':True,
         'five_nonlinear_constraints_equal_negative_defect':True,
         'canonical_reconstruction_matches':True,'tail_rows_exactly_preserved':True,
         'origin_slope_and_strain_exactly_preserved':True,'canonical_tau_nonzero_coordinates':len(tau_changes),
         'tau_density_L2_upper_bound_ball':tau_bound.str(90),'strict_tau_density_L2_upper_bound':'1e-24',
         'affine_density_L2_upper_bound_ball':z_bound.str(90),'strict_affine_density_L2_upper_bound':'3.424e-12',
         'status':'Exact checks pass locally. OPEN independent Opus theorem review and numerical reproduction.'}
    with (BASE/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps(out,indent=2))
    print('tau parameter balls',[x['ball'] for x in pars['tau_parameters']])
if __name__=='__main__':main()

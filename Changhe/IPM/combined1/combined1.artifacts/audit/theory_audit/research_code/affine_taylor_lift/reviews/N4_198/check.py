"""Independent Cartesian reconstruction of the affine Taylor correction."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import importlib.util,json,sys,time
from flint import fmpq as Q,arb,ctx
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/affine_taylor_lift_audit'
H=lambda p:sha256(Path(p).read_bytes()).hexdigest()
spec=importlib.util.spec_from_file_location('n4_affine_cartesian',ROOT/'research/constraint_rank/code/check.py')
J=importlib.util.module_from_spec(spec);spec.loader.exec_module(J)
PAIRS=[(2,1),(0,3),(3,1),(1,3),(0,4)]
def ar(q):return arb(q.numerator)/arb(q.denominator)

def run():
    start=time.monotonic();ctx.prec=768
    manifest=json.loads((BASE/'source/MANIFEST.json').read_text())
    for name,row in manifest['files'].items():assert H(BASE/'source'/name)==row['sha256']
    peer=json.loads((BASE/'source/T4_result.json').read_text())
    pp=json.loads((BASE/'source/T4_parameters.json').read_text())
    assert peer['parameters_sha256']==H(BASE/'source/T4_parameters.json')
    assert peer['proof_sha256']==H(BASE/'source/T4_PROOF.md') and peer['code_sha256']==H(BASE/'source/T4_check.py')
    rawpath=ROOT/'research/candidate_audits/data/C1-N1-007-d2w-j7-e2bal/canonical.json'
    ep=ROOT/'research/taylor_repair_audit/verification/exact.json'
    np=ROOT/'research/taylor_repair_audit/verification/result.json'
    cp=ROOT/'research/constraint_rank/verification/candidate007.json'
    raw=json.loads(rawpath.read_text());exact=json.loads(ep.read_text());norms=json.loads(np.read_text());old=json.loads(cp.read_text())
    assert H(rawpath)==pp['source_canonical_sha256']
    assert norms['exact_result_sha256']==H(ep)
    c=Q(raw['cl']);p=(3+1/c)/2;assert c>1 and Q(exact['c'])==c
    coeff={tuple(k):Q(v) for k,v in zip(raw['order'],raw['coefficients'],strict=True)}
    chi=J.add(*(J.scale(J.monojet(*key,c),v) for key,v in coeff.items() if key[2]<=4))
    a=J.fields(chi)[0][0,1];K=60*(a-8*c+4)
    assert a==Q(old['a0_exact']) and 4*chi[2,2]==1-c and a-4*c+2 and K
    ts={tuple(row['pair']):Q(row['coefficient']) for row in exact['parameters']}
    assert list(ts)==PAIRS
    directions={}
    for i,j in PAIRS:
        directions[i,j]=J.add(*(J.scale(J.mul({(2*i,2*j):Q(1)},J.spow(n)),J.binomial(p-i-j-2,n)) for n in range(5-i-j)))
    eta=J.add(*(J.scale(directions[ij],q) for ij,q in ts.items()))
    alpha,beta=ts[2,1],ts[0,3];assert alpha
    correction={(3,1):-192*alpha**2/K,(1,3):18*alpha*beta/c}
    correction[0,4]=(a-4)*correction[1,3]/112
    tau=J.add(*(J.scale(directions[ij],q) for ij,q in correction.items()))
    z=J.add(eta,tau)
    defect={(4,1):-192*alpha**2,(2,3):-8640*alpha*beta}
    defect={k:v for k,v in defect.items() if v}
    assert J.residual(J.add(chi,eta),c)=={}
    assert J.add(J.residual(chi,c),J.linearized(chi,eta,c))==J.scale(defect,-1)
    assert J.linearized(chi,tau,c)==defect
    assert J.add(J.residual(chi,c),J.linearized(chi,z,c))=={}
    assert J.residual(J.add(chi,z),c)==defect
    for direction in [eta,tau,z]:
        centered=J.scale(J.add(J.residual(J.add(chi,direction),c),J.scale(J.residual(J.add(chi,J.scale(direction,-1)),c),-1)),Q(1,2))
        assert centered==J.linearized(chi,direction,c)
        changed=J.add(chi,direction)
        assert J.fields(changed)[0][0,1]==a and 4*changed[2,2]==1-c
    changes={}
    for ij,t in correction.items():
        row=next(x for x in old['directions'] if (x['a'],x['b'])==ij)
        for entry in row['tail_polynomials']:
            m=int(entry['m'])
            for w,v in enumerate(entry['polynomial_coefficients']):
                key=(0,m,m+w);changes[key]=changes.get(key,Q(0))+t*Q(v)
    changes={k:v for k,v in changes.items() if v}
    affine=changes.copy()
    for row in exact['canonical_changes']:
        key=tuple(row['index']);affine[key]=affine.get(key,Q(0))+Q(row['coefficient'])
    affine={k:v for k,v in affine.items() if v}
    for correction_map,expected in [(changes,tau),(affine,z)]:
        assert set(correction_map)<=set(coeff)
        reconstructed=J.add(*(J.scale(J.monojet(*key,c),v) for key,v in correction_map.items() if key[2]<=4))
        assert reconstructed==expected
        for m in {k[1] for k in correction_map}:
            terms=[(k[2],v) for k,v in correction_map.items() if k[1]==m]
            assert sum((v for k,v in terms),Q(0))==0
            assert sum(((p-k)*v for k,v in terms),Q(0))==0
    assert correction=={tuple(row['pair']):Q(row['coefficient']) for row in pp['tau_parameters']}
    assert changes=={tuple(row['index']):Q(row['coefficient']) for row in pp['canonical_tau_changes']}
    assert affine=={tuple(row['index']):Q(row['coefficient']) for row in pp['canonical_affine_changes']}
    bn={tuple(row['pair']):(arb.pi()*ar(Q(row['squared_L2_over_pi']))).sqrt() for row in norms['direction_norms']}
    tau_bound=sum((ar(abs(t))*bn[ij] for ij,t in correction.items()),arb(0))
    z_bound=sum((ar(abs(t+correction.get(ij,Q(0))))*bn[ij] for ij,t in ts.items()),arb(0))
    assert tau_bound<ar(Q(1,10**24)) and z_bound<ar(Q(3424,10**15))
    assert tau_bound.overlaps(arb(peer['tau_density_L2_upper_bound_ball']))
    assert z_bound.overlaps(arb(peer['affine_density_L2_upper_bound_ball']))
    paths=[rawpath,ep,np,cp,Path(__file__),BASE/'PROOF.md',BASE/'source/MANIFEST.json',ROOT/'research/constraint_rank/code/check.py']
    out={'utc':datetime.now(timezone.utc).isoformat(),'inputs':{str(p.relative_to(ROOT)):H(p) for p in paths},
         'all_five_affine_constraints_zero':True,'nonlinear_residual_equals_quadratic_defect':True,
         'all_centered_differential_checks':True,'origin_slope_and_strain_preserved':True,
         'both_tail_moments_preserved':True,'all_exact_parameters_and_canonical_coordinates_equal_peer':True,
         'canonical_tau_nonzero_coordinates':len(changes),'canonical_affine_nonzero_coordinates':len(affine),
         'tau_density_L2_upper_bound_ball':tau_bound.str(100),'strict_tau_upper_exact':'1/1000000000000000000000000',
         'affine_density_L2_upper_bound_ball':z_bound.str(100),'strict_affine_upper_exact':'428/125000000000000',
         'tau_parameters':[{'pair':list(k),'coefficient':str(v),'ball':ar(v).str(70)} for k,v in correction.items()],
         'nonlinear_defect':[{'index':list(k),'coefficient':str(v),'ball':ar(v).str(70)} for k,v in defect.items()],
         'elapsed_seconds':time.monotonic()-start,'status':'CONFIRMED independent T4-251 candidate arithmetic; general theorem review separate'}
    with (BASE/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps({k:out[k] for k in ['utc','tau_density_L2_upper_bound_ball','affine_density_L2_upper_bound_ball','elapsed_seconds','status']},indent=2))
if __name__=='__main__':run()

"""Exact reconstruction of the retained kernel and rational damping fixture."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time
from flint import fmpq as Q,fmpq_poly as P
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/constraint_nullity_audit'
def H(p):return sha256(Path(p).read_bytes()).hexdigest()
def main():
    start=time.monotonic();src=BASE/'source'
    manifest=json.loads((src/'MANIFEST.json').read_text())
    for name,row in manifest['files'].items():assert H(src/name)==row['sha256']
    rawpath=ROOT/'research/basis_redundancy/source/candidate007.json'
    relpath=ROOT/'research/basis_redundancy/verification/candidate007_kernel_relations.json'
    rankpath=ROOT/'research/basis_redundancy/verification/candidate007.json'
    ownpath=ROOT/'research/constraint_rank/verification/candidate007.json'
    peerpath=ROOT/'research/constraint_rank/reviews/T4_209/result.json'
    raw=json.loads(rawpath.read_text());rel=json.loads(relpath.read_text());rank=json.loads(rankpath.read_text())
    own=json.loads(ownpath.read_text());peer=json.loads(peerpath.read_text())
    assert H(rawpath)==rank['source_sha256'] and H(relpath)==rank['relations_sha256']
    t=P([0,1]);z=2*t-1;legs=[P([1]),z]
    for n in range(1,max(int(g['spec'][2]) for g in raw['generators'] if g['spec'][0]=='leg')):legs.append(((2*n+1)*z*legs[-1]-n*legs[-2])/Q(n+1))
    pol=[]
    for g in raw['generators']:
        spec=g['spec'];w=int(spec[1]);assert spec[0] in ['mono','leg']
        pol.append(t**w if spec[0]=='mono' else t**w*legs[int(spec[2])])
    pivots={int(r['unit_nonpivot_index']) for r in rel['relations']};assert len(pivots)==len(rel['relations'])==1060
    for row in rel['relations']:
        coeff={int(k):Q(v) for k,v in row['coefficients'].items()}
        pivot=int(row['unit_nonpivot_index']);assert coeff[pivot]==1 and (set(coeff)&pivots)=={pivot}
        assert all((raw['generators'][k]['j'],raw['generators'][k]['m'])==(row['j'],row['m']) for k in coeff)
        total=sum((v*pol[k] for k,v in coeff.items()),P([]))
        assert not total and total(Q(1))==0 and total.derivative()(Q(1))==0
    assert rank['generators']==2982 and rank['potential_space_dimension']==1922 and rank['exact_zero_potential_dimension']==1060
    assert own['full_constraint_rank']==peer['full_differential_rank']==426
    assert own['constrained_generator_tangent_dimension']==peer['coefficient_tangent_dimension']==2556
    assert own['constrained_potential_tangent_dimension']==peer['potential_tangent_dimension']==1496
    assert 2556==1496+1060 and 2982-426==2556
    lam=Q(1);one=1/(1+lam);a=b=1/(2+lam);two=a+b
    assert (1+lam)*one==1 and (1+lam)*a+b==1 and a+(1+lam)*b==1
    assert two-one==lam/((1+lam)*(2+lam))>0
    spectrum=json.loads((src/'N1_spectrum.json').read_text())
    assert spectrum['constraint_rank']==426 and spectrum['reduced_dim']==2556
    paths=[rawpath,relpath,rankpath,ownpath,peerpath,src/'MANIFEST.json',BASE/'PROOF.md',Path(__file__)]
    out={'utc':datetime.now(timezone.utc).isoformat(),'inputs':{str(p.relative_to(ROOT)):H(p) for p in paths},
         'zero_polynomials_verified':1060,'unit_nonpivot_independence_checked':True,
         'tail_value_and_derivative_zero':True,'potential_rank':1922,'coefficient_dimension':2982,
         'constraint_rank':426,'physical_tangent_dimension':1496,'coefficient_tangent_dimension':2556,
         'retained_exact_kernel_dimension':1060,'absorbed_exact_kernel_dimension':0,
         'damping_fixture':{'lambda':str(lam),'one_coordinate_physical_step':str(one),
                           'duplicate_coordinate_physical_step':str(two),'difference':str(two-one),
                           'both_normal_equations_verified':True},
         'elapsed_seconds':time.monotonic()-start,
         'verdict':'REFUTED exact absorption of38 zero-potential directions; regularization alone does not prove redundancy irrelevant to a physical step'}
    with (BASE/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='inputs'},indent=2),flush=True)
if __name__=='__main__':main()

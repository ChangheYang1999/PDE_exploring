"""Exact witnesses for the abstract two-scale space, not an unregistered snapshot."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import comb
from flint import fmpq as Q
import importlib.util,json,sys,time
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/joint_scaled_density_rank'
sys.set_int_max_str_digits(0)
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def write(p,d):
 with p.open('x') as f:json.dump(d,f,indent=2);f.write('\n')
def main():
 start=time.monotonic();inputs={}
 def bind(p,h=None):
  p=Path(p);actual=sha(p);assert h is None or h==actual,(str(p),h,actual);inputs[str(p.relative_to(ROOT))]=actual;return p
 def read(p):return json.loads(bind(p).read_text())
 prep=read(B/'verification/PREPARE.json');bind(B/'PROOF.md',prep['proof_sha256']);bind(Path(__file__))
 rank=read(ROOT/'research/scaled_rank_peer/verification/result.json');density=read(ROOT/'research/scaled_density_injectivity/verification/result.json')
 for d in [rank,density]:
  for p,h in d['inputs'].items():bind(ROOT/p,h)
 for p,d in rank['frozen_sources'].items():bind(ROOT/p,d['stored_sha256'])
 assert rank['verdict'].startswith('CONFIRMED') and density['verdict'].startswith('CONFIRMED')
 assert density['own_rank_dependency_sha256']==sha(ROOT/'research/scaled_rank_peer/verification/result.json')
 old=read(ROOT/'research/optimizer_quotient_audit/source/N1_013_quot_exact.json')
 oldaudit=read(ROOT/'research/optimizer_quotient_audit/verification/result.json')
 for p,h in oldaudit['inputs'].items():bind(ROOT/p,h)
 row=next(r for r in oldaudit['rows'] if r['candidate']=='C1-N1-013-pairU-from007')
 assert row['selected_columns']==1922 and row['nonpivot_relations']==0 and sum(b['rank'] for b in row['blocks'])==1922 and row['all_canonical_coefficients_equal'] and row['selected_original_shapes_match']
 shape=lambda g:(g['j'],g['m'],tuple(g['spec']))
 oldshapes=list(map(shape,old['generators']));assert len(oldshapes)==len(set(oldshapes))==1922
 new=[(j,m,('legqs',0,N,4,R)) for R in [25,50] for j in [1,2,3] for m in range(9,16) for N in range(12)]
 shapes=oldshapes+new;assert len(new)==504 and len(shapes)==len(set(shapes))==2426
 c=Q(4076476460239181,2251799813685248);gamma=1/c;delta=1-gamma;ps=[(3+gamma-j*delta)/2 for j in range(8)]
 assert list(map(str,ps))==rank['p_j']==density['branch_exponents'] and all(p.denominator!=1 for p in ps)
 differences=[ps[j]-ps[k] for j in range(8) for k in range(j+1,8)]
 assert all(q.denominator!=1 for q in differences) and list(map(str,differences))==rank['noninteger_differences']==density['branch_differences']
 assert 3+gamma<4 and gamma-1<0 and 2*ps[0]==3+gamma
 backend=bind(ROOT/'research/joint_scaled_factored_weak/code/fields_joint.py')
 spec=importlib.util.spec_from_file_location('n4_two_pole_fields',backend);F=importlib.util.module_from_spec(spec);spec.loader.exec_module(F)
 witnesses=[];cross=[]
 for R,Rother in [(25,50),(50,25)]:
  a=Q(R*R-1);aother=Q(Rother*Rother-1);v0=-1/a;t0=1-v0;nonzero=1-aother/a
  assert nonzero!=0;cross.append({'scale':R,'other_scale':Rother,'pole_v_exact':str(v0),'other_denominator_at_pole_exact':str(nonzero),'other_scale_analytic':True})
  r=next(x for x in rank['rows'] if x['scale']==R);peer={(x['m'],x['N']):x for x in r['pole_witnesses']};assert len(peer)==84
  for m in range(9,16):
   for N in range(12):
    A=F.generator(m,['legqs',0,N,4,R]);want=tuple(4+N if q==a else 0 for q in F.SCALES);assert A.powers==want
    value=A.numerator_v()(v0)/a**(4+N)
    exact=Q(R)**8*v0**4*comb(2*N,N)*t0**(m+N)/a**(4+N)
    assert value==exact==Q(peer[m,N]['laurent_coefficient']) and value!=0
    witnesses.append({'scale':R,'m':m,'N':N,'pole_order':4+N,'Laurent_coefficient':str(value),'single_scale_accepted_witness_equal':True})
 shapep=B/'verification/abstract_shapes.json';write(shapep,{'c_exact':str(c),'old_count':1922,'new_count':504,'generators':[{'j':j,'m':m,'spec':list(spec)} for j,m,spec in shapes],'scope':'abstract basis, fitted coefficients and candidate match are not asserted'})
 inputs[str(shapep.relative_to(ROOT))]=sha(shapep)
 assert all(sha(ROOT/p)==h for p,h in inputs.items())
 out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'old_potential_rank':1922,'new_generators':504,'potential_dimension':2426,'density_dimension':2426,'abstract_shapes':2426,'actual_snapshot_match':None,'branch_exponents':list(map(str,ps)),'noninteger_differences':list(map(str,differences)),'growth_exponent':str(3+gamma),'fourth_derivative_exponent':str(gamma-1),'cross_pole_analyticity':cross,'Laurent_witnesses':witnesses,'inputs':inputs,'foreign_code_executed':False,'verdict':'OPEN independent review of two-scale potential independence and density injectivity; exact own finite hypotheses pass'}
 write(B/'verification/result.json',out);print(out['utc'],'JOINT_RANK',out['potential_dimension'],'witnesses',len(witnesses),'result',sha(B/'verification/result.json'),'seconds',out['elapsed_seconds'])
if __name__=='__main__':main()

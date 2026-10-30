from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import comb
from flint import fmpq as Q
import importlib.util,json,sys,time
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parents[3];B=R/'research/higher_mode_scaled_rank'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def write(p,d):
 with p.open('x') as f:json.dump(d,f,indent=2);f.write('\n')
def main():
 start=time.monotonic();inputs={}
 def bind(p,h=None):
  p=Path(p);actual=sha(p);assert h is None or h==actual,(p,h,actual);inputs[str(p.relative_to(R))]=actual;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 prep=read(B/'verification/PREPARE.json');bind(B/'PROOF.md',prep['proof_sha256']);bind(Path(__file__))
 accepted=read(R/'research/joint_scaled_rank_peer/verification/result.json','8652b3c60d9c857f04fd7ee25d93cb7f0739a6719a9934a6a329ef57c96eb8b7')
 for p,h in accepted['inputs'].items():bind(R/p,h)
 for d in accepted['frozen_sources'].values():bind(R/d['local'],d['stored_sha256'])
 density=read(R/'research/scaled_density_injectivity/verification/result.json')
 for p,h in density['inputs'].items():bind(R/p,h)
 assert density['verdict'].startswith('CONFIRMED')
 old=read(R/'research/optimizer_quotient_audit/source/N1_013_quot_exact.json')
 D=R/'research/candidate_audits/data/C1-N1-016-legqs25-quot013';mp=read(D/'MANIFEST.json');e=mp['coefficient_files'][0];parent=read(D/e['name'],e['sha256'])
 shape=lambda g:(g['j'],g['m'],tuple(g['spec']))
 oldshapes=list(map(shape,old['generators']));parents=list(map(shape,parent['generators']));present={(j,m) for j,m,sp in parents}
 assert len(oldshapes)==1922 and len(parents)==2174
 blocks=[(j,m) for j in range(1,4) for m in range(16,24) if (j,m) in present]
 expected=[(1,m) for m in range(16,20)]+[(j,m) for j in [2,3] for m in range(16,24)]
 assert blocks==expected and len(blocks)==20
 new=[(j,m,('legqs',0,N,4,25)) for j,m in blocks for N in range(12)]
 actual=parents+new;declared=oldshapes+[(j,m,('legqs',0,N,4,25)) for j in [1,2,3] for m in range(9,20 if j==1 else 24) for N in range(12)]
 assert set(actual)==set(declared) and len(actual)==len(set(actual))==len(declared)==2414 and len(new)==240
 source=bind(R/'research/expanded_objective_span/data/N1_chain022.sh').read_text()
 assert 'export IPM_ADD_LEGQS="1,2,3:16:23:25:12"' in source and 'unset IPM_ADD_LEGQS' in source
 desc=read(R/'research/expanded_objective_span/data/SOURCES.json');assert sha(R/'research/expanded_objective_span/data/N1_chain022.sh')==desc['files']['N1_chain022.sh']['sha256']
 c=Q(4076476460239181,2251799813685248);gamma=1/c;delta=1-gamma;ps=[(3+gamma-j*delta)/2 for j in range(8)]
 assert all(p.denominator!=1 for p in ps) and list(map(str,ps))==density['branch_exponents']
 differences=[ps[j]-ps[k] for j in range(8) for k in range(j+1,8)]
 assert all(q.denominator!=1 for q in differences) and list(map(str,differences))==density['branch_differences']
 assert 3+gamma<4 and gamma-1<0
 backend=bind(R/'research/joint_scaled_factored_weak/code/fields_joint.py');spec=importlib.util.spec_from_file_location('n4_higher_fields',backend);F=importlib.util.module_from_spec(spec);spec.loader.exec_module(F)
 a=Q(624);v0=-1/a;t0=1-v0;witnesses=[]
 for m in range(9,24):
  for N in range(12):
   A=F.generator(m,['legqs',0,N,4,25]);want=tuple(4+N if q==a else 0 for q in F.SCALES);assert A.powers==want
   value=A.numerator_v()(v0)/a**(4+N);formula=Q(625)**4*v0**4*comb(2*N,N)*t0**(m+N)/a**(4+N)
   assert value==formula and value!=0
   if m<=15:
    prior=next(x for x in accepted['witnesses'] if x['scale']==25 and x['m']==m and x['N']==N);assert value==Q(prior['coefficient'])
   witnesses.append({'m':m,'N':N,'pole_order':4+N,'coefficient':str(value),'exact_formula_equal':True,'old_independent_witness_equal':True if m<=15 else None})
 coefficient=4*33*32*(ps[1]-16-Q(4,625));assert coefficient!=0
 shapep=B/'verification/abstract_shapes.json';write(shapep,{'c_exact':str(c),'old_count':1922,'scaled_count':492,'increment_over016':240,'generators':[{'j':j,'m':m,'spec':list(sp)} for j,m,sp in actual],'scope':'Abstract proposed family, no fitted coefficients or actual candidate identity'});bind(shapep)
 out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'potential_dimension':2414,'density_dimension':2414,'actual_candidate_shape_match':None,'new_blocks':blocks,'new_functions':240,'all_scaled_blocks':41,'all_scaled_functions':492,'branch_exponents':list(map(str,ps)),'noninteger_differences':list(map(str,differences)),'growth_exponent':str(3+gamma),'fourth_derivative_exponent':str(gamma-1),'density_new_mode_support':list(range(31,48,2)),'density31_origin_coefficient':str(coefficient),'Laurent_witnesses':witnesses,'inputs':inputs,'publisher_code_executed':False,'verdict':'OPEN independent review of complete new finite-family rank proof; exact hypotheses and180Laurent witnesses PASS'}
 assert all(sha(R/p)==h for p,h in inputs.items());write(B/'verification/result.json',out);print(out['utc'],out['verdict'],sha(B/'verification/result.json'),out['elapsed_seconds'])
if __name__=='__main__':main()

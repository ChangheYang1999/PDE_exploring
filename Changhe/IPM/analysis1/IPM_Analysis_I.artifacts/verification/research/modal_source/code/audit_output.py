"""Exact rational audit of source manifest, bisection invariant and published comparisons."""
import json,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/modal_source/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def interval(v):return F(v['lower_exact']),F(v['upper_exact'])
def included(a,b):return b[0]<=a[0]<=a[1]<=b[1]
def dyad(v):return F.from_float(float(v))
respath=E/'source_result.json';res=json.loads(respath.read_text())
expected={'input_sha256':('data_exact/modal_v2.json','57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'),'scalar_input_sha256':('research/modal_repair/evidence/independent_gauss_iv.json','0985679510dfa1fbfceccddd19566d85452599c4b37ecde4c84adbd5aa5f0a2a'),'source_sha256':('research/modal_source/code/certify_source.py','8bb85cfaa0732810773c6770cbd10c2a079d1daad03aee1d0dfa7628a0c2206e'),'moments_sha256':('research/exponential_moments/code/moments.py','6f9aa03d5f7f4f2dff22e5bc8319a861148313e96d89991c16ee979dfdf0489c'),'Cox_sha256':('research/canonical_inverse/code/exact_audit.py','331771590a0dd764208306640b4b3af63aec8cfe966ed6a0d086ec512d617b42')}
for key,(path,h) in expected.items():assert res[key]==sha(BASE/path)==h,(key,path)
raw=json.loads((BASE/'data_exact/modal_v2.json').read_text());k=F.from_float(float.fromhex(raw['scalars_hex']['k']));t=[F.from_float(float.fromhex(v)) for v in raw['arrays']['knots']['hex']];tc=F(res['center_log_exact']);br=sorted(set(t)|{tc});M=raw['arrays']['S']['shape'][0];assert M==260 and len(br)-1==res['integration_cells']==1559
maxz=max((2*(M+1)+4)*(b-a) for a,b in zip(br[:-1],br[1:]));assert maxz<129
initial=res['initial_root_proof'][0];wa=interval(initial['w_a']);wb=interval(initial['w_b']);wp=interval(initial['wprime_on_box']);assert wa[1]<0<wb[0] and wp[0]>0
first=(F(initial['a_exact']),F(initial['b_exact']));final=tuple(map(F,res['final_root_endpoints_exact']));assert included(final,first);assert final[1]-final[0]==(first[1]-first[0])/2**28
vals=res['final_values'];assert included(final,interval(vals['xstar']));assert interval(vals['A_trial'])[0]>0
for name,value in [('cl',1/k),('sigma',3/k-1),('A_exact_solution_relation',2/k-1)]:assert included((value,value),interval(vals[name]))
num=BASE.parent/'ipmA-num/runs/scalars_full.json';numtext=num.read_text();r=json.loads(numtext);published={
 'xstar':(dyad(r['x_star_mid'])-dyad(r['x_star_rad']),dyad(r['x_star_mid'])+dyad(r['x_star_rad'])),
 'mu_minus_1':tuple(map(dyad,r['mu_minus_1'])),'g':tuple(map(dyad,r['g_star'])),'gprime':tuple(map(dyad,r['g_prime'])),
 'A_exact_solution_relation':tuple(map(dyad,r['A'])),'A_trial':tuple(map(dyad,r['A_tilde'])),'cl':tuple(map(dyad,r['c_l'])),'sigma':tuple(map(dyad,r['c']))}
checks=[]
for name,bounds in published.items():
 own=interval(vals[name]);assert included(own,bounds),(name,own,bounds)
 checks.append({'quantity':name,'verdict':'CONTAINED','published_lower_exact':str(bounds[0]),'published_upper_exact':str(bounds[1]),'independent_lower_exact':str(own[0]),'independent_upper_exact':str(own[1])})
(E/'published_scalars_snapshot.json').write_text(numtext)
out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','method':'Exact Fraction endpoint comparisons; all run/dependency hashes enforced against previously audited values; exact maximum moment argument; final bracket follows the independently reviewed point-sign bisection invariant','source_result_sha256':sha(respath),'audit_source_sha256':sha(__file__),'verified_dependencies':{key:h for key,(path,h) in expected.items()},'moment_hypothesis_max_abs_lambda_h_exact':str(maxz),'initial_signs_and_positive_derivative':True,'bisections_verified_by_exact_width':28,'published_scalars_sha256':sha(num),'comparisons':checks,'limits':'Does not validate the num-lane interval Newton derivative or other residual arithmetic. Confirms these published scalar intervals by independent density integration and bisection. Only one local root certified.'}
(E/'output_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='comparisons'},indent=2))

"""P253 exact last-cell coefficient/Parseval comparison, no NUM evaluator."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,hashlib,time,math
from r2_state_values import R2State
from exact_tail_residuals import COS,SIN,COS2,add,mul,scale,deriv,inv,chebs,linear,endpoints,ser
root=Path('research/253_k40_inverse_geometry_diagnostics/verification');beg=datetime.now(timezone.utc).isoformat();t0=time.monotonic();checks=[]
def check(name,ok,detail=None):checks.append({'name':name,'passed':bool(ok),'detail':detail})
def norm2(p):return sum(c[0]**2+c[1]**2 for c in p.values())
def norm(p):return math.sqrt(float(norm2(p)))
num=json.loads((root/'ffno_L2K40_b3085.json').read_text());st=R2State(root/Path(num['file']).name);b=Q.from_float(st.beta);s=1/b;m=1-2*s;k=2-s;L=Q.from_float(st.L)
fv,fd=endpoints(st,st.rawF);gv,gd=endpoints(st,st.rawG);basis=chebs(st.K)
H0=mul(COS2,linear(fv,basis));H1=mul(COS2,linear(fd,basis));A0=mul(COS,linear(gv,basis));A1=mul(COS,linear(gd,basis));P=inv(A0,k)
apred=add(scale(add(scale(mul(P,deriv(A0)),k),scale(mul(deriv(P),A0),s)),L),scale(mul(COS,H0),-m),mul(SIN,deriv(H0)))
bpred=scale(add(scale(mul(P,deriv(H0)),k),scale(mul(deriv(P),H0),-m)),L)
a2=scale(A1,-1);b2=scale(H1,-1);ae=add(a2,scale(apred,-1));be=add(b2,scale(bpred,-1))
check('source_archive_hash',st.sha256==next(x['sha256']for x in json.loads((root/'freeze.json').read_text())['inputs']if x['snapshot']==st.path.name))
check('native_fixed_forcing_and_range',st.native_source and 3<b<4 and st.bb==st.beta and st.seed_field.bb==3 and float(st.meta['eps'])==1)
check('homogeneous_inverse_identity',not add(deriv(deriv(P)),scale(P,k*k),A0))
check('predictor_nonzero',norm2(apred)>0 and norm2(bpred)>0)
vals={'a_L2':norm(A0)*float(L)**float(1+s),'a2_L2':norm(A1)*float(L)**float(1+2*s),'b_L2':norm(H0)*float(L)**float(1+2*s),'b2_L2':norm(H1)*float(L)**float(1+3*s),'a2_rel_diff_own_relation':math.sqrt(float(norm2(ae)/norm2(apred))),'b2_rel_diff_own_relation':math.sqrt(float(norm2(be)/norm2(bpred)))}
comparisons=[]
for key,val in vals.items():
 ref=num['endpoint'][key];err=abs(val-ref);comparisons.append({'key':key,'own':val,'NUM':ref,'absolute_difference':err});check('endpoint_finite_decimal_agreement',err<1e-8*max(1,abs(val)),comparisons[-1])
for name,p in [('H0',H0),('H1',H1),('A0',A0),('A1',A1),('P',P),('a2pred',apred),('b2pred',bpred)]:
 check('exact_real_fourier_symmetry',all(p.get(-n,(Q(0),Q(0)))==(c[0],-c[1])for n,c in p.items()),name)
check('self_tail_nonzero',bool(ae)and bool(be))
# Verify the old exact archive residual Laurent data, independent of its numerical norms.
old=json.loads(Path('research/248_k40_vertex_regional/verification/exact_native_tail.json').read_text());row=next(x for x in old['states']if x['archive_sha256']==st.sha256)
load=lambda poly:{int(n):tuple(map(Q,c))for n,c in poly.items()}
check('existing_ET_matches_negative_thermal_mismatch',not add(load(row['coefficients']['ET']),be))
check('existing_EO_matches_negative_vorticity_mismatch',not add(load(row['coefficients']['EO']),ae))
# Norm arithmetic uses no per-angle floor. Stored ratios use a predictor denominator.
ell=json.loads((root/'ell_L2K40_b3085.json').read_text());bands=[]
for z in ell['bands']:
 bands.append({'lo':z['lo'],'hi':z['hi'],'modal_max_absE':z['max_absE'],'sum_modal_maxE':z['max_sumE'],'ratio_of_separate_band_maxima':z['max_sumE']/z['max_sumOm'],'reported_modal_ratio':z['max_ratio'],'reported_step_difference':z['max_trunc']})
check('elliptic_global_reported_modal_max',ell['max_ratio']==max(z['max_ratio']for z in ell['bands']))
check('elliptic_global_reported_step_difference',ell['max_trunc']==max(z['max_trunc']for z in ell['bands']))
result={'started_utc':beg,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-t0,'checks':checks,'passed':sum(c['passed']for c in checks),'total':len(checks),'endpoint_comparisons':comparisons,'exact_polynomials':{key:ser(p)for key,p in [('H0',H0),('H1',H1),('A0',A0),('A1',A1),('a2pred',apred),('b2pred',bpred)]},'elliptic_band_statistics':bands,'archive_sha256':st.sha256,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact binary endpoint coefficient formulas, floating Parseval norms, and finite JSON statistics. No new finite-window fit, no E error enclosure or global stagnation exclusion.'}
(root/'endpoint_checks.json').write_text(json.dumps(result,indent=2)+'\n');print(result['passed'],result['total'],'seconds',result['elapsed_seconds']);print('comparisons',comparisons);print('failed',[c for c in checks if not c['passed']])

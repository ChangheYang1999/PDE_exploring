from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from flint import arb,ctx
from mpmath import iv
import json,hashlib,sys
sys.dont_write_bytecode=True;ctx.prec=512;ctx.threads=1;iv.dps=220
R=Path(__file__).resolve().parents[3];D=R/'research/stored_scaling_interface_defect';E=D/'evidence'
def load(p):return json.loads(Path(p).read_text())
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def aq(q):return arb(q.numerator)/q.denominator
def iq(q):return iv.mpf(q.numerator)/iv.mpf(q.denominator)
def arends(v):
 def f(z):m,e=z.man_exp();return Q(int(m))*Q(2)**int(e)
 return {'lower_exact':str(f(v.lower())),'upper_exact':str(f(v.upper()))}
def ivends(v):
 def f(z):s,m,e,b=z;assert b==m.bit_length();return Q((-1 if s else 1)*m)*Q(2)**e
 return {'lower_exact':str(f(v._mpi_[0])),'upper_exact':str(f(v._mpi_[1]))}
A=load(E/'arb.json');x=load(R/A['hex_json']['path']);a,b=Q(A['a_exact']),Q(A['b_exact']);s=x['scalars_hex'];k=Q.from_float(float.fromhex(s['k']));bi=Q.from_float(float.fromhex(s['bi']));bo=Q.from_float(float.fromhex(s['bo']));kf=float(k);lambdas=[Q.from_float((kf-3)-j*(1-kf)-2*l) for j,l in x['outer_jl']]
assert max(lambdas)==lambdas[0] and max(lambdas)<Q(-5,2) and bo>Q(5,2) and bi>0
pi,po,ti,to=[Q(A[n]) for n in ['P_inner','P_outer','F1_inner','F1_outer']]
V={'inner_source_difference':aq(2*a).exp()*aq((ti+pi)/4),'outer_source_difference':-aq(2*b).exp()*aq((to+po)/4),'log_stored_rmin_minus_a':aq(Q.from_float(float.fromhex(s['rmin']))).log()-aq(a),'log_stored_R0_minus_b':aq(Q.from_float(float.fromhex(s['R0']))).log()-aq(b)}
I={'inner_source_difference':iv.exp(iq(a))**2*iq((ti+pi)/4),'outer_source_difference':-iv.exp(iq(b))**2*iq((to+po)/4),'log_stored_rmin_minus_a':iv.ln(iq(Q.from_float(float.fromhex(s['rmin']))))-iq(a),'log_stored_R0_minus_b':iv.ln(iq(Q.from_float(float.fromhex(s['R0']))))-iq(b)}
Z={}
for n in V:
 ar,ir=arends(V[n]),ivends(I[n]);assert max(Q(ar['lower_exact']),Q(ir['lower_exact']))<=min(Q(ar['upper_exact']),Q(ir['upper_exact']));assert Q(ar['lower_exact'])*Q(ar['upper_exact'])>0
 Z[n]={'arb512':ar,'iv220':ir}
assert -Q(Z['outer_source_difference']['arb512']['upper_exact'])>500*Q(Z['inner_source_difference']['arb512']['upper_exact'])>0
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_GROWTH_SCOPE_AND_DUAL_REVIEW_CORRECTIONS','arb_json_sha256':sha(E/'arb.json'),'hex_json_sha256':sha(R/A['hex_json']['path']),'code_sha256':sha(Path(__file__)),'stored_k_exact':str(k),'source_outer_lambdas_exact':[str(q) for q in lambdas],'max_density_power_exact':str(3+max(lambdas)),'bi_exact':str(bi),'bo_exact':str(bo),'valid_common_growth_exponent':'1/2','source_difference_outer_dominates_inner_by_more_than_500':True,'dual_intervals':Z,'scope':'Source lambda expression reproduced without importing foreign module. Both stored radii differ from exp of the chosen endpoint knots; conventions kept distinct.'}
with (E/'application_checks.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'common_growth_exponent':out['valid_common_growth_exponent'],'max_density_power_exact':out['max_density_power_exact'],'display_only':{n:z.str(20) for n,z in V.items()}}))

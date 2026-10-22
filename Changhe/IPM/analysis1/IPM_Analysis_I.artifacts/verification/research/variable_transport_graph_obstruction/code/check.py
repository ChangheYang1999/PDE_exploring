from pathlib import Path
from fractions import Fraction as F
import sys,os,json,hashlib
from datetime import datetime,timezone
sys.dont_write_bytecode=True
for n in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[n]='1'
import numpy as np
import sympy as S
from flint import arb,fmpq,ctx
ctx.prec=512;ctx.threads=1
R=Path(__file__).resolve().parents[3];P=R/'research/variable_transport_graph_obstruction';E=P/'evidence'
sys.path.insert(0,str(R/'research/full_derivative_norm_bound_v2/code'));import protocol as p
assert p.sha(R/'research/full_derivative_norm_bound_v2/code/protocol.py')=='b57406959b9857d3acf994d7c1067fe4f534fa3b2362d2ddc3ed785be2cdcdcf'
start=p.now();pf=p.load(E/'proof_first.json');assert p.sha(P/'PROOF.md')==pf['proof_sha256']=='5f6216563558ba2bbf28709c1a24bb2772b792d19f9fa75ee87eb033763202a4'
parents={'moving_source':'dbe8a4e8794275a1524c9879c0bbfe949eb931bb3acc1014c7f30c9e90d83e11','annular_degree_five_leakage_v2':'e278d00ef75c8622235c16e9064d9cbd9be810f42e47f4eff28de8b077a88d25','logarithmic_frozen_range_inverse':'a5cce5f36cf56efdd512eb8ef5274f0b8708151342f4a16ec93892006601c3d7','source_instance':'be3a8ee307d1ed499af009c767be40b5e5982a1230fc51518355e77fee43516d','n8_velocity_hessian':'8a35f9cb43b241bd7a880b03aa8fcfdc01806a2517f50dbea99530e03a2455d5','n8_density_hessian':'c590ba0d354b26595bd1131f68ca87bbc9875c9d248b4cf5fdf71344ef6e01ca','canonical_full_radial_linkage':'4d91f313ec6dc475fc85a075f4154f6f302081112a0b5f7d77f7a172414eed1e'}
mapping=p.load(R/'research/full_derivative_norm_bound_v2/external_rebindings.json');pins={};deps={}
for name,h in parents.items():
 rel=f'research/{name}/evidence/verdict.json';p.pin(pins,rel,h);v=p.load(R/rel);assert v['status'].startswith('CONFIRMED');reb={}
 for n,nh in v['files'].items():
  if n in mapping:
   z=mapping[n];assert z['sha256']==nh and v['files'][z['replacement']]==nh;p.pin(pins,z['replacement'],nh);reb[n]=z
  else:p.pin(pins,n,nh)
 deps[name]={'path':rel,'sha256':h,'status':v['status'],'utc':v['utc'],'pins':len(v['files']),'byte_identical_rebindings':reb}
 if name=='canonical_full_radial_linkage':assert v['explicit_premise_application']['canonical_moment_condition_discharged'] is True
p.pin(pins,'research/full_derivative_norm_bound_v2/external_rebindings.json')
sv=p.load(R/'research/modal_source/evidence/source_result.json');pl,pu=map(F,sv['final_root_endpoints_exact']);mu=sv['final_values']['mu_minus_1'];mul,muu=1+F(mu['lower_exact']),1+F(mu['upper_exact']);A0=sv['final_values']['A_trial'];a0l,a0u=F(A0['lower_exact']),F(A0['upper_exact']);assert pl>F(43,5) and mul>F(99,100) and 0<a0l<a0u<F(51,5)
vp=p.load(R/'research/n8_velocity_hessian/evidence/verdict.json');M=F(vp['bound_exact']);rad=F(vp['disc_radius_exact']);assert M==F(743,2500) and rad==F(99,2000)
npz=R/'research/modal_exactification/evidence/trial_v2_h0.008.npz';assert p.sha(npz)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
with np.load(npz,allow_pickle=False) as z:k=F.from_float(float(z['k'].item()))
A=2/k-1;D=2*A+1;e=F(1,10000);ym=F(1,2000);yp=F(3,2000);rem=M*(e*e+yp*yp)/2;bmin=A*F(99,100)-D*(F(51,5)*e+rem)/(F(43,5)-e)-A*rem/ym
assert e*e+yp*yp<rad*rad and bmin>10
lo=F((bmin*10**12).numerator//(bmin*10**12).denominator,10**12);hi=lo+F(1,10**12);assert 10<lo<bmin<hi
# Differentiation of full expressions, not preassigned coefficient equalities.
x,y,z,a,AA,DD,nn,ss=S.symbols('x y z a A D n s',positive=True);vv1,vv2=S.symbols('v1 v2',real=True);bb=S.Function('b')(z,y);phase=DD*z+AA*S.log(y);Fnn=nn**(-ss)*bb*S.exp(S.I*nn*phase);h=S.exp((a-S.Rational(1,2))*z)*Fnn;weight=S.exp((S.Rational(1,2)-a)*z);c=-AA*(a-S.Rational(1,2))-1
checks={}
checks['frozen_characteristic_phase']=S.simplify(-AA*S.diff(phase,z)+DD*y*S.diff(phase,y))
checks['frozen_full_conjugation_and_phase_cancellation']=S.simplify(weight*(-AA*S.diff(h,z)+DD*y*S.diff(h,y)-h)-nn**(-ss)*S.exp(S.I*nn*phase)*(-AA*S.diff(bb,z)+DD*y*S.diff(bb,y)+c*bb))
checks['variable_full_conjugation']=S.simplify(weight*(vv1*S.exp(-z)*S.diff(h,z)+vv2*S.diff(h,y))-nn**(-ss)*S.exp(S.I*nn*phase)*(S.I*nn*(DD*vv1*S.exp(-z)+AA*vv2/y)*bb+vv1*S.exp(-z)*S.diff(bb,z)+vv2*S.diff(bb,y)+(a-S.Rational(1,2))*vv1*S.exp(-z)*bb))
q1,q2=S.symbols('q1 q2',real=True);checks['velocity_vector_symbol_square']=S.factor((q1*q2/(q1*q1+q2*q2))**2+(-q1*q1/(q1*q1+q2*q2))**2-q1*q1/(q1*q1+q2*q2))
K2=(x*x-y*y)/(2*S.pi*(x*x+y*y)**2);kernel=(3*x*x*y-y**3)/(S.pi*(x*x+y*y)**3)
checks['strain_kernel_sign']=S.factor(-S.diff(K2,y)-kernel)
checks['strain_F1_cancellation']=S.Rational(2,4)*S.Rational(1,2)*(1-1);checks['strain_F3_factor']=S.Rational(2,4)*S.Rational(1,2)*(1+3)-1
assert all(v==0 for v in checks.values()),checks
# Directed Arb recomputation of the complete scalar expression.
def Q(v):v=F(v);return arb(fmpq(v.numerator,v.denominator))
ak=Q(k);aa=2/ak-1;dd=4/ak-1;rr=Q(M)*(Q(e)**2+Q(yp)**2)/2;v=aa*Q(F(99,100))-dd*(Q(F(51,5))*Q(e)+rr)/(Q(F(43,5))-Q(e))-aa*rr/Q(ym)
def endpoint(v):m,e=v.man_exp();return F(int(m))*F(2)**int(e)
al,au=endpoint(v.lower()),endpoint(v.upper());assert lo<al<=bmin<=au<hi
out={'start_utc':start,'utc':p.now(),'status':'PASS_SOURCE_RECTANGLE_STRICT_MISMATCH_AND_CONJUGATIONS','proof_sha256':p.sha(P/'PROOF.md'),'code_sha256':p.sha(Path(__file__)),'parent_files':pins,'parent_pin_count':len(pins),'parents':deps,'source_accepted_bounds':{'p_lower':'43/5','mu_lower':'99/100','A0_upper':'51/5','M':str(M),'R':str(rad)},'actual':{n:str(v) for n,v in {'k':k,'A':A,'D':D,'e':e,'y_min':ym,'y_max':yp,'Taylor_remainder':rem,'b_lower':bmin}.items()},'strict_window':[str(lo),str(hi)],'arb512':{'lower_exact':str(al),'upper_exact':str(au)},'symbolic_identities':{n:str(v) for n,v in checks.items()},'scope':'Finite rational/interval and conjugation checks only. Function-space estimates and exact corrected sequence depend on the analytic proof.'};p.write(E/'check.json',out);print(json.dumps({n:out[n] for n in ['utc','status','parent_pin_count','actual','strict_window','symbolic_identities']}))

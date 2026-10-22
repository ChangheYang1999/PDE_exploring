from pathlib import Path
from fractions import Fraction as F
import sys,os,json
sys.dont_write_bytecode=True
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[name]='1'
import numpy as np
import sympy as S
R=Path(__file__).resolve().parents[3];D=R/'research/logarithmic_center_trace';E=D/'evidence';sys.path.insert(0,str(R/'research/full_derivative_norm_bound_v2/code'));import protocol as p
start=p.now();pf=p.load(E/'proof_first.json');assert p.sha(D/'PROOF.md')==pf['proof_sha256']=='1520a97d475afcfd62a464c32d7549d299d2d33ddf3ef24776528006ecdd3f58'
parent='research/logarithmic_scaling_rank_one/evidence/verdict.json';pv=p.load(R/parent);pins=dict(pv['files']);p.pin(pins,parent,'828baf7779370b7bb6b19e7a17d3c653ac9bcfeedb4fcc79353205addf91c843');p.rehash(pins)
raw=R/'research/modal_exactification/evidence/trial_v2_h0.008.npz';assert p.sha(raw)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
with np.load(raw,allow_pickle=False) as data:k=F.from_float(float(data['k'].item()))
actual={'k':k,'A':2/k-1,'D':4/k-1,'D_minus_2A':F(1),'example_weight':F(3,2),'example_decay_power':F(1),'s':F(153,50)};assert actual['A']>0 and actual['D']==2*actual['A']+1
x,y,u,z=S.symbols('x y u z',real=True);delta=S.symbols('delta',positive=True);b,beta,A,DD=S.symbols('b beta A D',real=True);C=S.Function('C');eta=S.Function('eta');Fz=S.Function('F')
f=-x**4*C(x/delta)*eta(y)/12;h=-S.diff(f,x,2)-S.diff(f,y,2);psi=S.diff(f,x);U1=-S.diff(psi,y);U2=S.diff(psi,x)
H2=S.diff(u**4*C(u),u,2)*eta(y)/12;H4=u**4*C(u)*S.diff(eta(y),y,2)/12
checks={}
def put(name,expr):
 value=S.simplify(S.expand(expr).doit());assert value==0,(name,value);checks[name]=str(value)
put('two_term_scaling',h.subs(x,delta*u).doit()-delta**2*H2-delta**4*H4)
put('H2_expansion',H2-u**2*(C(u)+2*u*S.diff(C(u),u)/3+u*u*S.diff(C(u),u,2)/12)*eta(y))
put('Poisson_stream',-S.diff(psi,x,2)-S.diff(psi,y,2)-S.diff(h,x))
put('velocity_divergence',S.diff(U1,x)+S.diff(U2,y))
put('velocity_curl',S.diff(U2,x)-S.diff(U1,y)+S.diff(h,x))
f0=-x**4*y/12;h0=-S.diff(f0,x,2)-S.diff(f0,y,2)
put('center_density',h0-x*x*y);J=S.diff(h0,x,2,y).subs({x:0,y:0})/2;Sigma=S.diff(f0,x,2,y).subs({x:0,y:0});assert J==1 and Sigma==0
put('center_J',J-1);put('center_Sigma',Sigma)
weighted=S.exp(-beta*z)*Fz(z,y);Tf=-A*S.diff(weighted,z)+DD*y*S.diff(weighted,y)-weighted
put('frozen_conjugation',S.exp(beta*z)*Tf-(-A*S.diff(Fz(z,y),z)+DD*y*S.diff(Fz(z,y),y)+(A*beta-1)*Fz(z,y)))
put('lower_decay_power',2+S.Rational(1,2)-b-(S.Rational(5,2)-b))
put('upper_decay_power',4+S.Rational(1,2)-b-(S.Rational(5,2)-b+2))
# Finite Euler-derivative checks illustrate, but do not prove, the all-order induction.
a=S.symbols('a',real=True);g=S.Function('g')(u,y)
for n in range(1,7):
 left=u**a*g;right=g
 for _ in range(n):left=u*S.diff(left,u);right=a*right+u*S.diff(right,u)
 put(f'power_preservation_order{n}',left-u**a*right)
out={'start_utc':start,'utc':p.now(),'status':'PASS_CENTER_POTENTIAL_SCALING_CONJUGATION_AND_TRACE_ALGEBRA','proof_sha256':p.sha(D/'PROOF.md'),'code_sha256':p.sha(Path(__file__)),'parent_files':pins,'parent_pin_count':len(pins),'actual':{n:str(v) for n,v in actual.items()},'symbolic_identities':checks,'center_J':str(J),'center_Sigma':str(Sigma),'delta_powers':['5/2-b','9/2-b'],'scope':'Finite exact identities only. General Sobolev convergence, sublinear-gauge uniqueness and nonclosability follow from the informal proof and REVIEW_RESPONSE, not these checks.'};p.write(E/'check.json',out);print(json.dumps({n:out[n] for n in ['start_utc','utc','status','parent_pin_count','actual','symbolic_identities']}))

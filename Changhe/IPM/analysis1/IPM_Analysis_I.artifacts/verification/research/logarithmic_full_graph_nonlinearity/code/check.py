from pathlib import Path
from fractions import Fraction as F
import sys,os,json
sys.dont_write_bytecode=True
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[name]='1'
import numpy as np
import sympy as S
R=Path(__file__).resolve().parents[3];D=R/'research/logarithmic_full_graph_nonlinearity';E=D/'evidence';sys.path.insert(0,str(R/'research/full_derivative_norm_bound_v2/code'));import protocol as p
start=p.now();pf=p.load(E/'proof_first.json');assert p.sha(D/'PROOF.md')==pf['proof_sha256']=='3ecda23dfa05f97bb7aedb762506b6d21e5a40e6918d6c9fc69d3b893cce4f32'
parent='research/logarithmic_full_graph_center_trace/evidence/verdict.json';pv=p.load(R/parent);assert pv['status']=='CONFIRMED_CENTER_TRACE_NONCLOSABILITY_IN_FULL_LINEARIZED_LOGARITHMIC_GRAPH';pins=dict(pv['files']);p.pin(pins,parent);p.rehash(pins)
raw=R/'research/modal_exactification/evidence/trial_v2_h0.008.npz';assert p.sha(raw)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
with np.load(raw,allow_pickle=False) as data:
 k,bi,L=[F.from_float(float(data[name].item())) for name in ['k','bi','L']];tau=F.from_float(float(data['knots'][0]));degree=int(data['p']);modes=int(data['M'])
assert 0<k<F(1,2) and bi>50 and L>0 and tau<0 and degree==7 and modes==260
actual={'k':k,'A':2/k-1,'D':4/k-1,'bi':bi,'L':L,'inner_tau':tau,'spline_degree':F(degree),'modes':F(modes),'s_example':F(153,50),'center_Vx_coefficient':1-2/k}
x,y,pp=S.symbols('x y p',real=True);n=S.symbols('n',positive=True);s=S.symbols('s',real=True);a=S.Function('a')(x,y);phi=S.Function('phi')(x,y);v1=S.Function('v1')(x,y);v2=S.Function('v2')(x,y);Fpot=S.Function('F')(x,y)
checks={}
def put(name,value):
 q=S.simplify(S.expand(value).doit());assert q==0,(name,q);checks[name]=str(q)
def lap(f):return S.diff(f,x,2)+S.diff(f,y,2)
def U(f):return [-S.diff(f,x,y),S.diff(f,x,2)]
def vdot(f):return v1*S.diff(f,x)+v2*S.diff(f,y)
h=-lap(Fpot);psi=S.diff(Fpot,x);uu=U(Fpot)
put('canonical_Poisson',-lap(psi)-S.diff(h,x));put('divergence_free',S.diff(uu[0],x)+S.diff(uu[1],y));put('curl_sign',S.diff(uu[1],x)-S.diff(uu[0],y)+S.diff(h,x))
plateau=(x-pp)**2/2;gu=U(plateau);g=-lap(plateau)
put('plateau_density',g+1);put('plateau_velocity1',gu[0]);put('plateau_velocity2',gu[1]-1);put('plateau_gradient_x',S.diff(g,x));put('plateau_gradient_y',S.diff(g,y))
# Factor out the common spatially constant n^(-s), for exact finite wave algebra.
f=a*S.cos(n*phi)/n**2;h=-lap(f);u1,u2=U(f);c=S.cos(n*phi);sn=S.sin(n*phi)
A0=a*(S.diff(phi,x)**2+S.diff(phi,y)**2);A1=2*(S.diff(a,x)*S.diff(phi,x)+S.diff(a,y)*S.diff(phi,y))+a*lap(phi);A2=lap(a)
put('density_wave_expansion',h-(A0*c+A1*sn/n-A2*c/n**2))
U1=a*S.diff(phi,x)*S.diff(phi,y)*c+(S.diff(a,x)*S.diff(phi,y)+S.diff(a,y)*S.diff(phi,x)+a*S.diff(phi,x,y))*sn/n-S.diff(a,x,y)*c/n**2
U2=-a*S.diff(phi,x)**2*c-(2*S.diff(a,x)*S.diff(phi,x)+a*S.diff(phi,x,2))*sn/n+S.diff(a,x,2)*c/n**2
put('velocity1_wave_expansion',u1-U1);put('velocity2_wave_expansion',u2-U2)
phasefactor=-n*A0*sn+A1*c+A2*sn/n
put('transport_phase_factorization',vdot(h)-(vdot(A0)*c+vdot(A1)*sn/n-vdot(A2)*c/n**2)-vdot(phi)*phasefactor)
rest=(S.diff(A0,y)+A1*S.diff(phi,y))*c+(S.diff(A1,y)+A2*S.diff(phi,y))*sn/n-S.diff(A2,y)*c/n**2
put('transverse_leading_remainder',S.diff(h,y)+n*A0*S.diff(phi,y)*sn-rest)
put('plateau_cross_exact',gu[0]*S.diff(h,x)+gu[1]*S.diff(h,y)+u1*S.diff(g,x)+u2*S.diff(g,y)-S.diff(h,y))
# Reflection covariance from the exact chain signs for generic potential jets.
fxx,fxy,fyy,fx,fy=S.symbols('fxx fxy fyy fx fy');reflection=[]
for sx in [-1,1]:
 for sy in [-1,1]:
  sig=sy
  transformed=[-sig*sx*sy*fxy,sig*sx*sx*fxx];expected=[sx*(-fxy),sy*fxx]
  for j in range(2):put(f'reflection_U_{sx}_{sy}_{j}',transformed[j]-expected[j])
  put(f'reflection_density_{sx}_{sy}',-(sig*sx*sx*fxx+sig*sy*sy*fyy)-sig*(-fxx-fyy))
  # V(SX)=S V(X), phi_S=phi(SX), so V.gradphi_S=(V.gradphi)(SX).
  put(f'reflection_first_integral_{sx}_{sy}',v1*sx*fx+v2*sy*fy-(sx*v1*fx+sy*v2*fy))
  reflection.append({'sx':sx,'sy':sy,'potential_sign':sig,'velocity_signs':[sx,sy]})
ug1,ug2,uh1,uh2,gx,gy,hx,hy,sg,sh=S.symbols('ug1 ug2 uh1 uh2 gx gy hx hy sg sh')
qp=(ug1+uh1)*(gx+hx)+(ug2+uh2)*(gy+hy)+(sg+sh)*(x*(gx+hx)+y*(gy+hy))/3
qm=(ug1-uh1)*(gx-hx)+(ug2-uh2)*(gy-hy)+(sg-sh)*(x*(gx-hx)+y*(gy-hy))/3
cross=ug1*hx+ug2*hy+uh1*gx+uh2*gy+(sg*(x*hx+y*hy)+sh*(x*gx+y*gy))/3
put('full_rank_one_polarization',qp-qm-2*cross);put('zero_strain_polarization',(qp-qm-2*(ug1*hx+ug2*hy+uh1*gx+uh2*gy)).subs({sg:0,sh:0}))
for j in [0,1,2]:put(f'modulation_power_{j}',(-s-j)+s+j)
put('scaled_cross_power',2*S.Rational(-1,2)+1);put('origin_saddle_relation',S.Rational(actual['D'].numerator,actual['D'].denominator)-2*S.Rational(actual['A'].numerator,actual['A'].denominator)-1)
out={'start_utc':start,'utc':p.now(),'status':'PASS_COMPACT_POTENTIAL_WAVE_AND_POLARIZATION_IDENTITIES','proof_sha256':p.sha(D/'PROOF.md'),'code_sha256':p.sha(Path(__file__)),'parent_files':pins,'parent_pin_count':len(pins),'actual':{k:str(v) for k,v in actual.items()},'symbolic_identities':checks,'reflections':reflection,'scope':'Exact finite algebra and data only. First-integral existence, compact support, all-order Sobolev modulation, full graph bounds and nonlinear discontinuity are analytic claims, not inferred from these finite checks.'};p.write(E/'check.json',out);print(json.dumps({k:out[k] for k in ['start_utc','utc','status','parent_pin_count','actual','symbolic_identities']}))

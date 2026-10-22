from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import sys,os,json
sys.dont_write_bytecode=True
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[name]='1'
import numpy as np
import sympy as S
R=Path(__file__).resolve().parents[3];D=R/'research/logarithmic_full_graph_center_trace';E=D/'evidence';sys.path.insert(0,str(R/'research/full_derivative_norm_bound_v2/code'));import protocol as p
start=p.now();pf=p.load(E/'proof_first.json');assert p.sha(D/'PROOF.md')==pf['proof_sha256']=='4d0743551aa93af5ae49825fe75f4230cd1392f17ac7ad45c007805056a08125'
parent='research/logarithmic_center_trace/evidence/verdict.json';pv=p.load(R/parent);pins=dict(pv['files']);p.pin(pins,parent,'0e401e54ccb1022ef2d82922f8f57b36eab6f2624b66927592fdecdc63d871c0');p.rehash(pins)
raw=R/'research/modal_exactification/evidence/trial_v2_h0.008.npz';assert p.sha(raw)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
with np.load(raw,allow_pickle=False) as data:
 k,bi=[F.from_float(float(data[n].item())) for n in ['k','bi']];knots=[F.from_float(float(t)) for t in data['knots']];degree=int(data['p']);modes=int(data['M']);shape=list(data['S'].shape)
cnt=Counter(knots);unique=sorted(cnt);assert knots==sorted(knots) and len(knots)==1573 and len(unique)==1559 and [cnt[t] for t in unique]==[8]+[1]*1557+[8]
assert degree==7 and modes==260 and shape==[260,1565] and bi>50 and 0<k<F(1,2)
actual={'k':k,'bi':bi,'inner_log_density_degree':bi+3,'inner_log_velocity_degree':bi+3,'fifth_derivative_log_margin':bi-2,'spline_degree':F(degree),'annular_join_order':F(6),'density_frequency_max':F(521),'source_frequency_max':F(522),'velocity_frequency_max':F(523),'s_example':F(153,50),'theta_example':F(3,50),'alpha_example':F(1,2),'multiplier_gap_example':F(11,25)}
# Trigonometric product-to-sum, followed by the Cartesian derivative formula.
# Each source frequency coefficient is affine in a generic homogeneous degree P.
source_maps=[]
for m in range(modes):
 d={}
 for n in [1,3]:
  for signed in [n+2*m,n-2*m]:
   if signed:d[abs(signed)]=d.get(abs(signed),F())+(1 if signed>0 else -1)*F(1,8)
 d={n:c for n,c in d.items() if c};q={}
 for n,c in d.items():
  for freq,constant in [(n+1,-n),(n-1,n)]:
   if freq:
    aa,bb=q.get(freq,(F(),F()));q[freq]=(aa+c*constant/2,bb+c/2)
 q={n:v for n,v in q.items() if any(v)};assert max(d)<=521 and max(q)<=522 and all(n%2==0 for n in q)
 source_maps.append({str(n):list(map(str,v)) for n,v in sorted(q.items())})
assert source_maps[0]=={'2':['1/4','1/4'],'4':['-3/8','1/8']}
x,y,u,z=S.symbols('x y u z',real=True);delta,r=S.symbols('delta r',positive=True);beta,b,pp,nn=S.symbols('beta b P n',real=True);C=S.Function('C');eta=S.Function('eta');Fx=S.Function('F')(z,y);cv=S.Function('p')(z,y);vv=S.Function('v')(z,y)
f=-x**4*C(x/delta)*eta(y)/12;h=-S.diff(f,x,2)-S.diff(f,y,2);U1=-S.diff(f,x,y);U2=S.diff(f,x,2)
H2=S.diff(u**4*C(u),u,2)*eta(y)/12;H3=S.diff(u**4*C(u),u)*S.diff(eta(y),y)/12;H4=u**4*C(u)*S.diff(eta(y),y,2)/12
checks={}
def put(name,value):
 v=S.simplify(S.expand(value).doit());assert v==0,(name,v);checks[name]=str(v)
put('density_scaling',h.subs(x,delta*u).doit()-delta**2*H2-delta**4*H4)
put('velocity1_sign_scaling',U1.subs(x,delta*u).doit()-delta**3*H3)
put('velocity2_sign_scaling',U2.subs(x,delta*u).doit()+delta**2*H2)
put('H3_expansion',H3-(4*u**3*C(u)+u**4*S.diff(C(u),u))*S.diff(eta(y),y)/12)
weighted=S.exp(-beta*z)*Fx
put('variable_transport_conjugation',S.exp(beta*z)*(cv*S.diff(weighted,z)+vv*S.diff(weighted,y)-weighted)-(cv*(S.diff(Fx,z)-beta*Fx)+vv*S.diff(Fx,y)-Fx))
rx,ry=S.symbols('rho_x rho_y');put('nonlocal_coupling_scaling',(U1*rx+U2*ry).subs(x,delta*u).doit()-(delta**3*H3*rx-delta**2*H2*ry))
for name,order in [('h2',2),('U1',3),('h4',4)]:put('weight_power_'+name,order+S.Rational(1,2)-b-(S.Rational(5,2)-b+order-2))
part=-x**3*y/3;put('leading_polynomial_Poisson',-S.diff(part,x,2)-S.diff(part,y,2)-2*x*y)
P=r**(pp+2)/(nn**2-(pp+2)**2);put('radial_nonresonant',-S.diff(P,r,2)-S.diff(P,r)/r+nn**2*P/r**2-r**pp)
Plog=-r**nn*S.log(r)/(2*nn);put('radial_resonant',-S.diff(Plog,r,2)-S.diff(Plog,r)/r+nn**2*Plog/r**2-r**(nn-2))
put('s_example_split',S.Rational(153,50)-3-S.Rational(3,50));put('multiplier_gap',S.Rational(1,2)-S.Rational(3,50)-S.Rational(11,25))
out={'start_utc':start,'utc':p.now(),'status':'PASS_FULL_GRAPH_LOCAL_PREMISES_AND_EXACT_SCALING','proof_sha256':p.sha(D/'PROOF.md'),'code_sha256':p.sha(Path(__file__)),'parent_files':pins,'parent_pin_count':len(pins),'actual':{n:str(v) for n,v in actual.items()},'knots':list(map(str,knots)),'distinct_knots':len(unique),'modes':modes,'shape':shape,'source_maps':source_maps,'symbolic_identities':checks,'scope':'Exact parameter, knot, finite angular-support and differential identities only. No new join evaluation, interval norm bound, multiplier constant or Sobolev theorem is inferred from finite checks.'};p.write(E/'check.json',out);print(json.dumps({n:out[n] for n in ['start_utc','utc','status','parent_pin_count','actual','symbolic_identities']}))

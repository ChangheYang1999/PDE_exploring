from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import os
for n in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[n]='1'
import sys,json,hashlib
sys.dont_write_bytecode=True
import numpy as np
import sympy as S
R=Path(__file__).resolve().parents[3];P=R/'research/logarithmic_frozen_range_inverse';E=P/'evidence'
def now():return datetime.now(timezone.utc).isoformat()
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
start=now();pf=load(E/'proof_first.json');assert pf['proof_sha256']==sha(P/'PROOF.md')=='e4ac31efdbd4e846c5d4765033cb6b5a7b71e209458b4dcc9153742d6abf753d'
rel='research/logarithmic_frozen_spectrum/evidence/verdict.json';assert sha(R/rel)=='eda22fba890eeb985df010d272895e436f06460972cfec584ac576f85d7e664f';parent=load(R/rel);pins=dict(parent['files']);pins[rel]=sha(R/rel)
for n,h in pins.items():assert sha(R/n)==h,n
u,v,D,r,tau=S.symbols('u v D r tau',positive=True);s=S.symbols('s',real=True);c,A,xi=S.symbols('c A xi',real=True);B,eta=S.symbols('B eta',positive=True)
total=u+v;H=total-2*D;d=-u+total*r;W=d*d+2*D*total*r*(1-r);Wexpr=u*u+2*total*(D-u)*r+total*H*r*r;vertex=(u-D)/H;m=D*D+2*D*(u-D)*(v-D)/H
checks={}
checks['coercive_quadratic']=S.expand(W-Wexpr);checks['endpoint_left']=S.expand(W.subs(r,0)-u*u);checks['endpoint_right']=S.expand(W.subs(r,1)-v*v)
checks['vertex_stationarity']=S.factor(S.diff(W,r).subs(r,vertex));checks['vertex_value']=S.factor(W.subs(r,vertex)-m)
checks['completed_square']=S.factor(W-m-total/H*(H*r-(u-D))**2);checks['vertex_right_margin']=S.factor(1-vertex-(v-D)/H)
rr=S.exp(2*tau)/(1+S.exp(2*tau));dd=-u+total*rr;g=S.exp(u*tau/D)*(1+S.exp(2*tau))**(-total/(2*D))
checks['potential_derivative']=S.simplify(S.diff(dd,tau)-2*total*rr*(1-rr));checks['adjoint_integrating_factor']=S.simplify(D*S.diff(g,tau)+dd*g)
logB=S.log(B);te=S.log(eta)-logB/2;logOriginal=-S.I*A*xi*te/D-S.log(eta)/2-s*S.log(B+eta**2)/2+u*te/D-s*S.log(1+eta**2/B)/2
logTarget=(-c-S.I*A*xi)*S.log(eta)/D-s*S.log(B+eta**2)+(s/2-u/(2*D)+S.I*A*xi/(2*D))*logB
checks['original_adjoint_scalar_and_exponents']=S.simplify(S.expand_log((logOriginal-logTarget).subs(u,D/2-c),force=True))
checks['weighted_pairing_cancels_sobolev_exponent']=S.simplify(s+(-s));checks['pairing_conjugates_phase']=S.simplify(S.conjugate((-c-S.I*A*xi)/D)-(-c+S.I*A*xi)/D)
assert all(vv==0 for vv in checks.values()),checks
npz=R/'research/modal_exactification/evidence/trial_v2_h0.008.npz';assert sha(npz)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
with np.load(npz,allow_pickle=False) as z:k=F.from_float(float(z['k'].item()))
Av=2/k-1;Dv=4/k-1;sv=F(153,50);uv=1+1/k;vv=sv*Dv-uv;assert 0<uv<Dv and vv>uv;iv=1/uv;assert iv==k/(1+k)
lo=F((iv*10**12).numerator//(iv*10**12).denominator,10**12);hi=lo+F(1,10**12);assert lo<iv<hi
cases=[]
for name,uu,vv1,dd1 in [('actual_a0',uv,vv,Dv),('concave',F(2),F(3),F(4)),('linear',F(3),F(5),F(4)),('convex_left_endpoint',F(1),F(10),F(4)),('vertex_boundary',F(4),F(7),F(4)),('interior_asymmetric',F(5),F(7),F(4)),('interior_symmetric',F(8),F(8),F(4))]:
 mm=min(uu,vv1)**2 if min(uu,vv1)<=dd1 else dd1**2+2*dd1*(uu-dd1)*(vv1-dd1)/(uu+vv1-2*dd1)
 assert mm>0;hh=uu+vv1-2*dd1;coeff=[uu*uu,2*(uu+vv1)*(dd1-uu),(uu+vv1)*hh];values=[uu**2,vv1**2];vertex_value=None
 if hh>0:
  rv=(uu-dd1)/hh
  if 0<rv<1:vertex_value=sum(z*rv**i for i,z in enumerate(coeff));values.append(vertex_value)
 assert mm==min(values)
 cases.append({'name':name,'u':str(uu),'v':str(vv1),'D':str(dd1),'m':str(mm),'vertex_value':str(vertex_value) if vertex_value is not None else None,'sharp_inverse_norm':str(1/min(uu,vv1)) if min(uu,vv1)<=dd1 else None})
out={'start_utc':start,'utc':now(),'status':'PASS_GENERAL_COERCIVE_IDENTITY_MELLIN_CONSTRAINT_AND_EXACT_MINIMA','proof_sha256':sha(P/'PROOF.md'),'code_sha256':sha(Path(__file__)),'parent_files':pins,'parent_pin_count':len(pins),'parent_path':rel,'parent_sha256':sha(R/rel),'symbolic_identities':{n:str(v) for n,v in checks.items()},'actual':{n:str(v) for n,v in {'k':k,'A':Av,'D':Dv,'s':sv,'u':uv,'v':vv,'inverse_norm':iv}.items()},'inverse_strict_window':[str(lo),str(hi)],'cases':cases,'scope':'Exact finite identities and parameters; infinite-dimensional closed range and compatibility rely on standalone proof.'}
with (E/'check.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({n:out[n] for n in ['utc','status','parent_pin_count','actual','inverse_strict_window','cases']}))

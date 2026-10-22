from pathlib import Path
from fractions import Fraction as F
import sys,os,json,time
sys.dont_write_bytecode=True
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
import numpy as np
import sympy as S
from flint import arb,arb_poly,fmpq,ctx
ctx.prec=384;ctx.threads=1
R=Path(__file__).resolve().parents[3];D=R/'research/canonical_residual_weak_axis_membership';E=D/'evidence';sys.path.insert(0,str(R/'research/full_derivative_norm_bound_v2/code'));import protocol as p
start=p.now();clock=time.monotonic();pf=p.load(E/'proof_first.json');assert p.sha(D/'PROOF.md')==pf['proof_sha256']=='b13a5c23f5deb1779caaca192324f98f3565627aa86fe29ba08a7a547a2f33d3'
parent='research/weak_axis_compact_mapping/evidence/verdict.json';pv=p.load(R/parent);assert p.sha(R/parent)=='5b636a2d455238f70bfdf8db0875ec719c8f467ce123d4aec06a7a5c5eb4b529';assert pv['status'].startswith('CONFIRMED');pins=dict(pv['files']);p.pin(pins,parent);p.rehash(pins)
npz=R/'research/modal_exactification/evidence/trial_v2_h0.008.npz';assert p.sha(npz)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
with np.load(npz,allow_pickle=False) as data:
 k,bi,bo=[F.from_float(float(data[n].item())) for n in ['k','bi','bo']];tb=F.from_float(float(data['knots'][-1]));raw=[[F.from_float(float(x)) for x in row[:2]] for row in data['Aout']];assert data['Aout'].shape==(260,10)
zpath='research/modal_repair/evidence/independent_gauss_iv.json';assert pins[zpath]=='0985679510dfa1fbfceccddd19566d85452599c4b37ecde4c84adbd5aa5f0a2a';zz=p.load(R/zpath)['values']['A00_correction'];zlo,zhi=[F(zz[n]) for n in ['lower_exact_dyadic','upper_exact_dyadic']];assert zlo<=zhi
pairs=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1),(2,1),(0,2)];beta=[k-j*(1-k)-2*l for j,l in pairs]+[3-bo];gamma=2*k-1;ae=k+1
assert 0<k<F(1,2) and bi>50 and bo>120
assert [i for i,b in enumerate(beta) if b==gamma]==[1]
assert [(i,j) for i,b in enumerate(beta) for j,c in enumerate(beta) if b+c-1==gamma]==[(0,0)]
assert max(beta[2:])<gamma and max(beta)==k
transient=[gamma-(b-2*n-2) for n in range(1,262) for b in beta];assert min(transient)>0
particular=[gamma-(b+c-1) for i,b in enumerate(beta) for j,c in enumerate(beta) if (i,j)!=(0,0)];assert min(particular)>0
linear=[gamma-b for i,b in enumerate(beta) if i not in [0,1]];assert min(linear)>0
# Two affine density vectors in the exact normalization scalar.
d=[(F(0),F(0)) for _ in range(262)];d1=[(F(0),F(0)) for _ in range(262)]
for mode,(a0,a1) in enumerate(raw):
 for freq in [1+2*mode,1-2*mode,3+2*mode,3-2*mode]:
  j=(abs(freq)-1)//2;weight=F(1 if freq>0 else -1,8)
  d[j]=(d[j][0]+weight*a0,d[j][1]+weight*(mode==0));d1[j]=(d1[j][0]+weight*a1,F(0))
assert d[-1]==d1[-1]==(0,0)
def ball(q):q=F(q);return arb(fmpq(q.numerator,q.denominator))
def endpoint(v):m,e=v.man_exp();return F(int(m))*F(2)**int(e)
def out(v):
 assert v.is_finite();return {'lower_exact':str(endpoint(v.lower())),'upper_exact':str(endpoint(v.upper())),'display':v.str(35)}
z=ball(zlo).union(ball(zhi));ds=[ball(a)+ball(b)*z for a,b in d];d1s=[ball(a)+ball(b)*z for a,b in d1]
cv=[arb(0) for _ in range(523)];sv=[arb(0) for _ in range(523)];dr=[arb(0) for _ in range(522)];da=[arb(0) for _ in range(522)];den=[]
for n in range(1,262):
 m=2*n;fn=(ball(ae-m)*ds[n-1]+ball(ae+m)*ds[n])/2;qp=fn/ball(ae+m);qm=-fn/ball(ae-m);v=-(qp+qm)/2;w=(qm-qp)/2
 den.append(F(m*m)-ae*ae);assert den[-1]>0
 cv[261+n]=v/2;cv[261-n]=v/2;sv[261+n]=w;sv[261-n]=-w
for j in range(261):
 dr[261+j]=ball(k)*ds[j];dr[260-j]=-ball(k)*ds[j];da[261+j]=(2*j+1)*ds[j]/2;da[260-j]=(2*j+1)*ds[j]/2
conv=arb_poly(cv)*arb_poly(dr)+arb_poly(sv)*arb_poly(da);assert conv.degree()<=1043
q=1;assert (conv[522+q]+conv[521-q]).contains(0)
linear_e=ball(3*tb).exp()*ball(gamma/k-1)*d1s[q];product_e=ball(5*tb).exp()*conv[522+q];e1=linear_e+product_e
window=[F(-966216463877,10**15),F(-966216463875,10**15)];assert window[0]<endpoint(e1.lower())<=endpoint(e1.upper())<window[1]<0
# Arbitrary-factor residual and endpoint algebra; no numerical sampling.
x,y,kk,b,theta,qv=S.symbols('x y k b theta q',real=True);a=S.Function('a')(x,y);v1=S.Function('v1')(x,y);v2=S.Function('v2')(x,y);rho=x*x*y*a;A=2/kk-1;DD=4/kk-1
center=(-A*x+x*v1)*S.diff(rho,x)+(DD*y+y*v2)*S.diff(rho,y)-rho
cb=x*x*y*(-A*x*S.diff(a,x)+DD*y*S.diff(a,y)+v1*(2*a+x*S.diff(a,x))+v2*(a+y*S.diff(a,y)))
far=(x/kk+x*v1)*S.diff(rho,x)+(y/kk+y*v2)*S.diff(rho,y)-rho
fb=x*x*y*((3/kk-1)*a+(x*S.diff(a,x)+y*S.diff(a,y))/kk+v1*(2*a+x*S.diff(a,x))+v2*(a+y*S.diff(a,y)))
identities={'center_factor':S.expand(center-cb),'far_factor':S.expand(far-fb),'center_cubic_cancel':S.simplify(-2*A+DD-1),'far_leading_cancel':S.simplify(3/kk-1+(kk-3)/kk),'far_L2_shell':S.expand(5-2*b+1+2*(2*kk-3-qv)-2*(2*kk-b-qv)),'far_divergence_exponent':S.expand(2*(2*kk-1)-2*b+1-(4*kk-2*b-1)),'center_fractional':S.expand((1-theta)*(3-b)+theta*(2-b)-(6-b-(3+theta)))}
af,mm,FF=S.symbols('ae m F');qp=FF/(af+mm);qm=-FF/(af-mm);identities['green_to_poisson_radial']=S.factor(-(qp+qm)/2+mm*FF/(mm*mm-af*af));identities['green_to_poisson_angular']=S.factor((qm-qp)/2-af*FF/(mm*mm-af*af));assert all(v==0 for v in identities.values())
actual={'k':k,'bi':bi,'bo':bo,'tb':tb,'s':F(153,50),'gamma':gamma,'minimum_weight':2*k,'maximum_weight':F(5,2),'center_rate_infimum':F(11,25),'minimum_stream_denominator':min(den),'minimum_other_linear_gap':min(linear),'minimum_other_particular_gap':min(particular),'minimum_transient_gap':min(transient)}
result={'start_utc':start,'utc':p.now(),'status':'PASS_RAW_NPZ_ARB_LEADING_COEFFICIENT_AND_MEMBERSHIP_IDENTITIES','proof_sha256':p.sha(D/'PROOF.md'),'code_sha256':p.sha(Path(__file__)),'parent_files':pins,'parent_pin_count':len(pins),'actual':{n:str(v) for n,v in actual.items()},'beta':list(map(str,beta)),'normalization_interval':list(map(str,[zlo,zhi])),'projection_d':[[str(x) for x in row] for row in d],'projection_d1':[[str(x) for x in row] for row in d1],'leading_linear':out(linear_e),'leading_product':out(product_e),'e1':out(e1),'strict_window':list(map(str,window)),'convolution_degree':conv.degree(),'angular_target':3,'symbolic_identities':{n:str(v) for n,v in identities.items()},'counts':{'density_projection_modes':260,'velocity_modes':261,'transient_gaps':len(transient),'other_particular_gaps':len(particular),'other_linear_gaps':len(linear)},'seconds':time.monotonic()-clock,'scope':'One nonzero far coefficient recomputed from raw data. No physical norm ceiling; inherited canonical normalization and axis Q, finite-formula analytic Sobolev argument.'};p.write(E/'check.json',result);print(json.dumps({n:v for n,v in result.items() if n not in ['parent_files','projection_d','projection_d1','normalization_interval']}))

from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import sys,os,json
sys.dont_write_bytecode=True
for n in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[n]='1'
import numpy as np
import sympy as S
R=Path(__file__).resolve().parents[3];D=R/'research/weak_axis_compact_higher_orders';E=D/'evidence';sys.path.insert(0,str(R/'research/full_derivative_norm_bound_v2/code'));import protocol as p
start=p.now();pf=p.load(E/'proof_first.json');assert p.sha(D/'PROOF.md')==pf['proof_sha256']=='0dcddf0f8356c434242ffc63986a74079e578d70acb7c32acc76975018730f4f'
parent='research/logarithmic_strain_functional/evidence/verdict.json';pv=p.load(R/parent);pins=dict(pv['files']);p.pin(pins,parent,'06eb106433266f45cbdab9669a8c7fc71aa8c7c85794c25c7a27a7500135a62b');p.rehash(pins)
raw=R/'research/modal_exactification/evidence/trial_v2_h0.008.npz';assert p.sha(raw)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
with np.load(raw,allow_pickle=False) as z:
 vals={n:F.from_float(float(z[n].item())) for n in ['k','bi','bo']};knots=[F.from_float(float(t)) for t in z['knots']];degree=int(z['p']);modes=int(z['M']);shapes={n:list(z[n].shape) for n in ['S','D','Aout','Ei','Eo']}
k,bi,bo=[vals[n] for n in ['k','bi','bo']];assert 0<k<F(1,2) and bi>50 and bo>120 and degree==7 and modes==260
cnt=Counter(knots);unique=sorted(cnt);assert knots==sorted(knots) and len(knots)==1573 and len(unique)==1559 and [cnt[t] for t in unique]==[8]+[1]*1557+[8]
actual=vals|{'spline_degree':F(degree),'matched_derivative_order':F(degree-1),'weak_a_order':F(7),'weak_g_order':F(6),'max_uniform_s':F(7,2),'axis_limit':F(5,2),'center_base':F(6),'far_margin_at_b0':3-k,'inner_gap':bi-2,'outer_log_gap':bo+k-3}
pairs=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1),(2,1),(0,2)];exponents=[k-3-j*(1-k)-2*l for j,l in pairs];assert max(exponents)==k-3 and all(t<k-3 for t in exponents[1:])
x,y,beta,b,n,theta,kk,q,ss=S.symbols('x y beta b n theta k q s');aa=S.Function('a')(x,y);v1=S.Function('v1')(x,y);v2=S.Function('v2')(x,y);Q=S.Function('Q')(x,y)
rho=x*x*y*aa;g=x*v1*S.diff(rho,x)+y*v2*S.diff(rho,y);B=v1*(2*aa+x*S.diff(aa,x))+v2*(aa+y*S.diff(aa,y));checks={'x2y_factor':S.expand(g-x*x*y*B)}
for pp in range(7):
 for qq in range(7-pp):
  f=S.diff(x*x*Q,y,qq);C=S.diff(Q,y,qq)
  for _ in range(pp):f=x*S.diff(f,x)+beta*f;C=x*S.diff(C,x)+(beta+2)*C
  checks[f'factor_p{pp}_q{qq}']=S.expand(f-x*x*C)
checks['center_L2_exponent']=S.expand((5-2*b)+1+2*(3-q)-2*(6-b-q));checks['far_L2_exponent']=S.expand((5-2*b)+1+2*(kk-6-q)-2*(kk-3-b-q));checks['interpolation']=S.expand((1-theta)*(6-b-n)+theta*(5-b-n)-(6-b-(n+theta)));checks['uniform_s_threshold']=S.expand(6-b-ss-((S.Rational(7,2)-ss)+(S.Rational(5,2)-b)));assert all(t==0 for t in checks.values())
out={'start_utc':start,'utc':p.now(),'status':'PASS_HIGHER_ORDER_MODAL_PREMISES_AND_SYMBOLIC_FACTOR_IDENTITIES','proof_sha256':p.sha(D/'PROOF.md'),'code_sha256':p.sha(Path(__file__)),'parent_files':pins,'parent_pin_count':len(pins),'actual':{n:str(v) for n,v in actual.items()},'knots_checked':len(knots),'distinct_knots':len(unique),'modes':modes,'shapes':shapes,'outer_exponents':list(map(str,exponents)),'symbolic_identities':{n:str(v) for n,v in checks.items()},'scope':'Exact scalar/knot premises and finite derivative algebra only. Exact canonical joins are inherited; no fresh join recomputation, interval enclosure, physical norm or analytical Sobolev conclusion from finite checks.'};p.write(E/'check.json',out);print(json.dumps({n:out[n] for n in ['start_utc','utc','status','parent_pin_count','actual','knots_checked','distinct_knots','symbolic_identities']}))

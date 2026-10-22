from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import sys,os,json
sys.dont_write_bytecode=True
for n in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[n]='1'
import numpy as np
import sympy as S
from flint import arb,fmpq,ctx
ctx.prec=256;ctx.threads=1
R=Path(__file__).resolve().parents[3];D=R/'research/weak_axis_compact_mapping';E=D/'evidence';sys.path.insert(0,str(R/'research/full_derivative_norm_bound_v2/code'));import protocol as p
start=p.now();pf=p.load(E/'proof_first.json');assert p.sha(D/'PROOF.md')==pf['proof_sha256']=='3bd85b7a29499ddd57fc3e13335bb8571c54f2aefcfec1fd93ba306c3a6de6a7'
parent='research/variable_transport_graph_obstruction/evidence/verdict.json';pv=p.load(R/parent);assert p.sha(R/parent)=='f4c7ffb261a3e26b51011fde486202d577ec2b254cb5a7509d9d475604cb0b6c';assert pv['status'].startswith('CONFIRMED');pins=dict(pv['files']);p.pin(pins,parent);p.rehash(pins)
# Parent199 already replaces six old mutable foreign files by byte-identical local snapshots.
# This audit never substitutes newly changed producer files into that chain.
npz=R/'research/modal_exactification/evidence/trial_v2_h0.008.npz';assert p.sha(npz)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
with np.load(npz,allow_pickle=False) as z:
 vals={n:F.from_float(float(z[n].item())) for n in ['k','bi','bo']};knots=[F.from_float(float(x)) for x in z['knots']];degree=int(z['p']);modes=int(z['M']);shapes={n:list(z[n].shape) for n in ['S','D','Aout','Ei','Eo']}
 for n in ['S','D','Aout','Ei','Eo','knots']:assert np.isfinite(z[n]).all()
k,bi,bo=map(vals.get,['k','bi','bo']);assert 0<k<F(1,2) and bi>2 and bo>3-k and degree==7 and modes==260
counts=Counter(knots);distinct=sorted(counts);assert knots==sorted(knots) and counts[distinct[0]]==counts[distinct[-1]]==8 and all(counts[t]==1 for t in distinct[1:-1]) and len(distinct)==1559
assert shapes=={'S':[260,1565],'D':[260,7],'Aout':[260,10],'Ei':[260,7],'Eo':[260,7]}
raw=p.load(R/'data_exact/modal_v2.json');pairs=raw['outer_jl'];assert pairs==[[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[0,1],[1,1],[2,1],[0,2]]
exponents=[(k-3)-j*(1-k)-2*l for j,l in pairs];assert max(exponents)==k-3 and len(set(exponents))==10 and all(e<k-3 for e in exponents[1:])
s=F(153,50);theta=s-3;actual=vals|{'s':s,'theta':theta,'center_rate_infimum':6-F(5,2)-s,'far_rate_minimum':3-k,'inner_factor_gap':bi-2,'outer_correction_gap':bo+k-3};assert actual['center_rate_infimum']==F(11,25)>0 and actual['far_rate_minimum']>F(5,2)
# General factor and pullback checks use arbitrary smooth functions.
x,y,z,beta,b,kk,q,t=S.symbols('x y z beta b k q theta',real=True);aa=S.Function('a')(x,y);v1=S.Function('v1')(x,y);v2=S.Function('v2')(x,y);Q=S.Function('Q')(x,y)
rho=x*x*y*aa;g=x*v1*S.diff(rho,x)+y*v2*S.diff(rho,y);B=v1*(2*aa+x*S.diff(aa,x))+v2*(aa+y*S.diff(aa,y));checks={'exact_global_x2y_factor':S.expand(g-x*x*y*B)}
for pp in range(5):
 for qq in range(5-pp):
  f=S.diff(x*x*Q,y,qq)
  for _ in range(pp):f=x*S.diff(f,x)+beta*f
  C=S.diff(Q,y,qq)
  for _ in range(pp):C=x*S.diff(C,x)+(beta+2)*C
  checks[f'weighted_Euler_factor_p{pp}_q{qq}']=S.expand(f-x*x*C)
Fz=S.Function('F')(z,y);physical=S.exp(-beta*z)*Fz;checks['logarithmic_weight_conjugation']=S.simplify(S.exp(beta*z)*S.diff(physical,z)-S.diff(Fz,z)+beta*Fz)
checks['center_L2_exponent']=S.expand((5-2*b)+1+2*(3-q)-2*(6-b-q))
checks['far_L2_exponent']=S.expand((5-2*b)+1+2*(kk-6-q)-2*(kk-3-b-q))
checks['fractional_interpolation_exponent']=S.expand((1-t)*(3-b)+t*(2-b)-(6-b-(3+t)))
assert all(v==0 for v in checks.values()),checks
# Nontrivial shell geometry is analytic; these identities do not certify it.
def ball(q):q=F(q);return arb(fmpq(q.numerator,q.denominator))
def endpoint(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
ball_expr={'far_rate_minimum':3-ball(k),'inner_factor_gap':ball(bi)-2,'outer_correction_gap':ball(bo)+ball(k)-3};intervals={};windows={}
for name,v in ball_expr.items():
 lo,hi=endpoint(v.lower()),endpoint(v.upper());qv=actual[name];assert lo<=qv<=hi
 floor=qv*10**12;fl=floor.numerator//floor.denominator;dl,du=F(fl,10**12),F(fl+1,10**12)
 if dl==qv:dl-=F(1,10**12)
 assert dl<lo<=hi<du
 intervals[name]={'lower_exact':str(lo),'upper_exact':str(hi)};windows[name]=[str(dl),str(du)]
out={'start_utc':start,'utc':p.now(),'status':'PASS_WEAK_AXIS_EXACT_MODAL_HYPOTHESES_AND_FACTOR_IDENTITIES','proof_sha256':p.sha(D/'PROOF.md'),'code_sha256':p.sha(Path(__file__)),'parent_files':pins,'parent_pin_count':len(pins),'actual':{n:str(v) for n,v in actual.items()},'degree':degree,'modes':modes,'knots_checked':len(knots),'distinct_knots':len(distinct),'outer_exponents':list(map(str,exponents)),'shapes':shapes,'symbolic_identities':{n:str(v) for n,v in checks.items()},'arb256':intervals,'strict_windows':windows,'scope':'Qualitative compact-test membership only. Finite checks verify actual exponents and algebra, not Sobolev convergence, canonical harmonic estimates or any physical norm.'};p.write(E/'check.json',out);print(json.dumps({k:v for k,v in out.items() if k not in ['parent_files','arb256']}))

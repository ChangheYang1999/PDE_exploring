"""Exact endpoint audit and full predecessor authentication."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json,ast,sys
from flint import arb,ctx
from mpmath import iv
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];P=B/'research/localized_forcing';ctx.prec=256;iv.dps=120

def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for c in iter(lambda:f.read(1048576),b''):h.update(c)
 return h.hexdigest()
def read(p):return json.loads(p.read_text())
def bf(q):return arb(q.numerator)/q.denominator
def vf(q):return iv.mpf(q.numerator)/q.denominator
prior=read(P/'evidence/verdict.json');assert prior['status']=='CONFIRMED_FINITE_COMPONENTS_PHYSICAL_FORCING_OPEN'
pins=dict(prior['files']);assert len(pins)==139
for f,h in pins.items():assert sha(B/f)==h,f
src=P/'source/runs/forcing/p9_K64_n16_P8_merged.json';raw=read(src)
a=read(D/'evidence/arb.json');e=read(D/'evidence/exact_iv.json')
assert a['status']=='PASS_CONDITIONAL_DIRECT_ARITHMETIC' and e['status']=='PASS_CONDITIONAL_EXACT_MOMENT_ARITHMETIC'
assert a['source_sha256']==e['source_sha256']==sha(src)
assert a['M']==e['M']=='9363/1000000' and a['row_order_sha256']==e['row_order_sha256']
assert a['row_count']==e['row_count']==43949 and a['nonnegative_checks']==e['nonnegative_checks']==483439
assert read(D/'evidence/proof_first.json')['sha256']==sha(D/'PROOF.md')
s=raw['sup_D_eps']['B94'];sq=sum(F.from_float(s[k])**2*m for k,m in [('2_0',1),('1_1',2),('0_2',1)])
assert sq==F(e['hessian_squared_exact']) and F(e['hessian_squared_margin'])==F(a['M'])**2-sq>0
assert F(a['global_hessian_bound']['upper'])<F(a['M'])
assert bf(F(a['M']))**2>bf(sq) and vf(F(a['M']))**2>vf(sq)
# The two cutoff engines proved a sum of absolute radial terms, not just |Delta tau|.
expressions={}
for fn,expr in [('check_cutoff.py','hi(T[2]+T[1]*inv)'),('check_cutoff_iv.py','high(Ts[2]+Ts[1]*inv)')]:
 tree=ast.parse((P/'code'/fn).read_text());target=ast.dump(ast.parse(expr,mode='eval').body,include_attributes=False)
 found=[]
 for node in ast.walk(tree):
  if isinstance(node,ast.Call) and isinstance(node.func,ast.Name) and node.func.id=='dict':
   for kw in node.keywords:
    if kw.arg=='TL':found.append(ast.dump(kw.value,include_attributes=False))
 assert target in found,(fn,found);expressions[fn]=expr
ceilings={'1':['2.99137','2898.53','5.94978'],'500':['4.55066','4779.82','9.12448']};checks=0;result={}
for lam in ['1','500']:
 aa=a['results'][lam];ee=e['results'][lam];j3=F(ee['J3_exact']);j4=F(ee['J4_exact']);assert j3>0 and j4>0
 for k,z in [('J3',j3),('J4',j4)]:assert F(aa[k]['lower'])<=z<=F(aa[k]['upper']);checks+=1
 exact_tests=[j3<F(ceilings[lam][0])**2,j4<F(ceilings[lam][1])**2,j3**9*j4<F(ceilings[lam][2])**20]
 assert all(exact_tests);checks+=3
 for k,q in zip(['N3','N4','N31'],map(F,ceilings[lam])):
  al,au=map(F,[aa[k]['lower'],aa[k]['upper']]);el,eu=map(F,[ee[k]['lower'],ee[k]['upper']])
  assert 0<al<=el<=eu<=au<q;checks+=2
 result[lam]={'strict_conditional_ceilings':ceilings[lam],'exact_squared_and_twentieth_power_tests':exact_tests}
# Independently derive the two polynomial coefficient lists from the nine moments.
z={k:F(v) for k,v in e['moments'].items()}
p3=[z['dd'],z['ll']+2*z['bd'],z['bb']+2*z['vl'],z['vv']]
p4=[z['ee'],4*z['le'],4*z['ll']+2*z['ve'],4*z['vl'],z['vv']]
assert p3==list(map(F,e['polynomial_J3'])) and p4==list(map(F,e['polynomial_J4']))
for lam in ['1','500']:
 x=F(int(lam)**2)
 assert sum(v*x**i for i,v in enumerate(p3))==F(e['results'][lam]['J3_exact'])
 assert sum(v*x**i for i,v in enumerate(p4))==F(e['results'][lam]['J4_exact'])
# Both scripts exclude all five original F fields and producer imports structurally.
for fn in ['arb_direct.py','exact_moments.py']:
 tree=ast.parse((D/'code'/fn).read_text())
 literals={n.value for n in ast.walk(tree) if isinstance(n,ast.Constant) and isinstance(n.value,str)}
 assert not literals.intersection({'F0','F1','FL','FL1','FL2','I3','I4','bound_order3','bound_order4','bound_order_3_1'})
 imports=[n.module for n in ast.walk(tree) if isinstance(n,ast.ImportFrom)]
 assert not any(m and m.startswith(('cert_','midrad')) for m in imports)
for rel in ['PROOF.md','NUMERICAL_RESULT.md','evidence/proof_first.json','code/arb_direct.py','code/exact_moments.py','code/audit.py','evidence/arb.json','evidence/exact_iv.json']:
 p=D/rel;pins[str(p.relative_to(B))]=sha(p)
p=P/'evidence/verdict.json';pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_CONDITIONAL_HESSIAN_REPLACEMENT_REQUIRES_REVIEW','prior_pins':139,'rows_each_engine':43949,'nonnegative_checks_each_engine':483439,'finite_endpoint_tests':checks,'exact_polynomial_coefficients':9,'cutoff_triangle_expressions':expressions,'results':result,'pins':dict(sorted(pins.items())),'scope':'Fully checked finite postprocessing theorem, conditional on physical residual derivatives. No original FL1/FL2 or physical norm accepted.'}
(D/'evidence/audit.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],len(pins),'pins',checks,'endpoint checks')

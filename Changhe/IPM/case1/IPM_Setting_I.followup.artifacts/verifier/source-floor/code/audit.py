from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
p=ROOT.parents[1]/'numerics/runs/opchannel_n120m48_S.json'
p=p.resolve();raw=p.read_bytes();data=json.loads(raw)
x=s.symbols('x',positive=True);w=-2*x*(1-x*x)/(1+x*x);g=x*x/(1+x*x);h=3-s.diff(w,x);a=(s.diff(g,x)-s.diff(w,x,2))/2;b=-s.diff(a,x)/3;F=-a*s.diff(g,x)-b*g;H=x**7/((1+x*x)**3*(1-x*x));Q=(11-5*x*x)/(6*x**5);G=x*x*(6*x**4+6*x**3+6*x*x+11*x+11)/(6*(x+1)*(x*x+1)**3)
checks={'first_axis_equation':s.factor(w*s.diff(g,x)+(h-1)*g),'homogeneous_equation':s.factor(w*s.diff(H,x)+(3*h-1)*H),'primitive':s.factor(s.diff(Q,x)-F/(w*H)),'selected_formula':s.factor(G-H*(Q-Q.subs(x,1))),'third_equation':s.factor(w*s.diff(G,x)+(3*h-1)*G-F)}
assert all(v==0 for v in checks.values())
B=-Q.subs(x,1);ell=s.limit(G/H,x,1);C=s.expand(s.series(G/H,x,0,1).removeO()).coeff(x,0);assert B==-1 and ell==0 and C==-1 and s.limit(G,x,1)==s.Rational(5,12)
rows=[]
for mode in data['modes']:
 base=mode['variants']['base'];row={'mode_zero_based':mode['mode'],'base_in5_squared_fraction':(base['in5']/base['norm'])**2,'variants':{}}
 for name,v in mode['variants'].items():
  assert abs(v['norm']**2-v['in5']**2-v['out5']**2)<max(1e-30,2e-14*v['norm']**2)
  row['variants'][name]={'in5_relative_vector_change':v['diff_in5']/base['in5'],'in5_relative_norm_change':abs(v['in5']-base['in5'])/base['in5'],'total_relative_vector_change':v['diff_norm']/base['norm']}
 rows.append(row)
out={'date':datetime.now(timezone.utc).isoformat(),'source':str(p),'md5':hashlib.md5(raw).hexdigest(),'scope':'Exact independent symbolic hierarchy; scalar arithmetic on source-provided channel diagnostics, not independent physical actions.','symbolic_residuals':{k:str(v) for k,v in checks.items()},'B3':str(B),'ell3':str(ell),'C0':str(C),'G3_at_source':str(s.limit(G,x,1)),'center_series':str(s.series(G,x,0,9)),'rows':rows,'algebraic_accuracy_factor_from_2.11e-4_to_1e-6_if_p2_8':211**(1/2.8)}
(ROOT/'verification/opchannel_source.json').write_bytes(raw);(ROOT/'verification/audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));print('ALL_SYMBOLIC_AND_SCALAR_CHECKS_PASS')
